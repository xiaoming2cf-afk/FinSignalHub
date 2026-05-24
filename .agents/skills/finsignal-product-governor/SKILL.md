---
name: finsignal-product-governor
description: Review FinSignalHub work for Research Mode-first, MCP-first, evidence-stream alignment and stop product drift.
---

# FinSignal Product Governor

## When to use

Use before any stage implementation and immediately when work resembles chat, generic RAG, stock recommendation, investment advice, report generation, financial dashboard, or model leaderboard behavior.

## Procedure

1. Compare the requested work with `CONTROL/01_PRODUCT_DEFINITION.md`.
2. Map every feature to a researcher need and one of: research delta, claim graph, evidence card, literature matrix, method card, dataset card, repro pack, or tool call log.
3. If mapping fails, stop implementation.
4. Write the drift reason to `CONTROL/20_BLOCKER_LOG.md`.
5. Require a corrected plan before work resumes.

## Required outputs

- Product alignment verdict: PASS, FAIL, or BLOCKED.
- Feature-to-research-value mapping.
- Blocker entry when drift is detected.

## Failure conditions

- Work proceeds after product drift is detected.
- A feature is justified as generic chat, generic RAG, prediction, recommendation, report, dashboard, or leaderboard output.
