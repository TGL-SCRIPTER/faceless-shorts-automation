# Usage-limit recovery and context rollover

This policy separates context-window management from provider quota/rate-limit recovery. They are different events and must never be confused.

## OpenCode context at 90%
1. Treat 90% context use as a checkpoint threshold, not a provider quota error.
2. Save batch ID, assignment, completed steps, current files/paths, decisions, next exact step, validation still needed, and any non-persistent tool state.
3. Stop starting new work; start a fresh OpenCode session only after the checkpoint is durable.
4. Read the checkpoint and shared instructions in the new session, verify the same assignment, and continue from the next incomplete step.
5. If the OpenCode client does not expose context percentage or cannot automatically create a fresh session, report the limitation for coordinator/manual action. Do not claim an automatic rollover occurred.

## Provider quota/rate limit
When any provider reports a temporary usage/rate limit:
1. Stop requests to that provider. Do not hammer the endpoint.
2. Save the current work and checkpoint.
3. Mark the affected agent `waiting_for_reset`, record error evidence, retry count, and provider-supplied reset/Retry-After timestamp if present.
4. Preserve batch ID, topic, angle, hook, character, assignment, and progress.

## OpenCode GLM-5.3-Flash fallback
- If GLM-5.3-Flash is temporarily unavailable due to a usage limit, check `TASKS/model_fallbacks.json`.
- Use another model only when it is actually configured and available in the user's OpenCode environment, suitable for the remaining work, and within its legitimate allowance.
- Prefer free/local models. Paid models, paid trials, new API keys, account changes, and additional subscriptions require explicit user approval.
- Record fallback provider/model and why it was selected. The OpenCode agent and its fixed character do not change.
- If no fallback qualifies, wait for the provider reset. Do not guess when GLM's quota resets.

## Coordinator retry
- Prefer provider Retry-After/reset metadata. If none exists, use fallback cooldown in `TASKS/retry_policy.json`, then poll with configured backoff and jitter.
- Re-check that the error is a temporary quota/rate limit and credentials/tools remain valid before resuming.
- Resume the same assignment from the last safe checkpoint. Enforce retry cap.
- Authentication/session expiry, billing, suspension, policy blocks, unknown errors, and persistent non-quota failures require manual intervention.
- A quota reset does not require discarding the context checkpoint; a new context session does not reset a provider quota.

## Operational limitation
These instructions and JSON settings are policy only. Automatic resume and automatic context rollover require a working coordinator scheduler and a supported OpenCode invocation/session-control integration. Until tested end-to-end, manual intervention may be required. Never claim automation is live merely because configuration exists.
