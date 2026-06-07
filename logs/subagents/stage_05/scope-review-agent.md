# scope-review-agent

## Role

Review Stage 05 planning for product drift and forbidden behavior.

## Files touched

None. This is a planning log only.

## Allowed files

Stage 05 planning and governance files only.

## Forbidden files

- `apps/api/finsignalhub_api/claim_graph/` during planning
- `apps/api/finsignalhub_api/research_delta/` during planning
- Stage 05 tests or fixtures during planning
- MCP tools
- Repro Pack export
- UI/dashboard
- chatbot/RAG
- stock prediction or investment advice
- Risk Mode or Replay Engine

## Summary

Stage 05 planning maps to research evidence-stream value because it defines how claims, evidence, relations, and deltas remain provenance-bearing and replayable. It must not produce end-user financial decisions, report prose, or dashboards.

## Risks

- "Delta" wording invites report-generation or risk-scoring behavior.
- "Claim graph" wording invites generic graph analytics.
- Implementation pressure bypasses GPT Pro plan and goal gates.

## Tests

Future forbidden-scope scan should search for Stage 06+ tool exposure, investment language, report-generation commands, dashboard behavior, provider calls, and real LLM clients.

## Unresolved issues

None for planning. Implementation must wait for GPT Pro approval.
