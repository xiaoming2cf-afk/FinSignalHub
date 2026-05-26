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

Stage 02 planning head: `af35b2253524641701d0a00ca6ebf6cee02ef897`

CI status: PASS.

- https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26475050339/job/77958288414
- https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26475039759/job/77958248972

Codex status: PENDING/BLOCKED. The required `@codex review` was requested through the standard CLI comment, a minimal CLI retry, GitHub plugin comment, and PR review event route. No Codex response was visible at packet preparation time, so this packet does not claim Codex review passed.

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
- `python -m compileall apps/api/app`
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
