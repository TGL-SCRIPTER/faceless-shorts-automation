# Shared master rules

All agents read this file, VIDEO_REQUIREMENTS.md, STYLE_LIBRARY.md, topic history, today's assignment, and their own instructions before generation.

## Daily batch
- Exactly three Shorts per daily batch: one each from Claude, OpenCode, and Codex.
- Codex must be verified available. If unavailable, report it and mark the batch blocked; never pretend or silently substitute.

## 2D only
- Every finished Short must be 2D animation.
- 3D animation, 3D renders, and 3D-looking scenes are not allowed.
- Explicitly confirm 2D-only production before submission.

## Skill-first
- Inspect and use the installed Faceless Shorts skill for ideas, templates, formats, styles, and production methods.
- Check other already-installed relevant skills when useful.
- If no suitable skill idea exists, create an original idea and reserve/check it with the coordinator.
- Do not claim a skill was inspected unless accessible. Do not install dependencies, buy services, or change account settings without approval.

## Uniqueness
Coordinator reserves all three assignments before agents start. Compare topic, entities, angle, hook, story progression/payoff, and primary 2D visual style. A different title alone is not enough. Reject exact and substantial semantic overlap. Check recent topic history.
A shared JSON file is not an atomic lock. Use one coordinator as the sole assignment writer; until orchestration exists, assign sequentially.

## Voice separation
Claude's voice-over voice must differ from OpenCode's. Prefer three distinct voices. Record exact provider and preset for every video. Report limitations honestly.

## Sources and rights
Verify factual claims with reliable sources. Public description must have a clearly labelled Sources section listing source/publisher names only, without URLs. Keep research URLs privately in task metadata when practical. Do not fabricate citations or use unlicensed music, footage, characters, or copied scripts.

## Deliverables
Each agent submits: finished vertical 2D video, title, sectioned description with Sources, topic/angle/hook/story format/visual style, voice provider and preset, source names and private references, asset/licensing notes, and 2D confirmation.

## Upload gate
Agents never upload directly. Upload only when all three outputs exist, are readable, have complete metadata, pass uniqueness and 2D checks, have sources and rights checked, and meet voice separation. If any one fails, hold all three. Use idempotency keys and record YouTube IDs/timestamps.
A single batch trigger may start three separate upload actions; do not promise exact same-second publication.

## Safety and quality
Avoid harmful, deceptive, age-inappropriate, or sensational misinformation. Respect YouTube policies and creator rights.
