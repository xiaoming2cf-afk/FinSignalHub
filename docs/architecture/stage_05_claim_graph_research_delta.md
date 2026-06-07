# Stage 05 Claim Graph and Research Delta Architecture

## Purpose

Define the future Claim Graph and Research Delta boundaries that will connect Stage 02 research objects and Stage 04 evidence candidates into provenance-preserving, project-scoped evidence-stream workflows.

## Claim Graph Boundary

The future Claim Graph layer will represent project-scoped research claims and evidence relations. It is not a general graph analytics engine, not a report generator, not a dashboard, and not a prediction system.

Future relation planning depends on:

- `ResearchProject` as the project boundary.
- `ResearchClaim` as the research judgment node.
- Stage 04 evidence candidates as the input evidence surface.
- Future `ClaimEvidenceEdge` records as explicit, rationale-bearing, provenance-bearing links.
- `ToolCallLog` lineage for replay and audit.

## Relation Rules

Future relation types must be bounded and explainable:

- `supports`
- `contradicts`
- `limits`
- `uses_method`
- `uses_dataset`
- `background`
- `uncertain`
- `supersedes`

Every relation must carry:

- relation type
- relation rationale
- evidence reference
- source identity
- source type
- retrieval time
- quoted span or no-quote rationale
- transformation notes
- confidence
- tool-call lineage
- same-project validation result

No edge may be created without evidence provenance and explicit rationale.

## Same-Project Guard

Future implementation must reject edges when a claim and evidence candidate do not belong to the same `ResearchProject`. Cross-project relations require a later explicit design and are forbidden by default.

## Research Delta Boundary

Research Delta compares two project-scoped evidence states: a baseline state and a current state. It must identify changes in claims, evidence, relations, rationale, confidence, and provenance completeness.

Research Delta is not:

- a prose report generator
- a financial prediction
- investment advice
- risk scoring
- a dashboard
- replay engine implementation

Future delta output must remain structured and evidence-linked, with baseline time, current time, changed entities, relation changes, rationale changes, and provenance references.

## Deferred Implementation Paths

These paths may be created only after GPT Pro approves a Stage 05 implementation goal:

- `apps/api/finsignalhub_api/claim_graph/`
- `apps/api/finsignalhub_api/research_delta/`
- `apps/api/tests/test_stage05_claim_graph.py`
- `apps/api/tests/test_stage05_research_delta.py`
- `apps/api/tests/fixtures/stage05_claim_graph/`

## Stop Conditions

Stop if future work requests MCP business tool exposure, UI/dashboard behavior, Repro Pack export, chatbot/RAG behavior, stock prediction, investment advice, Risk Mode, Replay Engine, external provider calls, real LLM calls, auth, billing, or destructive changes to Stage 02/03/04 behavior.
