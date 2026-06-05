# worker-skeleton-agent

## Files touched

No direct subagent edits. Main integration created `apps/api/finsignalhub_api/extraction/worker.py`.

## Summary

Implemented a mock-only worker that accepts `ExtractionRequest` with a Stage 03 normalized `DocumentCreate`, optional Stage 04-owned text, and tool-call lineage. The worker validates provenance, quote spans, candidate-only output, and EvidenceItem-compatible payload shape without persistence.

## Risks

Do not call raw provider fixtures or Stage 03 connector internals from the worker.

## Tests

Covered by worker fixture tests for quote-backed and metadata-only inputs.

## Unresolved issues

None locally.

