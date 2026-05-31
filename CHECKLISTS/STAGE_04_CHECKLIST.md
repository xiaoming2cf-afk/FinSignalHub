# Stage 04 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Planning files only; no extraction implementation package, tests, fixtures, LLM calls, claim graph, Research Delta, MCP business tools, UI, RAG, stock/investment, Risk Mode, or Replay Engine | PASS locally; PR/GPT Pro pending |
| Functionality | Plan defines future extraction candidate schema, quote-span validation, no-quote rationale, relation enum, provenance validation, mock LLM adapter, worker skeleton, and mock-only tests | PASS locally; PR/GPT Pro pending |
| Tests | Planning checks run: phase check, no extraction path, no test/fixture path, forbidden-scope scan, secret scan, diff check | PASS locally |
| Docs | Architecture and command docs exist | PASS locally; PR/GPT Pro pending |
| Logs | CONTROL and RUNLOG entries updated | PASS locally; PR/GPT Pro pending |
| GitHub | Branch, PR, CI, Codex review, PR URL | PENDING |
| GPT Pro | Plan packet, response, action items, final result | PENDING |
| Product governance | Stage 04 remains Research Mode evidence-stream planning only | PASS locally; PR/GPT Pro pending |
| Security | No secrets, no provider credentials, no real LLM calls, no live network CI | PASS locally |
| Next stage | GPT Pro gives implementation or next-stage instruction | PENDING |

Current Stage 04 status: planning-only branch `stage/04-evidence-extraction` passed local planning checks after Stage 03 merge and tag. Stage 04 implementation is not authorized.
