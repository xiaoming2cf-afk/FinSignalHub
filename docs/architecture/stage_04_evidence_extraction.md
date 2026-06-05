# Stage 04 Evidence Extraction Architecture

## Purpose

Define the mock-only Stage 04 skeleton that turns normalized Stage 03 `DocumentCreate` payloads into provenance-preserving `EvidenceCandidate` payloads for later evidence cards, literature matrices, method cards, dataset cards, research deltas, claim graph work, and Repro Packs.

## Candidate Boundary

Stage 04 candidates represent a candidate observation, method, dataset, limitation, background statement, or claim-supporting evidence item candidate. They are not persisted `EvidenceItem` records, not `ClaimEvidenceEdge` records, and not research-delta outputs.

Each candidate preserves:

- source identity
- normalized document reference
- source type
- retrieval time
- publication time when available
- quote span when text is available
- no-quote rationale when exact quote text is not available
- relation label
- candidate confidence
- transformation notes
- tool-call lineage

## Relation Labels

The Stage 04 runtime defines a bounded enum for:

- `observation`
- `method`
- `dataset`
- `limitation`
- `background`
- `supports_claim_candidate`
- `contradicts_claim_candidate`
- `uncertain_relation`

These labels are candidate labels only. They do not create `ClaimEvidenceEdge` records and do not compute claim graph state.

## Quote Span Validation

When source text is available, every candidate includes an exact quote span that can be checked against the normalized document text fixture. Stage 04 rejects spans that cannot be matched.

When source text is unavailable, the candidate carries a no-quote rationale that explains the source limitation, such as metadata-only input or unavailable full text. No-quote candidates are lower confidence and cannot support later graph work without validation.

## Mock Model Boundary

The Stage 04 mock model is deterministic and fixture-driven. It does not call external model providers, require API keys, use paid services, or make live network calls in default tests.

## Worker Skeleton Boundary

The worker orchestrates normalized document input, mock model output, quote validation, provenance validation, and deterministic errors. It does not implement production queues, claim graph updates, Research Delta computation, MCP business tools, or UI behavior in Stage 04.

## Implemented Paths

GPT Pro accepted the Stage 04 implementation goal before these paths were created:

- `apps/api/finsignalhub_api/extraction/`
- `apps/api/tests/test_stage04_extraction.py`
- `apps/api/tests/fixtures/stage04_extraction/`

## Forbidden Boundaries

Stage 04 planning and later skeleton work must not produce chatbot answers, ordinary summaries, reports, stock predictions, investment advice, dashboards, model rankings, Risk Mode, Replay Engine, claim graph computation, Research Delta computation, Repro Pack export, MCP business tools, auth, or billing.
