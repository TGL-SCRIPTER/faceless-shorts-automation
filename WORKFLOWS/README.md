# Workflow design

This is the intended architecture, not yet a live scheduler or command listener.

## 1. Command interface
See `COMMANDS.md` for the exact command contract.
- `/short` sets global mode to running, starts/resumes the daily educational Shorts workflow, and enables the configured publishing schedule. Repeated calls are idempotent.
- `/unshort` sets global mode to paused, disables future scheduled runs, and cancels pending runs/tasks. Running work is stopped gracefully where supported, checkpointed, and left resumable.
- A command dispatcher must authenticate the sender, parse exact commands, update the control state, and call the scheduler/runner APIs. Unknown commands must not change state.

## 2. Coordinator
- Read all shared rules, character registry, topic history, assignments, publishing policy, notification policy, and global control state.
- Verify Claude, OpenCode, Codex, and ChatGPT availability plus each agent's actual tools and rendering capability.
- Reserve four distinct educational topics, angles, hooks, story formats, dominant 2D styles, and agent characters before generation.
- ChatGPT counts as an unattended agent only when a supported scheduled runner/API is implemented and verified; an interactive ChatGPT chat or Zapier MCP connection alone is not enough.
- Use one coordinator as the only writer for assignments, queue state, control state, and publishing release.

## 3. Generation
Each available agent creates one assigned educational 2D Short using only its own fixed character, then returns the video and metadata to shared storage. Agents never upload. Reaction-led content is out of scope.

## 4. OpenCode context and quota handling
- At 90% context, checkpoint and continue in a new session from the next incomplete step.
- A GLM/provider usage limit is separate: pause calls, checkpoint, and use a verified permitted fallback if one is already available; otherwise wait for reset.
- Never guess reset times, bypass limits, rotate accounts, or silently use paid models.

## 5. Validation
Check file existence/playability, genuine 2D output, educational takeaway, character exclusivity, title/description, sources, rights, voice preset, and topic/angle/hook/story/style uniqueness. Reject invalid or incomplete videos.

## 6. Persistent queue and release
- Store all validated videos and metadata in durable shared storage.
- Normal daily target/cap is four videos.
- At 18:00 Asia/Kolkata, if four validated videos are ready, schedule four with one common publish timestamp.
- If fewer than four are ready at 18:00, wait until 00:00 and schedule all validated available queue items together.
- Normal overflow carries forward. At 15 validated queued videos, release the entire validated backlog together as one coordinated batch, overriding the normal four-video cap.
- The platform may not make videos visible at the exact same second; record the scheduled and actual timestamps.

## 7. Upload and comment
- Coordinator uploads/schedules only after validation.
- Use stable batch/video idempotency keys and reconcile partial failures before retrying.
- After each successful upload, attempt the configured channel comment once. YouTube comments do not support Markdown bold; configured Unicode bold-style text is used. If comments are disabled or permission is missing, record manual action.

## 8. Notifications
Emit structured events for quota/expiry, missing outputs at 18:00/00:00, model fallback, manual actions, render/storage/upload failures, comment failures, publishing results, and backlog threshold.
WhatsApp is not configured yet. A WhatsApp Business/Twilio/Zapier route, recipient secret, provider approval, and successful test are required before claiming delivery.

## 9. Operational status
The repository currently contains policies and instructions only. A command dispatcher, scheduler, agent invocation adapters, durable shared storage, YouTube scheduled publishing, comments, and WhatsApp delivery still need implementation and end-to-end tests. The slash command specification is not itself a live listener. Do not describe the workflow as live until verified.

## Concurrency
A shared JSON file is not an atomic lock. Use a single coordinator writer and a transactional queue store before running agents concurrently.
