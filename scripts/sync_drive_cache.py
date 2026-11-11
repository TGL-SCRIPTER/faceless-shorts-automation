#!/usr/bin/env python3
"""Build and sync the stable knowledge cache to Google Drive."""
import base64
import hashlib
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone

from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

OWNER_REPO = "TGL-SCRIPTER/faceless-shorts-automation"
BRANCH = "main"
FOLDER_ID = os.environ["GOOGLE_DRIVE_FOLDER_ID"]
SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN = os.environ["GITHUB_TOKEN"]
API = "https://api.github.com/repos/" + OWNER_REPO
DRIVE = "https://www.googleapis.com/drive/v3/files"

def github_json(path):
    req = urllib.request.Request(
        API + path,
        headers={"Authorization": "Bearer " + TOKEN,
                 "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req) as response:
        return json.load(response)

def github_text(path, ref):
    url = API + "/contents/" + urllib.parse.quote(path, safe="/") + "?ref=" + urllib.parse.quote(ref)
    data = github_json(url[len(API):])
    raw = base64.b64decode(data["content"])
    return raw.decode("utf-8"), data["sha"]

def drive_session():
    info = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"])
    credentials = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    return AuthorizedSession(credentials)

def upsert_drive(session, name, content, mime="application/json"):
    query = urllib.parse.urlencode({
        "q": "'" + FOLDER_ID + "' in parents and name='" + name.replace("'", "\\'") + "' and trashed=false",
        "fields": "files(id,name)",
        "pageSize": "10"
    })
    with session.get(DRIVE + "?" + query) as response:
        response.raise_for_status()
        matches = response.json().get("files", [])
    metadata = {"name": name, "mimeType": mime}
    boundary = "cache-sync-boundary"
    body = (
        "--" + boundary + "\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n" +
        json.dumps(metadata) + "\r\n--" + boundary +
        "\r\nContent-Type: " + mime + "\r\n\r\n" + content +
        "\r\n--" + boundary + "--"
    ).encode("utf-8")
    if matches:
        file_id = matches[0]["id"]
        url = DRIVE + "/" + file_id + "?uploadType=multipart"
        method = session.patch
    else:
        url = DRIVE + "?uploadType=multipart&fields=id,name"
        method = session.post
    with method(url, data=body, headers={"Content-Type": "multipart/related; boundary=" + boundary}) as response:
        response.raise_for_status()
        result = response.json()
    # Remove accidental duplicates with the same name after successful update.
    if matches:
        for duplicate in matches[1:]:
            session.delete(DRIVE + "/" + duplicate["id"]).raise_for_status()
    print("Synced", name, result.get("id"))

def main():
    ref = github_json("/git/ref/heads/" + BRANCH)
    commit = ref["object"]["sha"]
    manifest_text, manifest_blob_sha = github_text("CACHE/MANIFEST.json", commit)
    manifest = json.loads(manifest_text)
    stable_paths = list(manifest["files"])
    extra_paths = ["CACHE/MANIFEST.json", "CACHE/README.md", "SHARED/KNOWLEDGE_CACHE_PROTOCOL.md"]
    paths = list(dict.fromkeys(stable_paths + extra_paths))
    files = {}
    for path in paths:
        content, blob_sha = github_text(path, commit)
        files[path] = {
            "git_blob_sha": blob_sha,
            "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "content": content
        }
    bundle = {
        "schema_version": 1,
        "repository": OWNER_REPO,
        "branch": BRANCH,
        "source_commit": commit,
        "synced_at": datetime.now(timezone.utc).isoformat(),
        "file_count": len(files),
        "files": files
    }
    bundle_text = json.dumps(bundle, ensure_ascii=False, indent=2)
    index = {
        "schema_version": 1,
        "repository": OWNER_REPO,
        "branch": BRANCH,
        "source_commit": commit,
        "synced_at": bundle["synced_at"],
        "bundle_file": "KNOWLEDGE-CACHE.json",
        "file_count": len(files),
        "files": {p: {"git_blob_sha": v["git_blob_sha"], "sha256": v["sha256"]} for p, v in files.items()},
        "always_fresh_files": manifest.get("always_fresh_files", []),
        "note": "Automatically synced from GitHub main. Dynamic files are deliberately excluded."
    }
    session = drive_session()
    upsert_drive(session, "KNOWLEDGE-CACHE.json", bundle_text)
    upsert_drive(session, "CACHE-INDEX.json", json.dumps(index, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
