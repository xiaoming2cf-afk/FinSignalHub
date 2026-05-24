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
- Stage 03: openalex-agent, crossref-agent, semantic-scholar-agent, arxiv-agent, connector-review-agent.
- Stage 04: extraction-schema-agent, llm-adapter-agent, provenance-agent, dedup-agent, test-agent.
- Stage 06: mcp-core-agent, mcp-schema-agent, mcp-tool-agent, mcp-test-agent, mcp-docs-agent.
- Stage 07: admin-ui-agent, api-client-agent, claim-graph-ui-agent, browser-test-agent.

Stage 00 will use a bounded verification subagent if available.
