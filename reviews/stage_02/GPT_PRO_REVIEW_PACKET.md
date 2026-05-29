# GPT Pro Review Packet: Stage 02 Implementation

Please review the FinSignalHub Stage 02 implementation. This is an implementation review, not a request to begin Stage 03 unless Stage 02 passes.

## Project Identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. It supports AI Agent workflows for researchers, PhD students, labs, research teams, research-oriented product teams, and innovation project teams.

Core outputs are research delta, claim graph, evidence card, literature matrix, method card, dataset card, Repro Pack, and tool call log.

Forbidden directions remain chatbot, generic RAG, stock prediction, investment advice, ordinary report generator, standalone dashboard behavior, model leaderboard, Risk Mode, and Replay Engine.

## Prior Gate Evidence

- Stage 01 final implementation: PASS, PR #7 merged.
- Stage 02 plan review: PASS, response saved in `reviews/stage_02/GPT_PRO_PLAN_REVIEW_RESPONSE.md`.
- Stage 02 plan action items: saved in `reviews/stage_02/GPT_PRO_PLAN_ACTION_ITEMS.md`.
- PR #8 pre-implementation head: `8800022f55d79db951b57a61a1d1c7b3301cea9d`.
- Pre-implementation CI: PASS.
- Pre-implementation Codex: no major issues at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4576703382.
- User approval: direct execution approved in the Codex conversation; no repeated confirmation required.

## Stage 02 Goal

Implement Research Mode domain model primitives only:

- SQLAlchemy models for approved entities.
- Alembic migration.
- Pydantic schemas with provenance validation.
- Generic CRUD services.
- Model-level API routers.
- Tests.
- Docs, logs, PR body, acceptance evidence, and this review packet.

## Implemented Model Scope

Approved entities:

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

## Provenance Requirements Covered

The implementation is intended to model and validate:

- source identity;
- source type;
- retrieval or ingestion time;
- publication or release time where applicable;
- URL, DOI, or locator fields where applicable;
- quoted evidence span or explicit no-quote rationale;
- transformation notes;
- confidence;
- tool-call lineage;
- validation status;
- source artifact references for generated artifacts.

## Support-File Exception

Stage 02 changed `pyproject.toml`, `.env.example`, `docker-compose.yml`, README files, and `CHANGELOG.md` only to support approved dependencies, placeholder-only database routing, migration verification, and current-stage documentation.

This exception is recorded in `CONTROL/05_DECISION_LOG.md` ADR-0002. It must be reviewed as a bounded exception. It does not authorize connectors, extraction, MCP business tools, UI product behavior, auth, billing, or Stage 03+ work.

## Forbidden Scope Check

The implementation must not include:

- OpenAlex, Crossref, Semantic Scholar, arXiv, or user-upload ingestion connectors.
- External API calls.
- LLM adapters or extraction.
- Evidence extraction pipelines.
- Dedup pipelines.
- Claim graph computation.
- Research delta computation beyond table/schema fields.
- Literature matrix generation.
- Repro Pack export logic.
- MCP business tools.
- ChatGPT App, Claude Connector, Copilot Connector, or Gemini Connector implementation.
- Risk Mode or Replay Engine.
- Stock prediction, investment advice, chatbot UI, generic RAG, dashboard product behavior, auth, or billing.

## Local Check Evidence

Current locally verified:

- `python -m pytest apps/api/tests`: PASS, 42 tests after CR-02-030/031 remediation.
- `python -m pytest apps/api/tests/test_stage02_crud_routes.py -q`: PASS, 28 targeted route tests after CR-02-030/031 remediation.
- `python -m pytest apps/api/tests/test_stage02_models.py -q`: PASS, 5 model tests after CR-02-030 remediation.
- `python -m pytest apps/mcp_server/tests`: PASS, 2 tests.
- `python -m compileall apps/api/finsignalhub_api`: PASS.
- `python -m compileall apps/mcp_server/finsignalhub_mcp_server`: PASS.
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02`: PASS.
- `npm.cmd run web:build`: PASS.
- `npm.cmd run web:audit`: PASS, 0 vulnerabilities.
- `docker compose config`: PASS.
- PostgreSQL Alembic `upgrade head`, `downgrade -1`, `upgrade head`: PASS.
- Full `docker compose up --build -d` plus API/MCP/web smoke: PASS.
- Likely-secret scan: PASS.
- Runtime forbidden-scope scan: PASS; only expected guard-test strings in `apps/api/tests/test_stage02_forbidden_scope.py`.
- Artifact ID uniqueness: PASS.
- `git diff --check`: PASS.

Before final acceptance, Codex must prepend the latest implementation commit, CI links, Codex review URL/result, and any additional local verification results. If the implementation head does not have CI PASS and Codex no-major evidence, treat the GitHub gate as BLOCKED.

Implementation code commit pushed before this evidence sync:

- `fb8274aaaeedb3128d96c88473f49b0169186ee9`

Implementation-head Codex review returned CR-02-020/021/022 on head `834c8f03982394a8c7c9a7229ae4b574db21a8ba`, CR-02-023 on head `d631c3fde13f063885da2ae8899235abb9c4cd0b`, CR-02-024/025 on head `9984b407acd2e5b75c57847545807cf083c9bc2a`, CR-02-026/027/028/029 on head `2b6f9c57b75ea3c4e0a2c460fbae4a6a38e4e487`, and CR-02-030/031 on head `9c4e5d35556eb2115ccb333185f50a2889a02c33`. The remediation adds evidence quote-provenance update guards, project-boundary guards for EvidenceItem, ResearchClaim, Document, ClaimEvidenceEdge, generated artifact creation/update paths, source-artifact refs, SQLite FK enforcement, orphan project-scoped create rejection, tool-call lineage, and deployment evidence sync.

Current live PR head:

- `9c4e5d35556eb2115ccb333185f50a2889a02c33`
- CI PASS:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26654056821/job/78559544170
  - https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26654058385/job/78559547100
- Current-head Codex review requests:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4578394872
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4578418494
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#pullrequestreview-4391863335
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4578477038
- Delayed current-head Codex result: CR-02-030/031 returned at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#pullrequestreview-4391903098.
- Current local remediation status: fixed locally and Hegel read-only audit found no blocking issue; pending commit, push, CI, and current-head Codex follow-up.
- Browser/GPT Pro route status: BLOCKED. Chrome extension calls returned `native pipe is closed` after one retry; Chrome is running, extension is installed/enabled, native host manifest is correct, and the recovery-window attempt still failed.

The live PR #8 head, CI links, and Codex result must still be verified from GitHub immediately before this packet is submitted to GPT Pro.

## Review Files

- Plan: `PLANS/STAGE_02_PLAN.md`
- Tasks: `TASKS/STAGE_02_TASKS.md`
- Checklist: `CHECKLISTS/STAGE_02_CHECKLIST.md`
- Architecture doc: `docs/architecture/stage_02_domain_models.md`
- Commands/evidence doc: `docs/codex/stage_02_commands.md`
- Acceptance result: `reviews/stage_02/STAGE_ACCEPTANCE_RESULT.md`
- PR body: `reviews/stage_02/PR_BODY.md`
- Deployment evidence: `deployments/stage_02/GITHUB_PR.md`
- Codex review summary: `reviews/stage_02/CODEX_REVIEW_SUMMARY.md`
- Subagent summary: `reviews/stage_02/SUBAGENT_SUMMARY.md`
- Current stage state: `CONTROL/24_CURRENT_STAGE_STATE.md`
- Goal registry: `CONTROL/07_CODEX_GOAL_REGISTRY.md`
- Blocker log: `CONTROL/20_BLOCKER_LOG.md`

## Questions For GPT Pro

Please answer clearly:

1. PASS / CONDITIONAL PASS / FAIL for Stage 02 implementation.
2. Must-fix implementation items before Stage 02 may pass.
3. Deferrable items, if any.
4. Whether the support-file exception in ADR-0002 is acceptable.
5. Whether provenance modeling and validation are sufficient for Stage 02.
6. Whether any forbidden Stage 03+ behavior slipped in.
7. Whether local/GitHub/Codex evidence is sufficient.
8. Whether Stage 02 can be accepted after any critical fixes.
9. If Stage 02 passes, provide exact Stage 03 plan requirements, file boundaries, tests, risks, and stop conditions.

Do not authorize Stage 03 unless Stage 02 implementation passes or receives an accepted conditional pass with critical items resolved.
