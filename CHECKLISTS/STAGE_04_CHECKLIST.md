# Stage 04 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Planning files and implementation-goal draft only; no extraction implementation package, tests, fixtures, LLM calls, claim graph, Research Delta, MCP business tools, UI, RAG, stock/investment, Risk Mode, or Replay Engine | PASS for planning closeout and implementation-goal draft; implementation not started |
| Functionality | Plan and accepted goal define future extraction candidate schema, quote-span validation, no-quote rationale, relation enum, provenance validation, mock LLM adapter, worker skeleton, and mock-only tests | PASS for planning and goal definition; implementation not started |
| Tests | Planning checks run: phase check, no extraction path, no test/fixture path, forbidden-scope scan, secret scan, diff check | PASS locally for committed content; later heads still need live PR #11 CI after push |
| Docs | Architecture, command docs, review/deployment READMEs, GPT Pro response aliases, final GPT Pro recheck files, and implementation-goal PASS files exist | PASS |
| Logs | CONTROL and RUNLOG entries updated | PASS for local records; live PR #11 remains the source of truth for the current evidence head |
| GitHub | Branch, PR, CI, Codex review, PR URL, unresolved-thread check | LIVE EXTERNAL GATE. Do not infer PASS from this file. For any checked-out head, Gate 6 is PASS only when the latest live PR #11 head has CI PASS, current-head Codex no-major, and unresolved review threads = 0; otherwise it is BLOCKED/PENDING. |
| GPT Pro | Plan packet, response, action items, final result, implementation-goal packet, response, and action items | PASS for planning, closeout confirmation, final closeout recheck, and implementation-goal draft; implementation can start only after the response-saving head passes live GitHub/Codex/review-thread gates |
| Product governance | Stage 04 remains Research Mode evidence-stream planning only | PASS; no business implementation files created |
| Security | No secrets, no provider credentials, no real LLM calls, no live network CI | PASS locally |
| Next stage | GPT Pro accepted the exact Stage 04 implementation `/goal` | BLOCKED/PENDING until the response-saving evidence head satisfies live PR #11 CI, current-head Codex no-major, and unresolved review threads = 0; then implementation may start only under the accepted `/goal` |

Current Stage 04 status: planning content, GPT Pro closeout, and implementation-goal draft are PASS, but the GitHub gate is intentionally a live external gate. Use the latest PR #11 head, CI, current-head Codex response, and unresolved-thread count as the source of truth before starting implementation. Stage 04 implementation is not started.
