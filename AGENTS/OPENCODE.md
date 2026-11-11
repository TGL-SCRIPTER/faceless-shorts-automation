# OpenCode agent instructions

1. Follow `AGENTS/CONTEXT_LOADING.md`. Read shared manifest files and only this agent's role file; never read other agents' role files. Refresh all four live files every batch and provide the context receipt.
2. Inspect the installed Faceless Shorts skill and use relevant ideas, templates, formats, styles, and production methods. Check other installed relevant skills if available.
3. Produce exactly one assigned Short; do not change the reserved assignment without coordinator approval.
4. Use only OpenCode's dedicated character, `opencode_spark`, from `SHARED/AGENT_CHARACTERS.json`. Do not use any other agent's character.
5. Finished video must be **genuine 2D animation only**. Convert Deep Dive, Night File, and Tall Tale into fully 2D artwork and motion before production. Follow `SHARED/SKILL_INTEGRATION.md`.
6. Do not use 3D models, geometry, renders, environments, or scenes.
7. Choose a voice-over preset different from the other agents where possible. Record exact provider and preset.
8. Make the hook, story, visual treatment, and character use meaningfully distinct.
9. Submit video, title, sectioned description with Sources, topic/angle/hook/story format/visual style, voice details, source references, rights notes, and 2D confirmation.
10. Do not upload. Return output to coordinator.

## Context rollover at 90%
- Treat 90% context-window usage as a session-maintenance threshold, not as a model quota or provider reset.
- Before reaching the limit, stop starting new production steps and write a durable checkpoint to the assigned task's checkpoint file or task metadata.
- The checkpoint must include assignment/batch ID, completed steps, current files and paths, decisions, next exact step, outstanding checks, and any tool state that cannot be recovered.
- Start a fresh OpenCode session only after the checkpoint is saved. Read the shared rules and checkpoint, verify the same assignment, then continue from the next incomplete step.
- Do not restart the video, discard completed work, change the topic, or treat a new session as a quota reset.
- If the installed OpenCode client cannot automatically start a new session or expose context percentage, report that limitation and ask the coordinator to start a fresh session; never pretend the rollover occurred.

## GLM-5.3-Flash usage limit and fallback
- If GLM-5.3-Flash reports a temporary usage/rate limit, stop calls to that model and checkpoint immediately.
- Check the approved fallback list in `TASKS/model_fallbacks.json`. Select a fallback only if its provider/model is actually available in this OpenCode environment, permitted by the user, suitable for the remaining task, and within its legitimate usage allowance.
- Prefer a free/locally available option. Never use a paid model, start a paid trial, add an API key, switch accounts, rotate credentials, or bypass a provider limit without explicit user approval.
- Record the original model, error evidence, fallback model/provider, availability check, and handoff point. Keep the same agent identity, character, assignment, and output requirements.
- If no suitable fallback is available, mark `waiting_for_reset`, preserve the checkpoint, and let the coordinator follow `TASKS/retry_policy.json`. Do not guess the provider's reset time.
- A context rollover does not cure a provider usage limit; a provider reset does not require discarding a context checkpoint.

## Capability honesty
Report inaccessible skills/resources honestly. A model fallback changes the underlying model only; it does not change OpenCode's assigned agent character or permit skipping validation.
