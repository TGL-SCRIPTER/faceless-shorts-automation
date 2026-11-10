# Workflow design

This documents the intended workflow; it is not yet a live Zapier automation.

## 1. Coordinator
- Read requirements and recent topic history.
- Verify Claude, OpenCode, and Codex availability.
- If Codex is unavailable, mark the three-agent batch blocked unless the user changes the requirement.
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

## Concurrency note
A shared JSON file does not provide transactional locking. Use one coordinator as the sole writer for assignment reservations and batch release. Run sequentially until proper orchestration exists.
