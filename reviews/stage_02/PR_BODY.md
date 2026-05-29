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

PASS for Stage 02 plan review. Implementation still requires explicit user `/goal` approval.

## GitHub Status

- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8
- Last captured live evidence before this subagent/changelog refresh: `04b66822be98155a7112f42e7e084552b34b2154`
- CI: PASS on that pushed head.
- Codex: PASS/no-major on head `857696e19d46446658081ec2ed1236c791099730` before GPT Pro plan review. Final evidence commits still require CI/Codex follow-up before implementation starts.

## Current Codex Findings

- CR-02-001: stale subagent GitHub/CI status; fixed in `a1f4d2fff7b980d21531d80f21038d337d46b7b3`.
- CR-02-002: stale checklist GitHub gate status; fixed in `e336d4049e52b02a1b5e68a6c68cd8dc4373c53b`.
- CR-02-003: missing mandatory provenance detail; fixed in `e336d4049e52b02a1b5e68a6c68cd8dc4373c53b`.
- CR-02-004: planned implementation paths used nonexistent `apps/api/app`; fixed by using the existing `apps/api/finsignalhub_api` package.
- CR-02-005: PR body status was stale; fixed in `d8693f99fbd5f41b8914184de366edb5a3e35352`.
- CR-02-006: GPT Pro review packet used stale head/CI evidence; fixed in `30c9c9395ecc7593a6e2a1913cc39105f76c4bf0`.
- CR-02-007: Stage 02 checklist GitHub gate used stale head/finding evidence; fixed in `ec43b6e576bf3e7ff2deb75df02ea76eccaf3931`.
- CR-02-008: Stage 02 subagent summary used stale CR-02-001 gate evidence; fixed in `fc5045e8702cfc66db71d5bf52701c818ab49d57`.
- CR-02-009: Stage 02 directories lacked purpose docs; fixed in `04b66822be98155a7112f42e7e084552b34b2154`.
- CR-02-010: Stage 02 subagent summary still described older CR-02-008 state; fixed by this subagent summary refresh.
- CR-02-011: `CHANGELOG.md` contained internal CR-specific remediation notes; fixed by compressing it to user-visible Stage 02 governance changes only.

## Codex Review Request

`@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems`

## GPT Pro Plan Review

- Response: `reviews/stage_02/GPT_PRO_PLAN_REVIEW_RESPONSE.md`
- Action items: `reviews/stage_02/GPT_PRO_PLAN_ACTION_ITEMS.md`
- Result: PASS for Stage 02 plan; Stage 03 not authorized.
- Next implementation requirements: `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`
