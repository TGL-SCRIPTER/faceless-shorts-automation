#!/usr/bin/env python3
"""Build a verified knowledge-cache bundle for GitHub Actions artifacts.

Uses only the Python standard library. No Google Cloud account, service account,
external storage, or third-party Python package is required.
"""
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "knowledge-cache"
MANIFEST_PATH = ROOT / "CACHE" / "MANIFEST.json"
EXTRA_PATHS = [
    "CACHE/MANIFEST.json",
    "CACHE/README.md",
    "SHARED/KNOWLEDGE_CACHE_PROTOCOL.md",
]

def main():
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    paths = list(dict.fromkeys(manifest["files"] + EXTRA_PATHS))
    files = {}
    for relative in paths:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(f"Required cache file is missing: {relative}")
        content = path.read_text(encoding="utf-8")
        files[relative] = {
            "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "content": content,
        }

    commit = os.environ.get("GITHUB_SHA", "local-build")
    built_at = datetime.now(timezone.utc).isoformat()
    bundle = {
        "schema_version": 1,
        "repository": "TGL-SCRIPTER/faceless-shorts-automation",
        "branch": os.environ.get("GITHUB_REF_NAME", "main"),
        "source_commit": commit,
        "built_at": built_at,
        "file_count": len(files),
        "files": files,
    }
    index = {
        "schema_version": 1,
        "repository": bundle["repository"],
        "branch": bundle["branch"],
        "source_commit": commit,
        "built_at": built_at,
        "bundle_file": "KNOWLEDGE-CACHE.json",
        "file_count": len(files),
        "files": {
            name: {"sha256": item["sha256"]}
            for name, item in files.items()
        },
        "always_fresh_files": manifest.get("always_fresh_files", []),
        "storage": "GitHub Actions artifact",
        "note": "Dynamic files are deliberately excluded and must be fetched live.",
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "KNOWLEDGE-CACHE.json").write_text(
        json.dumps(bundle, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (OUT / "CACHE-INDEX.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Built {len(files)} files for commit {commit}")
    print(f"Output: {OUT}")

if __name__ == "__main__":
    main()
