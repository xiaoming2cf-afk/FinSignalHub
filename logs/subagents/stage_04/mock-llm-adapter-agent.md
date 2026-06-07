# mock-llm-adapter-agent

## Files touched

No direct subagent edits. Main integration created `apps/api/finsignalhub_api/extraction/mock_llm.py`.

## Summary

Implemented a deterministic mock model that returns fixture-backed candidates. It performs no environment lookup, provider construction, paid-service access, or network call.

## Risks

The filename is intentionally `mock_llm.py` to match the accepted GPT Pro goal boundary. Do not reintroduce `mock_llm_adapter.py`.

## Tests

Covered by deterministic output, socket-disabled execution, and AST import guard tests.

## Unresolved issues

None locally.

