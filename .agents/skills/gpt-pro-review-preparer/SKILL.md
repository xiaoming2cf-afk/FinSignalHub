---
name: gpt-pro-review-preparer
description: Prepare copy-ready GPT Pro review packets for FinSignalHub stages.
---

# GPT Pro Review Preparer

## When to use

Use after local checks and before GPT Pro submission for every stage.

## Procedure

1. Read product definition, approved plan, goal registry, execution log, artifact registry, PR body, and acceptance checklist.
2. Write `reviews/stage_XX/GPT_PRO_REVIEW_PACKET.md`.
3. Include project identity, stage goal, plan, actual implementation, files changed, checks, GitHub PR status, Codex review summary, gate checklist, known limitations, blockers, and explicit questions.
4. Ask GPT Pro to answer PASS, CONDITIONAL PASS, or FAIL.
5. Ask GPT Pro for next-stage instructions only after pass or accepted conditional pass.

## Required outputs

- Copy-ready GPT Pro review packet.
- Packet registered in `CONTROL/18_ARTIFACT_REGISTRY.md`.

## Failure conditions

- Packet omits GitHub, Codex review, GPT Pro gate, blockers, or next-stage question.
- Packet describes business functionality not implemented in the current stage.
