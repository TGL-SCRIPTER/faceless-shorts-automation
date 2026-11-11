# Knowledge cache protocol

## Storage and source of truth
GitHub `main` is the source of truth. GitHub Actions builds a complete cache bundle
and publishes it as a downloadable Actions artifact. No external cloud storage is
required. Artifacts are retained for 90 days.

## What belongs in the cache
Stable instructions, production standards, character definitions, role instructions,
style definitions, and stable publishing/retry policies listed in
`CACHE/MANIFEST.json`.

## What must remain live
The global pause/run state, today's assignments, current task statuses, topic history,
and any per-batch data. Refresh these directly from GitHub at the start of every batch.
Never let a stale cached assignment or topic history authorize duplicate work.

## Startup sequence for every agent
1. Identify the latest successful **Build GitHub knowledge cache** workflow run.
2. Download its artifact and confirm its source commit matches the intended `main`
   commit.
3. Verify the bundle schema, repository, commit SHA, and per-file SHA-256 checksums.
4. Refresh every `always_fresh_files` directly from GitHub.
5. Confirm the global mode is running and the task is assigned to this agent.
6. Load the stable bundle into the task context before generation.

## Update sequence
1. A relevant push to `main` triggers the cache workflow.
2. The workflow reads all manifest files from that exact checkout.
3. It builds the full bundle and checksum index.
4. GitHub Actions stores both files in a commit-specific artifact.
5. Agents adopt the new bundle at their next safe task boundary.

## Failure behavior
If the workflow fails, the artifact is missing, the source commit does not match,
or integrity checks fail, do not claim synchronization succeeded. Do not silently
use an older bundle as current. Keep the last artifact only for diagnosis/rollback,
marked stale.

## Important boundary
This artifact workflow stores and versions the cache, but does not automatically
download it into Claude, OpenCode, Codex, or ChatGPT. Each agent runner still needs
a download-and-load step. It also does not implement the project dispatcher,
scheduler, or publishing automation.
