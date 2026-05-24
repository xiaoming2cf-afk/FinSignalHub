# 02 Stage Roadmap

## Purpose

Defines the staged delivery path for FinSignalHub from governance through demo acceptance.

## Owner

Engineering lead and phase acceptance lead.

## When to update

Update only after GPT Pro approves a roadmap change or gives next-stage instructions that alter stage boundaries.

## Required fields

- Stage id
- Stage name
- Goal
- Main outputs
- Forbidden work
- Gate dependency

## Example format

`Stage 06 | MCP tools | expose Research Mode tools | forbidden: admin UI expansion | requires Stage 05 PASS`

## Current state

| Stage | Name | Goal | Status |
| --- | --- | --- | --- |
| 00 | Control system and capability audit | Create governance, audit, logs, skills, plugin draft, GitHub/GPT Pro protocols | active |
| 01 | Repo scaffold | Create monorepo, FastAPI skeleton, MCP server skeleton, Next.js admin skeleton, Docker Compose, PostgreSQL, CI, health check | planned |
| 02 | Research Mode domain models | Create models around ResearchProject, EvidenceItem, ResearchClaim, ClaimEvidenceEdge, ResearchDelta, LiteratureMatrix, MethodCard, DatasetCard, ReproPackExport, ToolCallLog | planned |
| 03 | Source connectors | Create OpenAlex, Crossref, Semantic Scholar, arXiv, and user upload connectors with normalized Document output | planned |
| 04 | Evidence extraction | Create extraction schema, mock LLM adapter, provenance validation, quote span validation, and relation classification | planned |
| 05 | Claim graph and research delta | Build claim graph, evidence edges, delta computation, literature matrix, method card, and dataset card first versions | planned |
| 06 | MCP tools | Expose Research Mode tools with schemas, tests, provenance, and call logs | planned |
| 07 | Admin UI | Create inspect-only admin UI for evidence streams, tool calls, and claim graph state | planned |
| 08 | Repro Pack | Export BibTeX, CSV, JSONL, Markdown, and manifest | planned |
| 09 | Demo acceptance | Run three demos and complete final MVP acceptance | planned |

P0 is Research Mode MVP only. Risk Mode, Replay Engine, investment tools, prediction tools, generic RAG, and report generation are out of scope.
