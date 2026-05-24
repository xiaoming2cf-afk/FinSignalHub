---
name: browser-gpt-pro-reviewer
description: Route GPT Pro review through Chrome extension or safe browser workflow.
---

# Browser GPT Pro Reviewer

## When to use

Use when submitting `reviews/stage_XX/GPT_PRO_REVIEW_PACKET.md` to the specified GPT Pro page.

## Procedure

1. Read `CONTROL/10_COMPUTER_BROWSER_PROTOCOL.md` and `CONTROL/06_GPT_PRO_REVIEW_PROTOCOL.md`.
2. Read the review packet.
3. Prefer Chrome extension because the GPT Pro page requires login state.
4. Open the specified GPT Pro page only with user-approved browser action.
5. Paste the review request only if no password, captcha, payment, permission, privacy, secret, or unclear consent prompt appears.
6. Save the response to `reviews/stage_XX/GPT_PRO_REVIEW_RESPONSE.md`.
7. Extract action items to `reviews/stage_XX/GPT_PRO_ACTION_ITEMS.md`.
8. If passed, request next-stage instructions and write them to `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`.
9. Update execution, artifact, blocker, and acceptance logs.

## Required outputs

- GPT Pro response file or blocker entry.
- GPT Pro action items file when response exists.
- Next-stage instruction when GPT Pro passes.

## Failure conditions

- Credentials, verification codes, payment information, API keys, or secrets are entered.
- GPT Pro review is marked complete without a saved response.
