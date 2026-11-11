# Knowledge cache protocol

## What belongs in the cache
Stable instructions, production standards, character definitions, role instructions, style definitions, and stable publishing/retry policies listed in `CACHE/MANIFEST.json`.

## What must remain live
The global pause/run state, today's assignments, current task statuses, topic history, and any per-batch data. Refresh these from the source of truth at the start of every batch. Never let a stale cached assignment or topic history authorize duplicate work.

## Startup sequence for every agent
1. Ask the coordinator for the active bundle version and source commit SHA.
2. Reuse the local bundle only if its repository, branch, commit SHA, schema version, and integrity checks match the coordinator's active version.
3. If absent or stale, request the shared bundle; do not fetch every permanent file independently if the coordinator can supply the bundle.
4. Refresh all `always_fresh_files` directly through the coordinator's live data interface.
5. Confirm the global mode is running and the task is assigned to this agent.
6. Begin generation.

## Update sequence
1. A GitHub push to the configured branch signals the sync process.
2. The coordinator compares the new commit with the last successfully synchronized commit.
3. Fetch only changed cache-manifest files, plus any newly required files.
4. Rebuild and validate the complete versioned bundle.
5. Atomically publish it to durable shared storage and update the active pointer.
6. Agents adopt the new bundle at their next safe task boundary. Do not silently change instructions mid-render.
7. If the update changes safety, publishing, or command-control rules, pause new tasks until all runners acknowledge the new version.

## Failure behavior
- If shared storage is unavailable, do not claim synchronization succeeded.
- If an agent cannot verify bundle integrity/currentness, pause that agent and ask the coordinator to sync.
- Never fall back to a stale cache without an explicit coordinator-approved emergency policy.
- Retain the last known-good bundle for rollback, but mark it stale.

## Cost and context behavior
- The cache reduces repeated repository fetching and repeated instruction assembly.
- It does not eliminate the model's need to receive relevant instructions in its context. Each agent runner must load the cached bundle into its task context, ideally once per persistent worker/session.
- A new model session may need the bundle context reloaded from shared storage, but it does not need to fetch every source file from GitHub again.
