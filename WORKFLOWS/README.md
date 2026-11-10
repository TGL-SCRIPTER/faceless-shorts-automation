# Workflow design

This documents the intended workflow; it is not yet a live Zapier automation.

## 1. Coordinator
- Read requirements and recent topic history.
- Verify Claude, OpenCode, and Codex availability and their actual connected tools.
- If any agent cannot access its assignment or produce a compliant output, mark the three-agent batch blocked; do not silently substitute another agent.
- Reserve three distinct topics, angles, hooks, story formats, and dominant 2D visual treatments before launching agents.
- Run semantic overlap checks against each other and recent history.
- Write assignments once, then launch agents.

## 2. Generation
Each agent reads its own instructions, creates one 2D Short, and returns video plus metadata to shared storage. Agents never publish or upload.

## 3. Validation
Check file existence/playability, 2D-only production, title/description, sources, rights, voice preset, and topic/angle/hook/story/style uniqueness.

## 4. Batch gate
Proceed only when all three outputs pass. If one fails, hold the entire batch and report the failure.

## 5. Upload
One batch-start event may trigger three separate YouTube upload actions. Use stable batch and per-video idempotency keys. Record YouTube IDs, status, and timestamps. Reconcile partial failures before retrying to avoid duplicates.

## Temporary usage-limit recovery
- Read `TASKS/retry_policy.json` and implement the pause/resume behavior in `SHARED/USAGE_LIMIT_RECOVERY.md`.
- A temporary provider quota/rate-limit response pauses only that agent and stores its checkpoint and reset/cooldown time. The coordinator retries the same assignment after the wait, subject to the retry cap.
- Keep the full batch and upload gate on hold until all three videos pass. Authentication, billing, suspension, policy, or unknown errors require manual action.
- The current repository is still a design scaffold: this policy does not run until a scheduled coordinator workflow and supported agent invocation integrations are implemented and enabled.

## Concurrency note
A shared JSON file does not provide transactional locking. Use one coordinator as the sole writer for assignment reservations and batch release. Run sequentially until proper orchestration exists.
