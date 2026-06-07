# provenance-agent

## Files touched

No direct subagent edits. Main integration created `apps/api/finsignalhub_api/extraction/provenance.py`.

## Summary

Added normalized-document provenance checks and candidate-to-document provenance matching. Required fields include source identity, source type, retrieval time, transformation notes, confidence, and tool-call lineage.

## Risks

Future stages must not weaken provenance when adding persistence, claim edges, or exports.

## Tests

Covered by document provenance and candidate provenance mismatch tests.

## Unresolved issues

None locally.

