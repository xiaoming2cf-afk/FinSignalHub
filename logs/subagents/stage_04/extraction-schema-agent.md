# extraction-schema-agent

## Files touched

No direct subagent edits. Main integration created `apps/api/finsignalhub_api/extraction/schemas.py`.

## Summary

Defined the Stage 04 candidate schema lane around candidate-only payloads, quote/no-quote evidence, bounded confidence, provenance fields, tool-call lineage, and compatibility validation through `EvidenceItemCreate` without persistence.

## Risks

Do not convert candidates into persisted evidence records in Stage 04. Do not add database, route, or migration dependencies.

## Tests

Covered by `python -m pytest apps/api/tests/test_stage04_extraction.py`.

## Unresolved issues

External GitHub/Codex/GPT Pro gates remain pending after local implementation.

