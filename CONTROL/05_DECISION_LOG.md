# 05 Decision Log

## Purpose

Records architecture, product, process, plugin, and phase acceptance decisions.

## Owner

Engineering lead and product process lead.

## When to update

Update when a decision changes product direction, architecture, governance, stage flow, security posture, or user-instruction precedence.

## Required fields

- ADR id
- Date
- Status
- Context
- Decision
- Consequences
- Follow-up

## Example format

`ADR-0001 | accepted | Research Mode-first and MCP-first evidence-stream architecture`

## Current state

### ADR-0001: FinSignalHub adopts Research Mode-first, MCP-first, evidence-stream architecture

- Date: 2026-05-24
- Status: accepted
- Context: The project must serve researchers through AI Agent workflows, not become a chat product, stock tool, dashboard, generic RAG, or report generator.
- Decision: FinSignalHub will prioritize Research Mode, MCP tools, connectors, evidence-stream artifacts, provenance, and reproducible exports. Business implementation must map to research delta, claim graph, evidence card, literature matrix, method card, dataset card, repro pack, or tool call log value.
- Consequences: Stage gates block product drift. MCP and connector surfaces are primary. UI work is inspect-only unless a later stage plan proves research value.
- Follow-up: Stage 01 may scaffold repo infrastructure only after Stage 00 GitHub and GPT Pro gates are resolved or explicitly blocked.
