# Shared master rules

All agents read this file, VIDEO_REQUIREMENTS.md, STYLE_LIBRARY.md, AGENT_CHARACTERS.json, topic history, today's assignment, and their own instructions before generation.

## Daily batch
- Four-agent target: one Short each from Claude, OpenCode, Codex, and ChatGPT.
- Each agent must verify its actual tools and production capabilities. If unavailable, mark that agent blocked/missing; never pretend or silently claim a completed output.
- Reserve four distinct assignments before agents start. If an agent is unavailable, the coordinator may publish the validated available queue at the configured midnight fallback; do not fabricate its output.

## Character separation
- Each agent has one fixed original character defined in `SHARED/AGENT_CHARACTERS.json`.
- The assigned agent may use only its own character. No cross-agent character reuse, swaps, or lookalike copies.
- Character identity, silhouette, palette, proportions, and signature accessories remain consistent across that agent's videos. Characters are original generic designs, not imitations of provider logos/mascots.

## 2D only
- Every finished Short must be genuine 2D animation.
- All six Faceless Shorts skill styles are allowed, but Deep Dive, Night File, and Tall Tale must be redesigned as genuine 2D before production.
- 3D models, geometry, renders, environments, and scenes are prohibited, even if described as stylized or flattened.
- Preserve the original style's mood and storytelling while replacing all 3D elements with 2D artwork and 2D motion.
- Follow `SHARED/SKILL_INTEGRATION.md` and document a 2D conversion plan for any 3D-origin style.
- Explicitly confirm 2D-only production before submission.

## Skill-first and uniqueness
- Inspect and use the installed Faceless Shorts skill for ideas, templates, formats, styles, and production methods.
- Follow `SHARED/SKILL_INTEGRATION.md`.
- Coordinator reserves four distinct assignments before agents start. Compare topic, entities, angle, hook, story progression/payoff, dominant 2D visual style, and character. A different title alone is not enough.
- A shared JSON file is not an atomic lock. Use one coordinator as the sole assignment writer; until orchestration exists, assign sequentially.

## Voice separation
- Record the actual voice provider and preset for every video. Prefer four distinguishable voices. If an agent cannot verify a usable voice, mark its output blocked for review rather than silently duplicating a voice.

## Sources and rights
- Verify factual claims with reliable sources. Public description must have a clearly labelled Sources section listing source/publisher names only, without URLs. Keep research URLs privately in task metadata when practical.
- Do not fabricate citations or use unlicensed music, footage, characters, or copied scripts.

## Deliverables
Each agent submits: finished vertical 2D video, title, sectioned description with Sources, topic/angle/hook/story format/visual style, voice provider and preset, source names and private references, asset/licensing notes, and 2D confirmation.

## Publishing and queue
- Follow `TASKS/publishing_policy.json`.
- Normal daily maximum/target is four published Shorts. At 18:00 Asia/Kolkata, if four validated videos are ready, schedule all four with the same publication timestamp.
- If fewer than four are ready at 18:00, wait until 00:00 Asia/Kolkata and then publish/schedule the validated available queue together.
- Extra finished videos remain in persistent storage and enter the next-day queue; never discard them.
- If the backlog reaches 15 validated videos, trigger a backlog-release batch containing the entire validated backlog together, overriding the normal four-video cap. Keep the release as one coordinated batch and record every video result.
- Platform processing may cause actual public availability to differ by seconds; use one common scheduled timestamp and report actual timestamps. Do not promise exact same-second visibility.
- Agents never upload. Coordinator alone uploads/schedules, with idempotency keys and partial-failure reconciliation.

## Comment
- After each successful upload, attempt the configured channel comment once per video: `𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞 𝐟𝐨𝐫 𝐦𝐨𝐫𝐞 𝐟𝐮𝐧 𝐟𝐚𝐜𝐭 𝐜𝐨𝐧𝐭𝐞𝐧𝐭 𝐚𝐧𝐝 𝐠𝐞𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐞𝐝!`
- YouTube comments do not support Markdown bold. Unicode bold-style characters are used to create a bold-looking effect. If comments are disabled or permission is missing, record a manual action; do not repeatedly retry or claim it succeeded.

## Temporary usage-limit recovery
- Follow `SHARED/USAGE_LIMIT_RECOVERY.md` and `TASKS/retry_policy.json`.
- Pause the affected agent, preserve its checkpoint and assignment, and resume the same work after reset/cooldown or through an approved fallback model. Keep the queue and publishing gate safe.
- Authentication, billing, suspension, policy, and unknown errors require manual intervention. Never bypass provider limits.

## Safety and quality
Avoid harmful, deceptive, age-inappropriate, or sensational misinformation. Respect YouTube policies and creator rights.
