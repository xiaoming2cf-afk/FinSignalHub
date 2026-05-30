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

- `python -m pytest apps/api/tests`: PASS, 53 tests after CR-02-043 remediation.
- `python -m pytest apps/api/tests/test_stage02_crud_routes.py -q`: PASS, 39 targeted route tests after CR-02-043 remediation.
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
- CR-02-035 documentation remediation governance checks: PASS for `phase_check.py --stage 02`, strict token-pattern scan, artifact/checkpoint ID uniqueness, and `git diff --check` with only normal Windows line-ending warnings.
- CR-02-036 documentation remediation governance checks: PASS for `phase_check.py --stage 02`, strict token-pattern scan, artifact/checkpoint ID uniqueness, and `git diff --check` with only normal Windows line-ending warnings.
- CR-02-038 ToolCallLog artifact-scope remediation checks: PASS for targeted route tests, full API tests, API compile, phase_check, final scans, live CI/Codex, and GPT Pro delta review.
- CR-02-039/040 delete-conflict and acceptance-wording remediation checks: PASS for targeted route tests, full API tests, API compile, final scans, live CI, and follow-up Codex; follow-up Codex returned CR-02-041.
- CR-02-041 nullable dependent-delete remediation checks: PASS for targeted route tests, full API tests, API compile, final scans, live CI, and follow-up Codex; follow-up Codex returned CR-02-042.
- CR-02-042 compose database URL remediation checks: PASS for `docker compose config`, targeted route tests, full API tests, phase check, live CI, and follow-up Codex; follow-up Codex returned CR-02-043.
- CR-02-043 explicit-null PATCH remediation checks: PASS for targeted route tests, full API tests, API compile, `docker compose config`, phase check, final scans, live CI, Codex no-major, and GPT Pro delta/final review.

## GitHub Status

- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8
- Pre-implementation head: `8800022f55d79db951b57a61a1d1c7b3301cea9d`
- Pre-implementation CI: PASS
- Pre-implementation Codex: no major issues at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4576703382
- Implementation code commit: `fb8274aaaeedb3128d96c88473f49b0169186ee9`
- Implementation-head Codex findings: CR-02-020/021/022 returned on head `834c8f03982394a8c7c9a7229ae4b574db21a8ba`; CR-02-023 returned on head `d631c3fde13f063885da2ae8899235abb9c4cd0b`; CR-02-024/025 returned on head `9984b407acd2e5b75c57847545807cf083c9bc2a`; CR-02-026/027/028/029 returned on head `2b6f9c57b75ea3c4e0a2c460fbae4a6a38e4e487`; CR-02-030/031 returned on head `9c4e5d35556eb2115ccb333185f50a2889a02c33`; CR-02-032/033 returned on head `db89107a855588d534da1eb4d32c151c120ec442`; CR-02-034 returned on head `99b366655c0b2374952740d9ed329e9584a38564`; CR-02-035 returned on head `d41e8d0429c30f5fa4a6bb1cf8fc32c2a83dcd37`; CR-02-036 returned on head `0d46aa12cce60533cc0c6bb35d58af0c01b716b1`; CR-02-037 returned on final evidence head `b80ad20623531005eb6b966608cebb22d8332731`; CR-02-038 returned on CR-02-037 remediation head `e3e260178fb23408680f025bfc473c164cee473a`; CR-02-039/040 returned on CR-02-038 remediation head `dd58ef23571f3511eb844b131d861813f0aed14e`; CR-02-041 returned on CR-02-039/040 remediation head `52a99629b5f2cf136e39efc1e4d4b47858abfe47`; CR-02-042 returned on CR-02-041 remediation head `6bff2191781b02d6e2bb2459a3c1efae05bfedf2`; CR-02-043 returned on CR-02-042 remediation head `01d26414d09b53e0c280cbf4839727d283da8053`.
- Current implementation-reviewed status: runtime remediation head `eb4dd0f97ad04ce2173b5d677564d3254ad93313` passed live CI and Codex no-major after CR-02-043 remediation. GPT Pro final review returned PASS for the implementation-reviewed head, and GPT Pro delta/final review returned PASS for runtime remediation head `eb4dd0f97ad04ce2173b5d677564d3254ad93313`. The final docs/log evidence-sync head must pass fresh CI/Codex after push before merge.

Required review request after implementation push:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

## GPT Pro Status

- Stage 02 plan review: PASS.
- Final implementation review: PASS.
- CR-02-043 delta/final review: PASS for runtime remediation head `eb4dd0f97ad04ce2173b5d677564d3254ad93313`.
- Stage 03: authorized for planning only; implementation is not authorized.

## Acceptance

Stage 02 implementation is PASS / ACCEPTED for runtime remediation head `eb4dd0f97ad04ce2173b5d677564d3254ad93313`. Final evidence follow-up fixed CR-02-037 through CR-02-043; the runtime remediation rejects explicit `null` PATCH values for non-null database columns before persistence while still allowing truly nullable fields. The final docs/log evidence-sync head must pass fresh CI/Codex after push before merge. Stage 03 may proceed to `/plan` only after Stage 02 is merged. Stage 03 implementation is not authorized.
