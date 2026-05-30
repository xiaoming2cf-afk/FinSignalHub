# Mendel Remediation Audit

## Scope

Read-only audit of Stage 02 CR-02-020/021/022 local remediation.

## Files Touched

None. This was a read-only subagent audit.

## Files Inspected

- `apps/api/finsignalhub_api/routers/domain.py`
- `apps/api/finsignalhub_api/schemas/domain.py`
- `apps/api/finsignalhub_api/services/crud.py`
- `apps/api/tests/test_stage02_crud_routes.py`
- `apps/api/tests/test_stage02_schemas.py`
- `deployments/stage_02/GITHUB_PR.md`
- `reviews/stage_02/STAGE_ACCEPTANCE_RESULT.md`
- `reviews/stage_02/CODEX_REVIEW_SUMMARY.md`
- related dashboard, blocker, and checklist files

## Summary

Mendel confirmed the local remediation addresses the three current implementation-head Codex findings:

- CR-02-020: PASS. EvidenceItem PATCH now rejects updates that would leave both `quoted_evidence_span` and `no_quote_reason` empty.
- CR-02-021: PASS. ClaimEvidenceEdge creation now rejects cross-project claim/evidence links and validates optional tool-call project membership.
- CR-02-022: PASS. Deployment evidence no longer marks Stage 02 complete and keeps live CI/Codex/GPT Pro gates pending.

## Tests

Mendel ran:

```powershell
python -m pytest apps/api/tests/test_stage02_schemas.py apps/api/tests/test_stage02_crud_routes.py -p no:cacheprovider -q
```

Result: PASS, 10 tests at the time of the subagent audit.

## Risks

Mendel identified narrower-than-guard coverage for:

- clearing only `quoted_evidence_span` when no `no_quote_reason` exists;
- replacing a quote span with a no-quote rationale;
- rejecting a same-project claim/evidence edge when `tool_call_id` belongs to another project.

These gaps were addressed by adding regression tests before final local verification.

## Unresolved Issues

No product-scope risk found. Final Stage 02 remains blocked pending remediation push, live CI, current-head Codex no-major, and GPT Pro final review.
