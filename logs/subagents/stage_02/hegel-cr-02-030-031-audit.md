# Hegel CR-02-030/031 Remediation Audit

## Purpose

Records Hegel's read-only audit of the Stage 02 local remediation for Codex findings CR-02-030 and CR-02-031.

## Scope

- Inspect `apps/api/finsignalhub_api/db/session.py` for SQLite foreign-key enforcement.
- Inspect `apps/api/finsignalhub_api/routers/domain.py` for project-existence and `source_artifact_refs` guards.
- Inspect Stage 02 tests covering orphan project-scoped creates, SQLite FK pragma, ClaimEvidenceEdge artifact refs, cross-project refs, and unknown refs.
- Do not modify files.

## Files Touched

None. Hegel was read-only.

## Summary

Hegel found no blocking issues in the inspected files.

CR-02-030 appears adequately addressed:

- SQLite FK enforcement is enabled through the connect listener in `apps/api/finsignalhub_api/db/session.py`.
- Project-scoped create hooks validate `project_id` existence in `apps/api/finsignalhub_api/routers/domain.py`.
- Source and ToolCallLog route registration now uses the project-existence hook.
- Tests cover SQLite pragma behavior and representative unknown-project create rejects.

CR-02-031 appears adequately addressed:

- `source_artifact_refs` now resolves known project-scoped artifacts.
- ClaimEvidenceEdge refs derive project scope from the linked claim and evidence item.
- Unknown refs and cross-project refs are rejected.
- Tests cover same-project edge refs, cross-project edge refs, and unknown refs.

## Risks

- Generated-artifact route tests are representative rather than exhaustive across every generated-artifact route and update path; the implementation relies on shared hook coverage.
- `source_artifact_refs` intentionally allow a broad set of Stage 02 project-scoped artifacts, including generated artifacts and `ToolCallLog`; keep this as documented Stage 02 provenance semantics and recheck in Stage 03+.

## Tests

Hegel did not run tests because the assignment was inspect-only. Mainline verification ran targeted and full local checks separately.

## Unresolved Issues

None blocking from Hegel's inspection. Gate 6 remains pending until this remediation is committed, pushed, receives CI PASS, and receives current-head Codex no-major evidence.
