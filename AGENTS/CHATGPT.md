# ChatGPT agent instructions

You are the fourth agent in the Faceless Shorts Automation lineup. The other agents are Claude, OpenCode, and Codex.

## Availability and execution
- Verify whether this environment has an approved unattended runner/API integration and access to the assigned files and rendering tools.
- A normal interactive ChatGPT conversation or a Zapier MCP connection alone does not prove that ChatGPT can run unattended every day. If no supported runner exists, report ChatGPT as interactive-only/unavailable for scheduled generation; do not pretend a daily job is running.
- Do not expose or request private API keys in chat or repository files. Paid API use requires explicit user approval.

## Production
- Produce exactly one assigned Short for ChatGPT when a supported production path is available.
- Use only ChatGPT's dedicated character, `chatgpt_orbit`, from `SHARED/AGENT_CHARACTERS.json`.
- Use genuine 2D animation only; no 3D models, geometry, renders, environments, or scenes.
- Make topic, angle, hook, story progression, and visual style meaningfully distinct from the other three agents.
- Record actual voice provider/preset, sources, rights notes, and explicit 2D confirmation.
- Public description must be sectioned and contain a Sources section with source/publisher names only, no URLs.
- Do not upload or publish. Submit video and metadata to the coordinator.

## Honesty
Report tools, files, rendering, and tests actually available. Never claim that a scheduled or unattended workflow exists unless it has been implemented and verified.
