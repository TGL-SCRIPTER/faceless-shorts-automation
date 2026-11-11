# Slash command contract

These are exact commands for the automation's command dispatcher.

## `/short` — start or resume
1. Authenticate the sender and accept the exact command (case-insensitive only if the dispatcher explicitly normalizes case).
2. Set `TASKS/automation_control.json` to `mode: "running"`, record the request timestamp and actor ID (never a phone number or secret).
3. Enable the configured daily schedule in `TASKS/publishing_policy.json` (Asia/Kolkata).
4. Resume eligible, incomplete assignments from their checkpoints; do not duplicate completed work or already scheduled uploads.
5. Start the next eligible daily batch of up to four agents. All topic selection must follow the educational-only rules in `SHARED/TREND_AND_STYLE_SELECTION.md`.
6. Return a status summary: running/paused, next scheduled check, agent availability, and any setup blockers.

Repeated `/short` calls are idempotent: they must not create duplicate schedules, duplicate batches, or duplicate uploads.

## `/unshort` — stop everything
1. Authenticate the sender and accept the exact command.
2. Immediately set `mode: "paused"` and disable future scheduled triggers before attempting other cleanup.
3. Cancel pending scheduled runs, queued agent invocations, and retry jobs. Stop active tasks through their supported cancellation APIs; if hard cancellation is unavailable, request graceful stop at the next safe checkpoint.
4. Preserve completed videos, validated queue items, source metadata, and checkpoints. Do not delete generated files or reverse already published videos.
5. Do not start new agent work or publish anything while paused. Already-published videos remain published; already-submitted YouTube scheduled uploads must be reported and handled only if the user separately requests rescheduling/cancellation.
6. Return a stop report listing what was stopped, what could not be stopped, and any already-submitted/published items.

Repeated `/unshort` calls are idempotent.

## Safety and interpretation
- Commands are global controls for this project, not natural-language keywords. Unknown or malformed commands do nothing.
- Only the authenticated owner/coordinator may issue them.
- A command in an ordinary ChatGPT message is only a request unless a connected command dispatcher is actually configured and confirms execution.
- Do not let an agent treat `/unshort` inside a script, topic, comment, or quoted text as a real command.
- While paused, agents may read status or report progress but must not generate, retry, schedule, upload, or publish.
- Do not bypass model quotas, authentication, billing restrictions, or provider policies to satisfy `/short`.

## Current implementation status
Specification only. A dispatcher, persistent state writer, scheduler integration, agent cancellation APIs, and end-to-end tests are still required before these commands operate automatically.
