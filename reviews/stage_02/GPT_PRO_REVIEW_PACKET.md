# GPT Pro Review Packet: Stage 02 Plan

Please review the FinSignalHub Stage 02 plan only. Do not review or request Stage 02 implementation in this packet.

## Project Identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. It supports AI Agent workflows for researchers, PhD students, labs, research teams, research-oriented product teams, and innovation project teams.

Core outputs are research delta, claim graph, evidence card, literature matrix, method card, dataset card, Repro Pack, and tool call log.

Forbidden directions remain chatbot, generic RAG, stock prediction, investment advice, ordinary report generator, standalone dashboard, model leaderboard, Risk Mode, and Replay Engine.

## Stage 01 Evidence

- Stage 01 PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7
- Stage 01 merge commit: `6b71850a1a59603fe169cd5a5ddf8d40adfaf8f4`
- Stage 01 accepted branch commit: `ce9bd7c008e1ec5c4b9a6cec9b1488883fe20742`
- Stage 01 tag: `stage-01-repo-scaffold`
- Stage 01 GPT Pro response: `reviews/stage_01/GPT_PRO_REVIEW_RESPONSE.md`
- Stage 01 result: PASS / accepted.
- Stage 02 status from GPT Pro: planning only; implementation not authorized.

## Stage 02 Plan

Plan path: `PLANS/STAGE_02_PLAN.md`

Stage 02 planning PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8

Stage 02 planning head: **not final in this file until live GitHub evidence is supplied at submission time**.

Latest verified pushed remediation baseline before this subagent/changelog refresh: `04b66822be98155a7112f42e7e084552b34b2154`.

CI status for that baseline: PASS.

- https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26640171982/job/78510781968
- https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26640175514/job/78510793998

Codex status: BLOCKED/PENDING. CR-02-001 is fixed in pushed head `a1f4d2fff7b980d21531d80f21038d337d46b7b3`; CR-02-002 and CR-02-003 were fixed in pushed head `e336d4049e52b02a1b5e68a6c68cd8dc4373c53b`; CR-02-004 and CR-02-005 were fixed in pushed head `d8693f99fbd5f41b8914184de366edb5a3e35352`; CR-02-006 was fixed in pushed head `30c9c9395ecc7593a6e2a1913cc39105f76c4bf0`; CR-02-007 was fixed in pushed head `ec43b6e576bf3e7ff2deb75df02ea76eccaf3931`; CR-02-008 was fixed in pushed head `fc5045e8702cfc66db71d5bf52701c818ab49d57`; CR-02-009 was fixed in pushed head `04b66822be98155a7112f42e7e084552b34b2154`. Codex then returned CR-02-010 for stale subagent summary state and CR-02-011 for internal remediation notes in `CHANGELOG.md`. This subagent/changelog refresh must be pushed, pass CI, and receive follow-up Codex no-major evidence before Gate 6 can pass.

Submission rule: before pasting this packet into GPT Pro, the operator must prepend the live PR #8 head commit, CI links, and Codex result from GitHub. The committed packet records historical evidence and must not be treated as a self-referential claim that the commit containing it already passed CI/Codex. If the live head does not have CI PASS and Codex no-major evidence, GPT Pro must treat the GitHub gate as BLOCKED and must not authorize Stage 02 implementation.

Important nuance:

- Codex returned no-major for the prior head `af35b2253524641701d0a00ca6ebf6cee02ef897`: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4548899623
- The current head then changed to `d8b6a274d6e5ab3f9b14a90f4266cadd00c343aa` to record PR/CI/Codex-attempt evidence.
- Current-head Codex requests were made through:
  - standard CLI comment: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4548936864
  - minimal CLI retry: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4548979169
  - GitHub plugin comment: comment id `4548999413`
  - PR review event route: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#pullrequestreview-4367584333
- Codex returned CR-02-001 P2 for that head: `reviews/stage_02/SUBAGENT_SUMMARY.md` still said GitHub PR and CI were pending even though PR #8 was open and CI had passed.
- CR-02-001 was fixed and pushed as `a1f4d2fff7b980d21531d80f21038d337d46b7b3`; CI passed.
- Codex then returned CR-02-002 P2 for stale checklist wording and CR-02-003 P1 for insufficient mandatory provenance detail in the plan:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#discussion_r3307129403
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#discussion_r3307129409
- CR-02-002 and CR-02-003 were fixed and pushed as `e336d4049e52b02a1b5e68a6c68cd8dc4373c53b`; CI passed.
- Codex then returned CR-02-004 P2 for using nonexistent `apps/api/app` paths instead of the existing `apps/api/finsignalhub_api` package, and CR-02-005 P2 for stale PR body status:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#discussion_r3324247315
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#discussion_r3324247318
- CR-02-004 and CR-02-005 were fixed and pushed as `d8693f99fbd5f41b8914184de366edb5a3e35352`; CI passed.
- Codex then returned CR-02-006 P2 because this packet still named an older head:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#discussion_r3324305755
- CR-02-006 was fixed and pushed as `30c9c9395ecc7593a6e2a1913cc39105f76c4bf0`; CI passed.
- Codex then returned CR-02-007 P2 because `CHECKLISTS/STAGE_02_CHECKLIST.md` still recorded older GitHub gate evidence:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#discussion_r3324406953
- The local fix updates the checklist Gate 6 row so reviewers use GitHub live PR head/CI/Codex evidence at submission time instead of a committed self-referential current-head value.
- CR-02-007 was fixed and pushed as `ec43b6e576bf3e7ff2deb75df02ea76eccaf3931`; CI passed.
- Codex then returned CR-02-008 P2 because `reviews/stage_02/SUBAGENT_SUMMARY.md` still described old subagent gate evidence:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#discussion_r3324516627
- The local fix updates the subagent summary to use the same GitHub live PR head/CI/Codex Gate 6 rule.
- CR-02-008 was fixed and pushed as `fc5045e8702cfc66db71d5bf52701c818ab49d57`; CI passed.
- Codex then returned CR-02-009 P2 because Stage 02 directories lacked purpose docs:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#discussion_r3324590704
- The local fix adds purpose docs under `reviews/stage_02/`, `deployments/stage_02/`, and `logs/subagents/stage_02/`.
- CR-02-009 was fixed and pushed as `04b66822be98155a7112f42e7e084552b34b2154`; CI passed.
- Codex then returned CR-02-010 and CR-02-011 P2:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#discussion_r3324664431
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#discussion_r3324664434
- The local fix refreshes `reviews/stage_02/SUBAGENT_SUMMARY.md` to the active CR-02-010/011 gate state and compresses `CHANGELOG.md` to user-visible Stage 02 governance changes only.
- This packet does not claim Codex review passed until this fix is pushed, CI passes, and Codex returns no major issues for the new head.

Stage 02 target: Research Mode Domain Models.

The Stage 02 plan proposes a later approved implementation for:

- Domain model schema.
- Database migration.
- Pydantic schemas.
- Basic CRUD services.
- Basic API routers.
- Tests.
- Docs.
- Logs.

Stage 02 implementation is not included in this branch unless you approve the plan and the user later approves the `/goal`.

## Proposed Model Scope

The plan covers:

- `ResearchProject`
- `Source`
- `Document`
- `EvidenceItem`
- `ResearchClaim`
- `ClaimEvidenceEdge`
- `ResearchDelta`
- `LiteratureMatrixRow`
- `MethodCard`
- `DatasetCard`
- `ReproPackExport`
- `ToolCallLog`

Model-level primitives may store fields needed later for evidence-stream workflows, but must not implement connectors, extraction, computation engines, MCP business tools, or UI behavior.

Mandatory provenance coverage in the Stage 02 implementation goal must include source identity, source type, retrieval time, quoted evidence span or explicit no-quote rationale, transformation notes, confidence, and tool-call lineage. These attributes must be modeled explicitly where applicable, not hidden behind an unvalidated generic blob.

## Forbidden Scope

Stage 02 must not implement:

- OpenAlex, Crossref, Semantic Scholar, arXiv, or user-upload ingestion connectors.
- External API calls.
- LLM adapters or extraction.
- Evidence extraction pipeline.
- Claim graph computation.
- Research delta computation beyond table/schema fields.
- Literature matrix generation logic.
- Repro Pack export logic.
- MCP business tools.
- ChatGPT App, Claude Connector, Copilot Connector, or Gemini Connector.
- Risk Mode or Replay Engine.
- Stock prediction, investment advice, chatbot UI, generic RAG, dashboard product behavior, auth, or billing.

## Planned Subagents

- `schema-agent`
- `migration-agent`
- `api-schema-agent`
- `test-agent`
- `docs-log-agent`

Each subagent has bounded file ownership and must write a log under `logs/subagents/stage_02/`.

## Planned Tests

Planning-only checks before implementation:

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02`: PASS locally.
- no Stage 02 implementation file check: PASS locally.
- secret scan: PASS locally.
- forbidden runtime/scope scan: PASS locally.
- `git diff --check`: PASS locally.

## Independent Verification

Read-only subagent Archimedes reviewed the Stage 02 plan scope. It initially found missing `phase_check.py` test category headings, which were fixed before this packet was submitted. The integrated verification log is `logs/subagents/stage_02/plan-scope-verifier.md`, and the summary is `reviews/stage_02/SUBAGENT_SUMMARY.md`.

Later implementation tests:

- `pytest apps/api/tests`
- `alembic upgrade head`
- `alembic downgrade -1` or documented blocker
- `alembic upgrade head`
- `python -m compileall apps/api/finsignalhub_api`
- Docker/Postgres migration check if required

## Review Questions

Please answer clearly:

1. PASS / CONDITIONAL PASS / FAIL for the Stage 02 plan.
2. Must-fix plan items before implementation may begin.
3. Deferrable plan items.
4. Whether Stage 02 implementation may begin after user `/goal` approval.
5. Required file boundaries for Stage 02 implementation.
6. Required tests and CI checks.
7. Required stop conditions.
8. Any product-alignment risks before implementation.
9. Whether the plan itself is acceptable while the Codex gate remains pending, and whether implementation must stay blocked until Codex returns a no-major response.

If PASS or accepted CONDITIONAL PASS, provide the exact Stage 02 `/goal` requirements. Do not authorize Stage 03.
