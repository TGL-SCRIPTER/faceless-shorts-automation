# Shared master rules

All agents read this file, VIDEO_REQUIREMENTS.md, STYLE_LIBRARY.md, topic history, today's assignment, and their own instructions before generation.

## Daily batch
- Exactly three Shorts per daily batch: one each from Claude, OpenCode, and Codex.
- Codex must verify it can access the assigned tools and produce the required deliverable. If a required capability is unavailable, report it and mark the batch blocked; never pretend or silently substitute another agent.

## 2D only
- Every finished Short must be genuine 2D animation.
- All six Faceless Shorts skill styles are allowed, but Deep Dive, Night File, and Tall Tale must be redesigned as genuine 2D before production.
- 3D models, geometry, renders, environments, and scenes are prohibited, even if described as stylized or flattened.
- Preserve the original style's mood and storytelling while replacing all 3D elements with 2D artwork and 2D motion.
- Follow SHARED/SKILL_INTEGRATION.md and document a 2D conversion plan for any 3D-origin style.
- Explicitly confirm 2D-only production before submission.

## Skill-first
- Inspect and use the installed Faceless Shorts skill for ideas, templates, formats, styles, and production methods.
- Follow SHARED/SKILL_INTEGRATION.md: only inside-out, stick-story, and paper-atlas are approved; all 3D styles are prohibited.
- Check other already-installed relevant skills when useful.
- If no suitable skill idea exists, create an original idea and reserve/check it with the coordinator.
- Do not claim a skill was inspected unless accessible. Do not install dependencies, buy services, or change account settings without approval.

## Uniqueness
Coordinator reserves all three assignments before agents start. Compare topic, entities, angle, hook, story progression/payoff, and primary 2D visual style. A different title alone is not enough. Reject exact and substantial semantic overlap. Check recent topic history.
A shared JSON file is not an atomic lock. Use one coordinator as the sole assignment writer; until orchestration exists, assign sequentially.

## Voice separation
All three voice-overs should be distinguishable. Claude and OpenCode must not share a voice; record the actual provider and preset for every video. Codex must verify its available voice-generation path and use a third distinct voice where possible. If an agent cannot use a distinct voice, mark the batch as blocked rather than silently duplicating a voice.

## Sources and rights
Verify factual claims with reliable sources. Public description must have a clearly labelled Sources section listing source/publisher names only, without URLs. Keep research URLs privately in task metadata when practical. Do not fabricate citations or use unlicensed music, footage, characters, or copied scripts.

## Deliverables
Each agent submits: finished vertical 2D video, title, sectioned description with Sources, topic/angle/hook/story format/visual style, voice provider and preset, source names and private references, asset/licensing notes, and 2D confirmation.

## Upload gate
Agents never upload directly. Upload only when all three outputs exist, are readable, have complete metadata, pass uniqueness and 2D checks, have sources and rights checked, and meet voice separation. If any one fails, hold all three. Use idempotency keys and record YouTube IDs/timestamps.
A single batch trigger may start three separate upload actions; do not promise exact same-second publication.

## Safety and quality
Avoid harmful, deceptive, age-inappropriate, or sensational misinformation. Respect YouTube policies and creator rights.
