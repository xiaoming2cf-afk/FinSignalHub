# relation-rule-agent

## Role

Plan relation type, rationale, and provenance rules for future Claim Graph edges.

## Files touched

None. This is a planning log only.

## Allowed future files

- `apps/api/finsignalhub_api/claim_graph/relations.py`
- `apps/api/finsignalhub_api/claim_graph/schemas.py`

## Forbidden files

- Unbounded relation strings
- Generic summaries as relation rationale
- Financial prediction or investment advice relations
- Stage 06 MCP tool exposure during Stage 05 planning

## Summary

Future relations must be bounded and explainable: supports, contradicts, limits, uses_method, uses_dataset, background, uncertain, and supersedes. Every relation needs explicit rationale, evidence reference, source identity, quote or no-quote rationale, confidence, transformation notes, and tool-call lineage.

## Risks

- Optional rationale weakens claim auditability.
- Relation enums drift into prediction, risk scoring, or trading-signal language.
- Evidence provenance becomes generic metadata.

## Tests

Future tests must reject unknown relation types, blank rationale, missing evidence reference, and missing provenance.

## Unresolved issues

Exact enum names must be locked in the implementation goal before code is created.
