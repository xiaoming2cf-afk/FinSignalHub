# 06 GPT Pro Review Protocol

## Purpose

Defines the blocking GPT Pro review process for each FinSignalHub stage.

## Owner

GPT Pro review preparer and phase acceptance lead.

## When to update

Update when GPT Pro target, packet fields, response format, or gate behavior changes.

## Required fields

- Stage id
- Review packet path
- Target URL
- Submission route
- Response path
- Action items path
- Final result
- Next-stage instruction path

## Example format

`Stage 00 | packet: reviews/stage_00/GPT_PRO_REVIEW_PACKET.md | result: BLOCKED | reason: login required`

## Current state

Target GPT Pro page:

`https://chatgpt.com/g/g-p-6a035355560081918d4a66ef7c70a14e-guo-chuang/c/6a128f5e-3a78-83ea-8a46-acc16e9578aa`

Protocol:

1. Generate `reviews/stage_XX/GPT_PRO_REVIEW_PACKET.md`.
2. Use Chrome extension first because the target page likely needs login state.
3. Do not enter passwords, verification codes, payment data, API keys, or secrets.
4. Stop on login, captcha, permission, payment, privacy, or unclear consent.
5. Save response to `reviews/stage_XX/GPT_PRO_REVIEW_RESPONSE.md`.
6. Save action items to `reviews/stage_XX/GPT_PRO_ACTION_ITEMS.md`.
7. Record PASS, CONDITIONAL PASS, FAIL, or BLOCKED in acceptance result.
8. If PASS or accepted conditional resolution, request next-stage instructions.
9. Save next-stage instruction in `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`.

Stage 00 GPT Pro status is PASS. The initial review, final Stage 00 confirmation, and post-acceptance capability confirmation are saved in:

- `reviews/stage_00/GPT_PRO_REVIEW_RESPONSE.md`
- `reviews/stage_00/GPT_PRO_ACTION_ITEMS.md`
- `reviews/stage_00/GPT_PRO_POST_ACCEPTANCE_RESPONSE.md`
- `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`

GPT Pro authorized Stage 01 planning only. Stage 01 implementation still requires an approved Stage 01 plan and formal goal.
