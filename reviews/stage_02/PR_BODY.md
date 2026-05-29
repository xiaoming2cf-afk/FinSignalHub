# Stage 02: Research Mode Domain Models

## Goal

Implement FinSignalHub Stage 02 Research Mode domain model primitives after GPT Pro plan PASS, PR #8 pre-implementation CI/Codex no-major evidence, and user direct-execution approval.

## Scope

Included:

- SQLAlchemy domain models for approved Research Mode entities.
- Alembic migration for the approved tables only.
- Pydantic schemas with provenance validation.
- Generic CRUD services and model-level API routes.
- Tests for metadata, provenance fields, schemas, CRUD routes, Alembic, and forbidden scope.
- Docs, logs, review artifacts, and acceptance evidence.

Explicitly not included:

- Connectors or external API calls.
- LLM adapters or evidence extraction.
- Claim graph computation.
- Research delta computation engines.
- Literature matrix generation.
- Repro Pack export logic.
- MCP business tools.
- ChatGPT/Claude/Copilot/Gemini connector implementation.
- Product UI behavior, dashboard behavior, chatbot UI, generic RAG, reports, stock prediction, investment advice, auth, billing, Risk Mode, or Replay Engine.

## Support-File Exception

Stage 02 modifies `pyproject.toml`, `.env.example`, `docker-compose.yml`, README files, and `CHANGELOG.md` only to support approved dependencies, placeholder-only database routing, PostgreSQL migration verification, and current-stage documentation. The exception is recorded in `CONTROL/05_DECISION_LOG.md` ADR-0002.

## Local Checks

Verified local evidence:

- `python -m pytest apps/api/tests`: PASS, 44 tests after CR-02-032/033 remediation.
- `python -m pytest apps/api/tests/test_stage02_crud_routes.py -q`: PASS, 30 targeted route tests after CR-02-032/033 remediation.
- `python -m pytest apps/api/tests/test_stage02_models.py -q`: PASS, 5 model tests after CR-02-030 remediation.
- `python -m pytest apps/mcp_server/tests`: PASS, 2 tests.
- `python -m compileall apps/api/finsignalhub_api`: PASS.
- `python -m compileall apps/mcp_server/finsignalhub_mcp_server`: PASS.
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02`: PASS.
- `npm.cmd run web:build`: PASS.
- `npm.cmd run web:audit`: PASS, 0 vulnerabilities.
- `docker compose config`: PASS.
- PostgreSQL Alembic upgrade/downgrade/upgrade: PASS.
- Full Docker Compose build/smoke for API/MCP/web: PASS.
- Likely-secret scan: PASS.
- Runtime forbidden-scope scan: PASS; only expected guard-test strings in `apps/api/tests/test_stage02_forbidden_scope.py`.
- Artifact ID uniqueness: PASS.
- `git diff --check`: PASS.

## GitHub Status

- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8
- Pre-implementation head: `8800022f55d79db951b57a61a1d1c7b3301cea9d`
- Pre-implementation CI: PASS
- Pre-implementation Codex: no major issues at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4576703382
- Implementation code commit: `fb8274aaaeedb3128d96c88473f49b0169186ee9`
- Implementation-head Codex findings: CR-02-020/021/022 returned on head `834c8f03982394a8c7c9a7229ae4b574db21a8ba`; CR-02-023 returned on head `d631c3fde13f063885da2ae8899235abb9c4cd0b`; CR-02-024/025 returned on head `9984b407acd2e5b75c57847545807cf083c9bc2a`; CR-02-026/027/028/029 returned on head `2b6f9c57b75ea3c4e0a2c460fbae4a6a38e4e487`.
- Current remediation status: CR-02-032/033 fixed locally after Codex review on head `db89107a855588d534da1eb4d32c151c120ec442`; local checks pass. The remediation still needs commit, push, live CI PASS, and current-head Codex no-major. GPT Pro final review is not submitted because the hard GitHub/Codex gate is incomplete and Chrome extension automation is blocked.

Required review request after implementation push:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

## GPT Pro Status

- Stage 02 plan review: PASS.
- Final implementation review: blocked until current-head Codex no-major exists and Chrome/GPT Pro submission route is controllable.
- Stage 03: not authorized.

## Acceptance

Stage 02 remains blocked until local checks, CI, Codex, GPT Pro final review, and next-stage instruction are all recorded.
