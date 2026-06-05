# Stage 04 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Planning files only; no extraction implementation package, tests, fixtures, LLM calls, claim graph, Research Delta, MCP business tools, UI, RAG, stock/investment, Risk Mode, or Replay Engine | PASS for planning closeout; implementation remains unauthorized |
| Functionality | Plan defines future extraction candidate schema, quote-span validation, no-quote rationale, relation enum, provenance validation, mock LLM adapter, worker skeleton, and mock-only tests | PASS for planning content; implementation not authorized |
| Tests | Planning checks run: phase check, no extraction path, no test/fixture path, forbidden-scope scan, secret scan, diff check | PASS locally for committed content; later heads still need live PR #11 CI after push |
| Docs | Architecture, command docs, review/deployment READMEs, GPT Pro response aliases, and final GPT Pro recheck files exist | PASS |
| Logs | CONTROL and RUNLOG entries updated | PASS for local records; live PR #11 remains the source of truth for the current evidence head |
| GitHub | Branch, PR, CI, Codex review, PR URL, unresolved-thread check | LIVE EXTERNAL GATE. Do not infer PASS from this file. For any checked-out head, Gate 6 is PASS only when the latest live PR #11 head has CI PASS, current-head Codex no-major, and unresolved review threads = 0; otherwise it is BLOCKED/PENDING. |
| GPT Pro | Plan packet, response, action items, final result | PASS for planning, closeout confirmation, and final closeout recheck; implementation authorized only as a separate future `/goal` draft |
| Product governance | Stage 04 remains Research Mode evidence-stream planning only | PASS; no business implementation files created |
| Security | No secrets, no provider credentials, no real LLM calls, no live network CI | PASS locally |
| Next stage | GPT Pro gives implementation-goal instruction | BLOCKED/PENDING until the latest live PR #11 head satisfies the GitHub gate; then drafting a separate implementation `/goal` is allowed, but no extraction implementation may start |

Current Stage 04 status: planning content and GPT Pro closeout are PASS, but the GitHub gate is intentionally a live external gate. Use the latest PR #11 head, CI, current-head Codex response, and unresolved-thread count as the source of truth before drafting a separate implementation `/goal`. Stage 04 implementation is not authorized.
