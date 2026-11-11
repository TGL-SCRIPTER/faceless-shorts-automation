# Faceless Shorts Automation

Coordinated workflow targeting **four original 2D animated YouTube Shorts per daily batch**:
- Claude: one Short
- OpenCode: one Short
- Codex: one Short, subject to verified access/capabilities
- ChatGPT: one Short, subject to verified interactive/API runner capability

## Non-negotiable rules
- Genuine 2D animation only; never 3D.
- One assigned video per available agent per batch.
- Each agent uses only its own fixed original character from `SHARED/AGENT_CHARACTERS.json`.
- No substantially overlapping topics, angles, hooks, story structures, or dominant visual styles.
- All agents read shared rules and role instructions before generation.
- Use the installed Faceless Shorts skill first when accessible.
- Prefer distinguishable voices and record actual provider/preset.
- Public description is sectioned and its Sources section lists source/publisher names only, without URLs.
- Agents do not upload. The coordinator alone validates and publishes.

## Publishing schedule (Asia/Kolkata)
- Normal target/cap: four Shorts per day.
- At 18:00, if four validated videos are queued, schedule all four for one common publication timestamp.
- If fewer than four are ready at 18:00, wait until 00:00, then publish/schedule the validated available queue together.
- Keep extra validated videos in persistent storage for the next day.
- If backlog reaches 15, release the entire validated backlog together as one coordinated batch; this is an explicit override of the normal four-video cap.
- The YouTube platform may not make every video publicly visible at the exact same second, even when the same timestamp is scheduled.

## Notifications
Structured alerts are defined for agent limits/expiry, missing outputs, failures, manual actions, queue status, and publishing outcomes. WhatsApp delivery is optional and not configured until an approved WhatsApp Business, Twilio, or Zapier integration is connected. Do not put phone numbers, tokens, or webhook secrets in this public repository.

## Important capability note
This repository is a configuration/instruction scaffold, not yet a live scheduler. Agent invocations, durable shared storage, scheduled YouTube uploads, comments, WhatsApp notifications, and automatic resume must each be implemented and tested with supported integrations before they can be considered operational.

## Cost and security
Use existing/free tools where possible. No paid API, subscription, model, or trial without explicit approval. Never commit API keys, passwords, tokens, webhook URLs, private logs, or personal information. Keep secrets in a secure credential store or ignored local environment file.
