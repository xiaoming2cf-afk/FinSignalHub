# project-boundary-validator-agent

## Role

Plan same-project validation for future Claim Graph and Research Delta operations.

## Files touched

None. This is a planning log only.

## Allowed future files

- `apps/api/finsignalhub_api/claim_graph/validators.py`
- future Stage 05 tests after implementation-goal approval

## Forbidden files

- Cross-project relation creation by default
- Global evidence pools without explicit project validation
- Destructive changes to Stage 02 project model

## Summary

Future Stage 05 implementation must require a `ResearchProject` boundary check before linking a claim and evidence candidate. Cross-project relations are forbidden by default because they risk evidence leakage and false research lineage.

## Risks

- Evidence from one project contaminates another project's claim graph.
- Delta compares snapshots from different projects.
- Tool-call lineage is not scoped by project.

## Tests

Future tests must accept same-project relation creation and reject cross-project claim/evidence or baseline/current snapshot comparisons.

## Unresolved issues

Implementation must decide whether validation belongs in service, schema, or both; this is deferred to the implementation goal.
