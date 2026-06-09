# Computer Use GPT Pro Review Runbook

## Preconditions

- Active stage review packet exists and is current.
- Live GitHub Gate 6 evidence is clean for the current PR head.
- A callable Computer Use tool is visible in the active Codex tool surface.
- User is not actively using the foreground browser, or the available Computer Use route is background-isolated.

## Submission Payload

Submit only:

- Project identity and forbidden directions.
- Active stage scope and non-scope.
- PR URL and current head.
- CI PASS links.
- Current-head Codex no-major or accepted finding status.
- Unresolved non-outdated review thread count.
- Local check summary.
- Explicit GPT Pro questions requesting PASS, CONDITIONAL PASS, or FAIL.

## Stop Conditions

Stop without input when the page shows:

- Login or account selection.
- MFA, captcha, or verification code.
- Permission, privacy, or consent prompt.
- Payment, subscription renewal, or billing prompt.
- Password, token, API key, or secret request.
- Page state that cannot be confidently identified.

## Evidence To Save

- `reviews/stage_XX/GPT_PRO_REVIEW_RESPONSE.md`
- `reviews/stage_XX/GPT_PRO_ACTION_ITEMS.md`
- `reviews/stage_XX/STAGE_ACCEPTANCE_RESULT.md`
- `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md` when GPT Pro authorizes next-stage work.
- Log updates in `CONTROL/04_EXECUTION_LOG.md`, `CONTROL/18_ARTIFACT_REGISTRY.md`, and `CONTROL/20_BLOCKER_LOG.md`.
