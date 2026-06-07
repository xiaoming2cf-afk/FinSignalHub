# claim-graph-architecture-agent

## Role

Plan future Claim Graph architecture for FinSignalHub Stage 05.

## Files touched

None. This is a planning log only.

## Allowed future files

- `apps/api/finsignalhub_api/claim_graph/`
- `docs/architecture/stage_05_claim_graph_research_delta.md`

## Forbidden files

- Stage 02 migrations during planning
- Stage 03 connector runtime
- Stage 04 extraction runtime behavior
- MCP business tools
- Repro Pack export logic
- UI/dashboard behavior

## Summary

The future Claim Graph should connect project-scoped `ResearchClaim` nodes to provenance-bearing evidence references through explicit edge records. It must not become a generic graph analytics engine or a report generator. Future graph outputs should be structured neighborhoods and relation payloads that can support evidence cards, literature matrices, method cards, dataset cards, and research deltas.

## Risks

- Edge records treated as verified truth without rationale.
- Graph traversal drifting into dashboard analytics.
- Runtime created before GPT Pro implementation-goal approval.

## Tests

Future tests must cover same-project relation creation, cross-project rejection, relation payload shape, and absence of report-generation wording.

## Unresolved issues

Exact persistence model belongs to the future Stage 05 implementation goal and is not created during planning.
