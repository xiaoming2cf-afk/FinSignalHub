# 21 Subagent Protocol

## Purpose

Defines bounded subagent usage for complex FinSignalHub stages.

## Owner

Subagent coordinator.

## When to update

Update when a stage enables subagents, subagent responsibilities change, or integration conflicts occur.

## Required fields

- Stage id
- Subagent name
- Responsibility
- Files allowed
- Files forbidden
- Output path
- Integration owner
- Conflict handling

## Example format

`schema-agent | Stage 02 | SQLAlchemy models | app/models only | migrations forbidden | logs/subagents/stage_02/schema-agent.md`

## Current state

Rules:

- Subagents must be declared in the plan before use unless the user explicitly requests them during execution.
- Subagents cannot modify the whole repository without file boundaries.
- Subagent outputs must be written to `logs/subagents/stage_XX/<agent_name>.md`.
- Output must include files touched, summary, risks, tests, and unresolved issues.
- Integration owner summarizes results in `reviews/stage_XX/SUBAGENT_SUMMARY.md`.

Recommended future subagents:

- Stage 02: schema-agent, migration-agent, api-schema-agent, test-agent, docs-agent.
- Stage 03: openalex-agent, crossref-agent, semantic-scholar-agent, arxiv-agent, user-upload-agent, connector-review-agent.
- Stage 04: extraction-schema-agent, llm-adapter-agent, provenance-agent, dedup-agent, test-agent, docs-agent.
- Stage 06: mcp-core-agent, mcp-schema-agent, mcp-tool-agent, mcp-test-agent, mcp-docs-agent.
- Stage 07: admin-ui-agent, api-client-agent, claim-graph-ui-agent, browser-test-agent.

Stage 03 central responsibility map:

- `openalex-agent`: fixture-only OpenAlex metadata mapping plan.
- `crossref-agent`: fixture-only Crossref metadata mapping plan.
- `semantic-scholar-agent`: fixture-only Semantic Scholar metadata mapping plan.
- `arxiv-agent`: fixture-only arXiv metadata mapping plan.
- `user-upload-agent`: uploaded-file metadata normalization plan only; no file parsing implementation, storage implementation, extraction behavior, or user-upload endpoint may be created in Stage 03 planning.
- `connector-review-agent`: provenance, no-network, no-business-implementation, and Stage 02 schema-compatibility review.

Stage 04 planning responsibility map:

- `extraction-schema-agent`: future extraction candidate schema and relation enum boundaries; no implementation files during planning.
- `llm-adapter-agent`: future deterministic mock LLM adapter contract; no provider calls, credentials, or live network behavior.
- `provenance-agent`: quote-span, no-quote rationale, source identity, retrieval time, transformation notes, confidence, and tool-call lineage requirements.
- `dedup-agent`: future duplicate evidence candidate handling plan only; no claim graph or Research Delta logic.
- `test-agent`: future mock-only extraction test plan; no Stage 04 test file or fixture directory during planning.
- `docs-agent`: method, dataset, limitation, provenance, and stop-condition documentation plan.

Stage 00 will use a bounded verification subagent if available.
