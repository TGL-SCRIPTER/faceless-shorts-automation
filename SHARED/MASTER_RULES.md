# Shared master rules

All agents read this file, VIDEO_REQUIREMENTS.md, STYLE_LIBRARY.md, AGENT_CHARACTERS.json, topic history, today's assignment, and their own instructions before generation.

## Educational channel identity
- This is an educational and interesting-facts channel. Topic discovery must stay within educational content: science, space, technology, nature, history, geography, engineering, useful everyday explanations, and verified surprising facts.
- Do not select reaction videos, reaction commentary, creator drama, celebrity gossip, memes, prank compilations, or trend-chasing entertainment formats.
- A trending subject is eligible only when it can be turned into a factual educational explainer or a verified fun fact. The video itself must teach something.
- Use a clear learning takeaway. Entertainment, humour, suspense, and storytelling may support learning but must not replace it.

## Daily batch
- Four-agent target: one Short each from Claude, OpenCode, Codex, and ChatGPT.
- Each agent must verify its actual tools and production capabilities. If unavailable, mark that agent blocked/missing; never pretend or silently claim a completed output.
- Reserve four distinct assignments before agents start. If an agent is unavailable, the coordinator may publish the validated available queue at the configured midnight fallback; do not fabricate its output.

## Trend-aware educational topic selection
- Research current educational interest and educationally relevant YouTube Shorts trends using accessible, legitimate sources and current data.
- Prioritize rising questions, science/space discoveries, technology explainers, historical/geographical curiosities, nature facts, and practical "how/why" topics with credible evidence.
- Exclude reaction-led trends and topics whose main appeal is watching someone else's reaction or drama.
- Record source, date checked, geography/language if known, and limitations. Never invent trend data, views, search volume, or viral probabilities.
- Score candidate topics using the rubric in `SHARED/TREND_AND_STYLE_SELECTION.md`. Treat the score as a prioritization aid, not a prediction or guarantee of virality.
- Prefer curiosity, a strong educational hook, a clear visual explanation, a surprising but verifiable payoff, broad audience relevance, and credible sources.
- Reserve four distinct educational topics/angles/hooks/story structures across the batch. Avoid duplicate or near-duplicate coverage.

## Adaptive style selection and creation
- For every selected topic, choose the visual/storytelling style that best serves comprehension, emotional tone, pacing, and available production tools—not simply the agent's favourite style.
- Evaluate the existing styles in `SHARED/STYLE_LIBRARY.md` first. If none is a good fit, the agent may propose and create a new original style for that specific topic.
- A new style must have a name, purpose, visual grammar, palette, scene rules, motion language, typography/caption rules, transition rules, sample storyboard, and production feasibility notes. Save its specification in `SHARED/CUSTOM_STYLES/` and add a summary to the style registry.
- New styles must remain genuine 2D, compatible with the agent's assigned character, distinct from other agents' styles in the same batch, and must not imitate a living artist, copyrighted franchise, or another creator's signature style.
- Do not create a new style merely for novelty. Reuse or refine a proven style when it fits the topic better.
- Record why the selected style fits the topic and whether it is existing, adapted, or newly created.

## Character separation
- Each agent has one fixed original character defined in `SHARED/AGENT_CHARACTERS.json`.
- The assigned agent may use only its own character. No cross-agent character reuse, swaps, or lookalike copies.
- Character identity, silhouette, palette, proportions, and signature accessories remain consistent across that agent's videos. Characters are original generic designs, not imitations of provider logos/mascots.

## 2D only
- Every finished Short must be genuine 2D animation.
- All six Faceless Shorts skill styles are available, but Deep Dive, Night File, and Tall Tale must be redesigned as genuine 2D before production.
- 3D models, geometry, renders, environments, and scenes are prohibited, even if described as stylized or flattened.
- Preserve the original style's mood and storytelling while replacing all 3D elements with 2D artwork and 2D motion.
- Follow `SHARED/SKILL_INTEGRATION.md` and document a 2D conversion plan for any 3D-origin style.
- Explicitly confirm 2D-only production before submission.

## Skill-first and uniqueness
- Inspect and use the installed Faceless Shorts skill for ideas, templates, formats, and production methods.
- Follow `SHARED/SKILL_INTEGRATION.md`.
- Coordinator reserves four distinct assignments before agents start. Compare topic, entities, angle, hook, story progression/payoff, dominant 2D visual style, and character. A different title alone is not enough.
- A shared JSON file is not an atomic lock. Use one coordinator as the sole assignment writer; until orchestration exists, assign sequentially.

## Voice separation
- Record the actual voice provider and preset for every video. Prefer four distinguishable voices. If an agent cannot verify a usable voice, mark its output blocked for review rather than silently duplicating a voice.

## Sources and rights
- Verify factual claims with reliable sources. Public description must have a clearly labelled Sources section listing source/publisher names only, without URLs. Keep research URLs privately in task metadata when practical.
- Do not fabricate citations or use unlicensed music, footage, characters, or copied scripts.

## Deliverables
Each agent submits: finished vertical 2D video, title, sectioned description with Sources, topic/angle/hook/story format/visual style, trend evidence and score, style-selection rationale, voice provider and preset, source names and private references, asset/licensing notes, and 2D confirmation.

## Publishing and queue
- Follow `TASKS/publishing_policy.json`.
- Normal daily maximum/target is four videos. At 18:00 Asia/Kolkata, if four validated videos are ready, schedule all four with the same publication timestamp.
- If fewer than four are ready at 18:00, wait until 00:00 Asia/Kolkata and then publish/schedule the validated available queue together.
- Extra finished videos remain in persistent storage and enter the next-day queue; never discard them.
- If backlog reaches 15 validated videos, trigger a backlog-release batch containing the entire validated backlog together, overriding the normal four-video cap. Keep the release as one coordinated batch and record every video result.
- Platform processing may cause actual public availability to differ by seconds; use one common scheduled timestamp and report actual timestamps. Do not promise exact same-second visibility.
- Agents never upload. Coordinator alone uploads/schedules, with idempotency keys and partial-failure reconciliation.

## Slash command control
- The command contract is in `COMMANDS.md`; it is authoritative for `/short` and `/unshort`.
- `/short` means start/resume the approved daily educational Shorts workflow and enable its configured schedule. It must not bypass validation, provider limits, or publishing safeguards.
- `/unshort` means globally pause the schedule and stop/cancel active or queued automation tasks where the connected runner supports it. Preserve completed videos and checkpoints; do not delete user work.
- Commands only take effect when received by a configured command dispatcher. A text command in an ordinary chat does not itself activate or stop external services.

## Comment
- After each successful upload, attempt the configured channel comment once per video: `𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞 𝐟𝐨𝐫 𝐦𝐨𝐫𝐞 𝐟𝐮𝐧 𝐟𝐚𝐜𝐭 𝐜𝐨𝐧𝐭𝐞𝐧𝐭 𝐚𝐧𝐝 𝐠𝐞𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐞𝐝!`
- YouTube comments do not support Markdown bold. Unicode bold-style characters are used to create a bold-looking effect. If comments are disabled or permission is missing, record a manual action; do not repeatedly retry or claim it succeeded.

## Temporary usage-limit recovery
- Follow `SHARED/USAGE_LIMIT_RECOVERY.md` and `TASKS/retry_policy.json`.
- Pause the affected agent, preserve its checkpoint and assignment, and resume the same work after reset/cooldown or through an approved fallback model. Keep the queue and publishing gate safe.
- Authentication, billing, suspension, policy, and unknown errors require manual intervention. Never bypass provider limits.

## Safety and quality
Avoid harmful, deceptive, age-inappropriate, or sensational misinformation. Respect YouTube policies and creator rights.
