# Shared knowledge cache

## Purpose
Reduce repeated GitHub reads and repeated prompt/context loading by maintaining one versioned knowledge bundle for all four agents.

## Intended architecture
1. GitHub `main` remains the source of truth.
2. A single coordinator sync process reads the files listed in `MANIFEST.json` when the source commit changes.
3. The coordinator writes an immutable, versioned bundle to the configured durable shared-storage provider.
4. Each agent runner keeps a local copy keyed by repository + commit SHA.
5. At task start, an agent checks the small cache metadata record. If its commit is current, it reuses the cached bundle. If stale, it obtains the latest bundle before generating.
6. Dynamic files listed under `always_fresh_files` are fetched at batch start and are never trusted from the permanent cache.
7. If sync or validation fails, stop generation rather than silently using stale rules.

## Cache rules
- Cache key: `TGL-SCRIPTER/faceless-shorts-automation:main:<commit-sha>`.
- Store source commit SHA, file paths, per-file SHA-256 checksums, generated-at timestamp, and schema version.
- Publish a new bundle atomically only after all required files pass validation.
- Keep the previous known-good bundle for rollback.
- Never cache secrets, access tokens, private user data, generated videos, or transient task state in this knowledge bundle.
- Agents must not independently rewrite the shared bundle.
- A changed source commit invalidates the old bundle; changed files can be fetched incrementally, but the published bundle must represent one consistent commit.

## Important implementation boundary
This folder currently defines the cache contract and manifest only. It is not yet a running cache service. A coordinator runner and a durable shared-storage adapter must be connected and tested before claiming that agents are actually reusing one cache. Separate agent environments cannot share an ordinary local disk cache automatically.
