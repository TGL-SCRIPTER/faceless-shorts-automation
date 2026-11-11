# Knowledge cache and agent loading protocol

## Source of truth
GitHub `main` is the source of truth. The Actions artifact is optional packaged cache storage with 90-day retention. It is not automatically injected into agent context and is not required for agents to read instructions.

## Minimal startup reads
Every agent follows `AGENTS/CONTEXT_LOADING.md`:
- Read `CACHE/MANIFEST.json` and `AGENTS.md`.
- Read shared stable files listed in the manifest and only that agent's own role file. Never read other agents' role files.
- Fetch all four `always_fresh_files` directly from GitHub for every batch.
- Do not scan or fetch unrelated repository files.

## Reuse and integrity
Reuse stable context within a session while the source commit remains unchanged. A local bundle may replace individual stable-file reads only after repository, source commit, schema, and every SHA-256 checksum validate. Always refresh live files directly from GitHub. If a listed file is missing or freshness cannot be verified, report the blocker and stop.

## Artifact workflow
GitHub Actions packages manifest files and checksums for optional download. It does not invoke agents or inject content into Claude, OpenCode, Codex, or ChatGPT. Each agent must have its own working GitHub/repository access.

## Not implemented
This protocol does not implement a daily scheduler, agent invocation, video rendering, coordinator, YouTube publishing, command dispatcher, or WhatsApp notifications.
