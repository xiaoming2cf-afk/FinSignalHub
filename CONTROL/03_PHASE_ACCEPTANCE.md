# 03 Phase Acceptance

## Purpose

Defines the ten hard gates used to accept or block every stage.

## Owner

Phase acceptance lead.

## When to update

Update when gate definitions change, when a stage closes, or when GPT Pro adds a required acceptance condition.

## Required fields

- Stage id
- Gate name
- Required evidence
- Result: PASS, FAIL, or BLOCKED
- Reviewer
- Notes

## Example format

`Gate 6 GitHub | required: branch, PR, CI, @codex review, PR URL | result: BLOCKED | reason: gh unauthenticated`

## Current state

The ten gates are mandatory:

1. Scope: work stayed inside the approved stage.
2. Functionality: stage-specific deliverables exist and do not drift.
3. Tests: approved checks ran or blocker was recorded.
4. Docs: required docs and READMEs are complete.
5. Logs: execution, goal, artifact, decision, and blocker logs are current.
6. GitHub: branch, PR, CI, `@codex review`, PR URL, and Codex review summary exist.
7. GPT Pro: packet, response, action items, final result, and next-stage instruction exist.
8. Product governance: output aligns with Research Mode-first, MCP-first, evidence-stream value.
9. Security: no secrets, unsafe browser actions, or unreviewed permission steps.
10. Next stage: next-stage source is GPT Pro or a recorded blocker.

Gate 6 and Gate 7 are hard gates. Missing GitHub or GPT Pro evidence means FAIL or BLOCKED.
