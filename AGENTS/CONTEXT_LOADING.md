# Agent context loading

This is the mandatory startup contract for every agent. GitHub `main` is the source of truth.

## Read only the required context

Use connected GitHub/repository tools to fetch these files from `main` in this order:

1. `CACHE/MANIFEST.json` — determines the exact stable-file and live-file lists.
2. `AGENTS.md` — repository-wide rules.
3. Every shared path in `CACHE/MANIFEST.json` → `files`, plus only your own role file. Never read another agent's role file.
4. Every path in `CACHE/MANIFEST.json` → `always_fresh_files` — fetch directly from GitHub at the start of every batch.

Do not fetch unrelated repository files, other agents' role instructions, generated videos, or old task artifacts. Do not scan the repository tree. If a listed file is unavailable, stop and report the exact missing path.

## Stable knowledge reuse

- Reuse stable shared instructions already loaded in the current session while the source commit is unchanged.
- At a new session, fetch the required stable files again unless a verified local bundle is already available.
- Record the exact `main` commit SHA used. If the connected tool cannot verify the commit/ref, report that limitation rather than claiming freshness.
- GitHub Actions cache artifacts are optional packaged copies, not required for reading. Do not make task startup depend on downloading an artifact.
- A verified local bundle may replace individual stable-file fetches only when its repository, source commit, manifest, and all SHA-256 checksums validate. Always fetch the four live files directly from GitHub.

## Batch gate

Refresh `TASKS/automation_control.json`, `TASKS/daily_assignments.json`, `TASKS/task_status.json`, and `SHARED/TOPIC_HISTORY.json` for every batch. Proceed only if global mode is running and this agent has one clear, unclaimed assignment. Otherwise stop and report the blocker.

## Context receipt

Before production, report agent name, verified branch/commit SHA (if exposed), stable files loaded, live files refreshed, assigned batch/task ID, global mode, and any missing file/tool limitation.

Never claim files were read, a cache was downloaded, or integrity was checked unless that action actually succeeded.
