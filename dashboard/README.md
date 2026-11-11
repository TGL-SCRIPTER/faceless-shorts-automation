# Shorts Command Center

A static Cloudflare Pages dashboard with a Pages Function that reads the public workflow JSON files from this repository. It does not contain credentials and does not invoke agents or publish videos.

## Cloudflare Pages deployment (free tier)

Create a Pages project connected to this GitHub repository:
- Framework preset: None
- Root directory: `dashboard`
- Build command: leave blank
- Build output directory: `/` (or `.`, as accepted by the dashboard)
- Production branch: `main`

Cloudflare Pages supports Git-connected automatic deployments. The free Workers plan currently documents 100,000 requests/day; plan limits can change.

## Make it private BEFORE sharing or using the URL

A GitHub repository may be public, and Pages sites are public by default. Enable Cloudflare Access for the Pages hostname and create an allow policy for only the account email you control. Test in a signed-out/private browser: access must be denied. Do not rely on a hidden URL or a client-side password.

Cloudflare Access setup is an account-owner action and cannot be safely completed by repository code. Do not deploy/share the site until Access protection is enabled and tested.

## Current capabilities

- Reads live automation control, daily assignment, task status and publishing policy JSON from GitHub.
- Shows truthful configuration state and agent/task statuses.
- Responsive PC/mobile interface.

## Not implemented (controls remain disabled)

- Agent process startup/session triggers or orchestration.
- Assignment creation/dispatch and durable task writes.
- Video file storage/preview.
- Video validation pipeline.
- YouTube scheduling/upload/comment actions.
- Notifications and unattended retries.

The existing repository is a policy/configuration scaffold. This dashboard deliberately does not pretend those systems are running. No GitHub token, YouTube token, or other secret belongs in browser code or this repository.
