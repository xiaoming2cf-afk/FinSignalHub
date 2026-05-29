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

## GitHub Status

- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8
- Current remediation baseline: `e336d4049e52b02a1b5e68a6c68cd8dc4373c53b`
- CI: PASS on the remediation baseline.
- Codex: CR-02-004 and CR-02-005 are fixed in this PR body refresh and Stage 02 path update. Gate 6 remains blocked until this remediation is pushed, CI passes, and Codex returns no major issues for the new head.

## Current Codex Findings

- CR-02-001: stale subagent GitHub/CI status; fixed in `a1f4d2fff7b980d21531d80f21038d337d46b7b3`.
- CR-02-002: stale checklist GitHub gate status; fixed in `e336d4049e52b02a1b5e68a6c68cd8dc4373c53b`.
- CR-02-003: missing mandatory provenance detail; fixed in `e336d4049e52b02a1b5e68a6c68cd8dc4373c53b`.
- CR-02-004: planned implementation paths used nonexistent `apps/api/app`; fixed by using the existing `apps/api/finsignalhub_api` package.
- CR-02-005: PR body status was stale; fixed by this file.

## Codex Review Request

`@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems`
