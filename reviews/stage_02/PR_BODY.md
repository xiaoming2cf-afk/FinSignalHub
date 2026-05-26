# Stage 02: Research Mode Domain Models Plan

## Goal

Create the Stage 02 plan for Research Mode domain models. This PR is planning-only until GPT Pro plan review and user `/goal` approval authorize implementation.

## Scope

The plan covers minimum domain model boundaries, migration plan, Pydantic schema plan, model-level CRUD/router plan, tests, docs, CI, GitHub review, GPT Pro plan review, risks, and stop conditions.

## Not Included

This PR does not implement domain model runtime code, migrations, CRUD routers, connectors, extraction, claim graph computation, research delta computation, Repro Pack export, MCP business tools, admin UI product features, Risk Mode, Replay Engine, stock prediction, investment advice, chatbot UI, generic RAG, or dashboard product behavior.

## Deliverables

- `PLANS/STAGE_02_PLAN.md`
- `TASKS/STAGE_02_TASKS.md`
- `CHECKLISTS/STAGE_02_CHECKLIST.md`
- `reviews/stage_02/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_02/STAGE_ACCEPTANCE_RESULT.md`
- `deployments/stage_02/GITHUB_PR.md`
- Stage control and RunLog updates

## Checks

Required planning checks:

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02`: PASS
- no Stage 02 implementation file check: PASS
- secret scan: PASS
- forbidden scope scan: PASS
- `git diff --check`: PASS

## Subagent Evidence

- Read-only plan verifier: `logs/subagents/stage_02/plan-scope-verifier.md`
- Summary: `reviews/stage_02/SUBAGENT_SUMMARY.md`

## GPT Pro Status

Pending plan review.

## Codex Review Request

`@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems`
