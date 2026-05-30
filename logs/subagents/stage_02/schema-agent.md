# schema-agent

## Files Touched

Read-only subagent; parent integrated findings into:

- `apps/api/finsignalhub_api/models/domain.py`
- `apps/api/finsignalhub_api/models/enums.py`
- `apps/api/finsignalhub_api/db/base.py`

## Summary

The schema audit confirmed the approved Stage 02 models align with FinSignalHub's Research Mode evidence-stream outputs. It recommended explicit provenance fields, structured quote spans, controlled status/relation values, `back_populates` relationships, `ToolCallLog` lineage, and no Stage 03+ behavior.

## Risks

- Generic provenance blobs would weaken later evidence cards and claim edges.
- Tool lineage must remain safe and must not store secrets.
- ResearchDelta and ReproPackExport are stored artifacts only in Stage 02.

## Tests

Covered by `apps/api/tests/test_stage02_models.py` and `apps/api/tests/test_stage02_schemas.py`.

## Unresolved Issues

None known after integration.
