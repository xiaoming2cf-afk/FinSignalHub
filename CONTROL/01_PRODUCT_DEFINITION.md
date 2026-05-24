# 01 Product Definition

## Purpose

Defines the FinSignalHub product identity, user base, allowed outputs, and forbidden product directions.

## Owner

Product process lead.

## When to update

Update when the user changes product positioning or GPT Pro approves a material product-scope change.

## Required fields

- Product identity
- Primary users
- Primary entrypoints
- Core outputs
- Non-goals
- Drift response

## Example format

`Allowed: EvidenceItem supports provenance-backed research delta. Forbidden: stock recommendation.`

## Current state

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. It serves researchers, PhD students, labs, innovation teams, and research-oriented product teams.

Primary entrypoints are MCP tools, ChatGPT App, Claude Connector, Copilot Connector, Gemini Connector, and other AI Agent workflows.

Core outputs are research delta, claim graph, evidence card, literature matrix, method card, dataset card, and repro pack.

Forbidden directions: chatbot, stock recommendation, investment advice, generic RAG, generic literature summary, ordinary report generator, financial dashboard, or model leaderboard.

Drift response: stop, invoke `finsignal-product-governor`, write `CONTROL/20_BLOCKER_LOG.md`, and do not continue until the direction is corrected.
