# research-delta-agent

## Role

Plan Research Delta semantics for comparing baseline and current evidence states.

## Files touched

None. This is a planning log only.

## Allowed future files

- `apps/api/finsignalhub_api/research_delta/`
- `apps/api/finsignalhub_api/research_delta/schemas.py`
- `apps/api/finsignalhub_api/research_delta/service.py`
- `apps/api/finsignalhub_api/research_delta/rules.py`

## Forbidden files

- Report generator logic
- Risk scoring
- Stock prediction
- Investment advice
- Replay Engine implementation

## Summary

Research Delta should compare a project-scoped baseline state and current state. Future outputs should identify added, removed, changed, contradicted, or superseded claim/evidence relations while preserving relation rationale, source provenance, and tool-call lineage.

## Risks

- Delta output becomes prose report generation.
- Delta confidence is misread as a financial forecast.
- Baseline/current timestamps are missing or ambiguous.

## Tests

Future tests must cover baseline/current time validation, changed-claims delta, relation-state changes, no-report wording, and deterministic mock fixture behavior.

## Unresolved issues

Delta payload names and exact state transition enum belong to the future implementation goal.
