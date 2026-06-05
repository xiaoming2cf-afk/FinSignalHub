# quote-span-agent

## Files touched

No direct subagent edits. Main integration created `apps/api/finsignalhub_api/extraction/quote_span.py` and quote-span schema validation in `schemas.py`.

## Summary

Implemented exact quote-span validation for fixture document text and deterministic mismatch errors. Metadata-only candidates must use no-quote rationale instead of a fabricated span.

## Risks

Future real text parsing must preserve exact offsets and source text identity before these candidates can support later graph work.

## Tests

Covered by exact-span and mismatch tests in `apps/api/tests/test_stage04_extraction.py`.

## Unresolved issues

None locally.

