# test-plan-agent

## Role

Plan Stage 05 mock-only tests and governance checks.

## Files touched

None. This is a planning log only.

## Allowed future files

- `apps/api/tests/test_stage05_claim_graph.py`
- `apps/api/tests/test_stage05_research_delta.py`
- `apps/api/tests/fixtures/stage05_claim_graph/`

## Forbidden files

- Test files during planning
- Live API tests
- Real LLM calls
- Provider credentials

## Summary

Future tests must be deterministic and fixture-only. They should validate relation enums, rationale, provenance, same-project guards, neighborhood output, baseline/current deltas, changed-claim deltas, no-report wording, no external network behavior, and no forbidden product drift.

## Risks

- Tests depend on live provider state.
- Tests validate only happy paths and miss provenance gaps.
- Tests accidentally create Stage 06+ MCP behavior.

## Tests

Planning checks for this branch are `phase_check.py --stage 05`, forbidden path absence checks, secret scan, forbidden-scope scan, and `git diff --check`.

## Unresolved issues

Exact fixture schema is deferred to the implementation goal.
