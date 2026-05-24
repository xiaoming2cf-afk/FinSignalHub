# Stage 04 Tasks: Evidence Extraction

## Stage goal

Create extraction schemas, mock LLM adapter, provenance validation, quote span validation, and relation classification.

## User needs

Researchers need evidence cards that preserve traceability from source text to claims.

## Files allowed

To be defined in Stage 04 plan around extraction schema, adapters, validators, relation labels, mocks, tests, and docs.

## Files forbidden

MCP public tools, admin UI, investment conclusions, and report generation.

## Skills required

`evidence-graph-architect`, `codex-log-keeper`, `phase-gate-auditor`.

## Subagents required

Recommended: extraction-schema-agent, llm-adapter-agent, provenance-agent, dedup-agent, test-agent.

## Implementation tasks

To be filled after GPT Pro Stage 04 instruction.

## Test tasks

Extraction schema tests, provenance validation tests, quote span tests, relation classification tests.

## Docs tasks

Document evidence extraction constraints and failure modes.

## GitHub deployment tasks

Use branch `stage/04-evidence-extraction`, PR, CI, Codex review.

## GPT Pro review tasks

Submit Stage 04 packet and request Stage 05 instructions.

## Stop conditions

Stop if extraction fabricates quotes, drops provenance, or becomes generic summarization.
