# Stage 04 Evidence Extraction Architecture Plan

## Purpose

Define the future evidence extraction skeleton that will turn normalized Stage 03 documents into provenance-preserving evidence candidates for later evidence cards, claim graph edges, literature matrices, method cards, dataset cards, research deltas, and Repro Packs.

## Extraction Candidate Boundary

Future extraction candidates should represent a candidate observation, method, dataset, limitation, background statement, or claim-supporting piece of evidence. They must not be claim graph edges yet and must not compute research deltas.

Each future candidate must preserve:

- source identity
- normalized document reference
- source type
- retrieval time
- publication time when available
- quote span when text is available
- no-quote rationale when exact quote text is not available
- relation label
- extraction confidence
- transformation notes
- tool-call lineage

## Relation Labels

The Stage 04 implementation goal should define a bounded enum for:

- `observation`
- `method`
- `dataset`
- `limitation`
- `background`
- `supports_claim_candidate`
- `contradicts_claim_candidate`
- `uncertain_relation`

These labels are extraction candidate labels only. They do not create `ClaimEvidenceEdge` records and do not compute claim graph state.

## Quote Span Validation

When source text is available, every extracted evidence candidate must include an exact quote span that can be checked against the normalized document text fixture. The future implementation should reject spans that cannot be matched.

When source text is unavailable, the candidate must carry a no-quote rationale that explains the source limitation, such as metadata-only input or unavailable full text. No-quote candidates must be lower-confidence and must not support a claim graph edge without later validation.

## Mock LLM Adapter Boundary

The future mock LLM adapter should be deterministic and fixture-driven. It must not call external LLM providers, require API keys, use paid services, or make live network calls in default tests.

## Worker Skeleton Boundary

The future extraction worker may orchestrate document input, mock adapter output, validation, and deterministic errors. It must not implement production queues, claim graph updates, Research Delta computation, MCP business tools, or UI behavior in Stage 04.

## Deferred Implementation Paths

These paths may be created only after GPT Pro accepts a separate Stage 04 implementation `/goal`:

- `apps/api/finsignalhub_api/extraction/`
- `apps/api/tests/test_stage04_extraction.py`
- `apps/api/tests/fixtures/stage04_extraction/`

## Forbidden Boundaries

Stage 04 planning and later skeleton work must not produce chatbot answers, ordinary summaries, reports, stock predictions, investment advice, dashboards, model rankings, Risk Mode, Replay Engine, claim graph computation, Research Delta computation, Repro Pack export, MCP business tools, auth, or billing.
