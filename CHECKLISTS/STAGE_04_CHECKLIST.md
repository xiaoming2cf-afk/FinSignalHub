# Stage 04 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Planning files only; no extraction implementation package, tests, fixtures, LLM calls, claim graph, Research Delta, MCP business tools, UI, RAG, stock/investment, Risk Mode, or Replay Engine | PASS for planning closeout; implementation remains unauthorized |
| Functionality | Plan defines future extraction candidate schema, quote-span validation, no-quote rationale, relation enum, provenance validation, mock LLM adapter, worker skeleton, and mock-only tests | PASS for planning content; implementation not authorized |
| Tests | Planning checks run: phase check, no extraction path, no test/fixture path, forbidden-scope scan, secret scan, diff check | PASS locally; evidence-sync head still needs live PR #11 CI after push |
| Docs | Architecture, command docs, review/deployment READMEs, GPT Pro response aliases, and final GPT Pro recheck files exist | PASS |
| Logs | CONTROL and RUNLOG entries updated | PASS; live PR #11 remains the source of truth for the current evidence head |
| GitHub | Branch, PR, CI, Codex review, PR URL, unresolved-thread check | PASS for reviewed head `3864181e1dfcbdf522884e7f78e4cb0815b96966`: CI PASS, Codex no-major, unresolved review threads = 0. This evidence-sync commit must also pass live CI and current-head Codex after push. |
| GPT Pro | Plan packet, response, action items, final result | PASS for planning, closeout confirmation, and final closeout recheck; implementation authorized only as a separate future `/goal` draft |
| Product governance | Stage 04 remains Research Mode evidence-stream planning only | PASS; no business implementation files created |
| Security | No secrets, no provider credentials, no real LLM calls, no live network CI | PASS locally |
| Next stage | GPT Pro gives implementation-goal instruction | PASS for drafting a separate implementation `/goal` only after this evidence-sync head is clean; no extraction implementation may start |

Current Stage 04 status: planning closeout PASS after the live PR #11 evidence-sync head has CI PASS and current-head Codex no-major. Stage 04 implementation is not authorized; the next allowed step is a separate implementation `/goal` draft only.
