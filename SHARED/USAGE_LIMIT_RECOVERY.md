# Usage-limit pause and automatic resume

This policy lets the coordinator pause an agent when its provider reports a temporary usage/rate limit, wait, and retry the **same assignment** after the expected reset. It is designed for Claude, OpenCode, and Codex.

## Important distinction

This file documents the required behavior and provides settings. **It does not, by itself, create a running scheduler or make provider quotas reset faster.** The GitHub Actions/coordinator workflow must be implemented and enabled before automatic resume actually runs. Each agent also needs a supported way to be invoked by that workflow.

## When an agent hits a limit

1. Stop making requests to that provider. Do not repeatedly hammer the endpoint.
2. Save the current work and last safe checkpoint.
3. Update that agent's entry in `TASKS/task_status.json`:
   - `status`: `waiting_for_reset`
   - `usage_recovery.state`: `waiting`
   - `usage_recovery.reason`: `temporary_usage_limit`
   - `usage_recovery.retry_after`: provider-supplied reset time in ISO-8601, if available; otherwise null
   - `usage_recovery.last_checkpoint`: short description of what is complete
   - `usage_recovery.retry_count`: increment the retry count
4. Keep the original batch ID, topic, angle, hook, and assignment unchanged.

## Coordinator behavior

- Prefer an explicit provider `Retry-After` or reset timestamp when available.
- If the provider gives no reset time, use the fallback cooldown in `TASKS/retry_policy.json`; then poll only at the configured interval with exponential backoff and jitter.
- When the wait expires, re-check that the failure was a temporary quota/rate limit and that credentials and required tools are still valid.
- Reinvoke the same agent on the same assignment from its last safe checkpoint.
- Do not mark the task complete until its deliverables and normal validation checks pass.
- Enforce the configured retry cap. After it is reached, mark the agent `manual_action_required` and notify the user.
- If one agent is waiting, keep the three-video batch and upload gate on hold. Never upload a partial batch.

## Cases that must not auto-retry

Authentication/session expiry, billing/payment requirements, account suspension, policy blocks, unknown errors, and persistent non-quota failures require manual intervention. Never bypass provider limits, rotate accounts/credentials, or create extra accounts.

## Provider-specific limitation

Claude, OpenCode, and Codex may expose different error messages and reset metadata. The workflow must classify each provider's response using verified integration behavior. If a reliable quota signal or invocation path is unavailable for an agent, mark that agent as requiring manual action instead of guessing.

## Configuration

See `TASKS/retry_policy.json` for cooldown, polling, backoff, retry cap, and safety settings. A future workflow should read that file rather than hard-code these values.
