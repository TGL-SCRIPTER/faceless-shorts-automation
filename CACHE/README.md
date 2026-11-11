# Shared knowledge cache

## GitHub-only implementation
GitHub `main` is the source of truth. A GitHub Actions workflow builds a complete,
checksummed cache bundle whenever a cache-relevant file changes and stores it as a
GitHub Actions artifact named `knowledge-cache-<commit-sha>`.

No Google Cloud account, Google Drive connection, service-account key, paid storage,
or third-party Python package is required. The build script uses Python's standard
library only.

## Using the cache
1. Open the repository's **Actions** tab.
2. Open the latest successful **Build GitHub knowledge cache** run.
3. Download its `knowledge-cache-<commit-sha>` artifact.
4. Verify the source commit and per-file SHA-256 values in `CACHE-INDEX.json`
   before loading the bundle into an agent.

Artifacts are retained for 90 days. A new cache artifact is built on each relevant
push, so use the artifact from the latest successful run for the current `main`
commit. A manual run is available through **Actions → Build GitHub knowledge cache
→ Run workflow**.

## Cache rules
- Cache key: `TGL-SCRIPTER/faceless-shorts-automation:main:<commit-sha>`.
- The bundle includes stable instructions and policies listed in `MANIFEST.json`.
- Dynamic files listed under `always_fresh_files` are intentionally excluded and
  must be fetched live at the start of each batch.
- Never cache secrets, access tokens, private user data, generated videos, or
  transient task state.
- If the latest workflow fails or its commit does not match `main`, do not use an
  older bundle as if it were current.
- This provides a shared downloadable cache artifact; it does not automatically
  inject the bundle into every agent's context. Each runner must download and load it.
