# Stage 04 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Planning files only; no extraction implementation package, tests, fixtures, LLM calls, claim graph, Research Delta, MCP business tools, UI, RAG, stock/investment, Risk Mode, or Replay Engine | PASS for planning scope; implementation remains unauthorized |
| Functionality | Plan defines future extraction candidate schema, quote-span validation, no-quote rationale, relation enum, provenance validation, mock LLM adapter, worker skeleton, and mock-only tests | PASS for planning content; implementation not authorized |
| Tests | Planning checks run: phase check, no extraction path, no test/fixture path, forbidden-scope scan, secret scan, diff check | PASS locally |
| Docs | Architecture, command docs, review/deployment READMEs, and GPT Pro response aliases exist | PASS for planning docs |
| Logs | CONTROL and RUNLOG entries updated | PASS for planning; status-only updates remain subject to live-head PR #11 CI/Codex before merge |
| GitHub | Branch, PR, CI, Codex review, PR URL | BLOCKED by CR-04-023 until the current-state live-route remediation head passes live PR #11 CI and current-head Codex. Head `926b24fc59d5bfc7eba11f3f352c72ad6dcde632` passed CI but Codex found `CONTROL/24_CURRENT_STAGE_STATE.md` still pointed the next required action at an already-completed commit/push step. The current remediation must use live PR #11 evidence after push. |
| GPT Pro | Plan packet, response, action items, final result | PASS for Stage 04 planning and closeout confirmation; implementation authorized only as a separate future `/goal` draft |
| Product governance | Stage 04 remains Research Mode evidence-stream planning only | PASS; no business implementation files created |
| Security | No secrets, no provider credentials, no real LLM calls, no live network CI | PASS locally |
| Next stage | GPT Pro gives implementation or next-stage instruction | PASS for drafting a separate implementation `/goal` only after the live PR #11 head is clean; no extraction implementation may start |

Current Stage 04 status: planning-only branch `stage/04-evidence-extraction` has GPT Pro planning PASS and GPT Pro closeout confirmation PASS, but final GitHub Gate 6 is blocked by CR-04-023 until the current remediation head has CI PASS plus current-head Codex no-major. Stage 04 implementation is not authorized; the next allowed step is a separate implementation `/goal` draft only after the pushed live PR #11 head is clean.
