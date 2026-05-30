# Volta CR-02-038 Read-Only Audit

## Purpose

Record the bounded subagent verification for Codex finding CR-02-038 on Stage 02 PR #8.

## Scope

- Stage: 02 Research Mode domain models.
- Finding: `ToolCallLog.input_artifact_ids` and `ToolCallLog.output_artifact_ids` lacked project-scoped artifact validation.
- Mode: read-only subagent audit.
- Product boundary: Research Mode-first, MCP-first, evidence-stream provenance only; no connector, extraction, MCP business tool, UI behavior, chatbot, RAG, stock prediction, investment advice, dashboard, or report work.

## Files Inspected

- `apps/api/finsignalhub_api/routers/domain.py`
- `apps/api/finsignalhub_api/schemas/domain.py`
- `apps/api/tests/test_stage02_crud_routes.py`
- `CONTROL/03_PHASE_ACCEPTANCE.md`

## Files Touched

None by the subagent.

## Summary

Volta confirmed CR-02-038 is valid. The route registration for `tool-call-logs` only validated that `project_id` exists and did not validate `input_artifact_ids` or `output_artifact_ids` against the owning project on create or update. Because Stage 02 evidence lineage later trusts the ToolCallLog project boundary, accepting cross-project artifact ids would contaminate replay lineage.

The main thread implemented the remediation locally by adding a ToolCallLog artifact-id project-scope guard in `apps/api/finsignalhub_api/routers/domain.py`, registering it on create and update, and adding regression tests in `apps/api/tests/test_stage02_crud_routes.py`.

## Risks

- Cross-project ToolCallLog artifact refs would weaken evidence-stream provenance and replay lineage.
- Output artifact ids should reference already-created artifacts; omitted output ids remain the supported create-time path when outputs do not exist yet.
- ToolCallLog ids remain valid project-scoped artifact refs because the existing Stage 02 artifact lookup intentionally includes `ToolCallLog`.

## Tests

- `python -m pytest apps/api/tests/test_stage02_crud_routes.py -q`
- `python -m pytest apps/api/tests -q`
- `python -m compileall apps/api/finsignalhub_api`
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02`

## Unresolved Issues

- Push, live CI, and follow-up Codex no-major evidence are still required before PR #8 can merge.
