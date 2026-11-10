# Faceless Shorts Automation

Coordinated workflow for **three 2D animated YouTube Shorts per daily batch**:
- Claude: one Short
- OpenCode: one Short
- Grok: one Short, subject to verifying that its connected tools and production capabilities support the assigned work

## Non-negotiable rules
- Every video must be **2D animation only**. Never 3D.
- One video per configured agent per batch.
- No duplicate or substantially overlapping topics, angles, hooks, story structures, or primary visual styles.
- All agents read SHARED rules and their AGENTS instructions before generation.
- Use the installed Faceless Shorts skill first for ideas, formats, styles, and production methods. Never claim to have inspected it unless accessible.
- All three voice-over voices should be distinguishable; record the actual provider and preset.
- Each video needs a YouTube title and a sectioned description with a Sources section. Public descriptions list source/publisher names only, with no URLs.
- Agents do not upload directly. The coordinator controls the batch gate.

## Workflow
1. Coordinator checks availability and reserves three distinct assignments before generation.
2. Agents generate one 2D Short each.
3. Coordinator collects files and metadata.
4. Validate completeness, 2D-only production, uniqueness, sources, rights, and voice separation.
5. Upload only if all three pass. If one fails, hold the entire batch.
6. Record YouTube IDs and upload results; retries must not create duplicates.

## Important capability note
The repository is an instruction and coordination scaffold; it does not itself make Claude, OpenCode, or Grok run on a schedule. Each agent's actual GitHub access, tools, rendering path, and voice capability must be tested. Do not claim a workflow is operational until its triggers and end-to-end output have been verified.

## Cost
Repository files and local scripts can be free. AI model usage, voice generation, rendering/storage, Zapier tasks, and integrations may have limits or costs. Do not add paid APIs or subscriptions without approval.

## Security
This repository is public. Never commit API keys, passwords, tokens, webhook URLs, private logs, or personal information. Keep secrets in environment variables or an ignored local .env file.
