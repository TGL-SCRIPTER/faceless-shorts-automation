# Faceless Shorts Automation

Coordinated workflow for **three 2D animated YouTube Shorts per daily batch**:
- Claude: one Short
- OpenCode: one Short
- Codex: one Short, only when installed and available

## Non-negotiable rules
- Every video must be **2D animation only**. Never 3D.
- One video per configured agent per batch.
- No duplicate or substantially overlapping topics, angles, hooks, story structures, or primary visual styles.
- All agents read SHARED rules and their AGENTS instructions before generation.
- Use the installed Faceless Shorts skill first for ideas, formats, styles, and production methods. Never claim to have inspected it unless accessible.
- Claude's voice-over voice must differ from OpenCode's. Prefer three distinct voices where available.
- Each video needs a YouTube title and a sectioned description with a Sources section. Public descriptions list source/publisher names only, with no URLs.
- Agents do not upload directly. The coordinator controls the batch gate.

## Workflow
1. Coordinator checks availability and reserves three distinct assignments before generation.
2. Agents generate one 2D Short each.
3. Coordinator collects files and metadata.
4. Validate completeness, 2D-only production, uniqueness, sources, rights, and voice separation.
5. Upload only if all three pass. If one fails, hold the entire batch.
6. Record YouTube IDs and upload results; retries must not create duplicates.

## Cost
Repository files and local scripts can be free. AI model usage, voice generation, rendering/storage, Zapier tasks, and integrations may have limits or costs. Do not add paid APIs or subscriptions without approval.

## Security
This repository is public. Never commit API keys, passwords, tokens, webhook URLs, private logs, or personal information. Keep secrets in environment variables or an ignored local .env file.
