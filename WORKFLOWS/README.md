# Workflow design

This is the intended architecture, not yet a live scheduler or command listener.

## 1. Shared knowledge cache
See `CACHE/README.md`, `CACHE/MANIFEST.json`, and `SHARED/KNOWLEDGE_CACHE_PROTOCOL.md`.
- GitHub `main` remains the source of truth for permanent instructions.
- A single coordinator syncs stable files when the source commit changes and publishes one immutable versioned bundle to durable shared storage.
- Each agent runner keeps a local copy keyed by repository + commit SHA and reuses it while verified current.
- Only the small cache metadata/version record needs checking at task start. Do not fetch all permanent instruction files again when the cache is valid.
- Refresh global control, daily assignments, task status, and topic history at every batch; these are live state, not permanent knowledge.
- Publish cache updates atomically after checksums/manifest validation. Keep the previous known-good bundle for rollback.
- A failed sync must not silently fall back to stale rules.
- Separate agent environments cannot share a local disk cache by themselves. A durable shared-storage adapter and coordinator runner are required.

## 2. Command interface
See `COMMANDS.md` for the exact command contract.
- `/short` sets global mode to running, starts/resumes the daily educational Shorts workflow, and enables the configured publishing schedule. Repeated calls are idempotent.
- `/unshort` sets global mode to paused, disables future scheduled runs, and cancels pending runs/tasks. Running work is stopped gracefully where supported, checkpointed, and left resumable.
- A command dispatcher must authenticate the sender, parse exact commands, update the control state, and call the scheduler/runner APIs. Unknown commands must not change state.

## 3. Coordinator
- Read the active shared knowledge bundle plus live control state, assignments, task status, topic history, and publishing queue.
- Verify Claude, OpenCode, Codex, and ChatGPT availability plus each agent's actual tools and rendering capability.
- Reserve four distinct educational topics, angles, hooks, story formats, dominant 2D styles, and agent characters before generation.
- ChatGPT counts as an unattended agent only when a supported scheduled runner/API is implemented and verified; an interactive ChatGPT chat or Zapier MCP connection alone is not enough.
- Use one coordinator as the only writer for assignments, queue state, control state, and publishing release.

## 4. Generation
Each available agent creates one assigned educational 2D Short using only its own fixed character, then returns the video and metadata to shared storage. Agents never upload. Reaction-led content is out of scope.

## 5. OpenCode context and quota handling
- At 90% context, checkpoint and continue in a new session from the next incomplete step.
- A GLM/provider usage limit is separate: pause calls, checkpoint, and use a verified permitted fallback if one is already available; otherwise wait for reset.
- Never guess reset times, bypass limits, rotate accounts, or silently use paid models.

## 6. Validation
Check file existence/playability, genuine 2D output, educational takeaway, character exclusivity, title/description, sources, rights, voice preset, and topic/angle/hook/story/style uniqueness. Reject invalid or incomplete videos.

## 7. Persistent queue and release
- Store all validated videos and metadata in durable shared storage.
- Normal daily target/cap is four videos.
- At 18:00 Asia/Kolkata, if four validated videos are ready, schedule four with one common publish timestamp.
- If fewer than four are ready at 18:00, wait until 00:00 and schedule all validated available queue items together.
- Normal overflow carries forward. At 15 validated queued videos, release the entire validated backlog together as one coordinated batch.
- The platform may not make videos visible at the exact same second; record the scheduled and actual timestamps.

## 8. Upload and comment
- Coordinator uploads/schedules only after validation.
- Use stable batch/video idempotency keys and reconcile partial failures before retrying.
- After each successful upload, attempt the configured channel comment once. YouTube comments do not support Markdown bold; configured Unicode bold-style text is used. If comments are disabled or permission is missing, record manual action.

## 9. Notifications
Emit structured events for quota/expiry, missing outputs at 18:00/00:00, model fallback, manual actions, render/storage/upload failures, comment failures, publishing results, and backlog threshold.
WhatsApp is not configured yet. A WhatsApp Business/Twilio/Zapier route, recipient secret, provider approval, and successful test are required before claiming delivery.

## 10. Operational status
The knowledge-cache design and manifest are documented, but no coordinator sync runner, durable shared-storage adapter, agent cache loader, command dispatcher, scheduler, agent invocation adapters, YouTube scheduled publishing, comments, or WhatsApp delivery are live yet. Do not describe these systems as operational until implemented and tested end to end.

## Concurrency
A shared JSON file is not an atomic lock. Use one coordinator writer and a transactional queue store before running agents concurrently.
