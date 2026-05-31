# Stage 04 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Planning files only; no extraction implementation package, tests, fixtures, LLM calls, claim graph, Research Delta, MCP business tools, UI, RAG, stock/investment, Risk Mode, or Replay Engine | PASS for planning scope; implementation remains unauthorized |
| Functionality | Plan defines future extraction candidate schema, quote-span validation, no-quote rationale, relation enum, provenance validation, mock LLM adapter, worker skeleton, and mock-only tests | PASS for planning content; implementation not authorized |
| Tests | Planning checks run: phase check, no extraction path, no test/fixture path, forbidden-scope scan, secret scan, diff check | PASS locally |
| Docs | Architecture, command docs, review/deployment READMEs, and GPT Pro response aliases exist | PASS for planning docs |
| Logs | CONTROL and RUNLOG entries updated | PASS for planning; status-only updates remain subject to live-head PR #11 CI/Codex before merge |
| GitHub | Branch, PR, CI, Codex review, PR URL | PASS for reviewed remediation head `2601f25bb33a9062e27c841d352a31bc7c467eca`: CI passed and Codex no-major at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11#issuecomment-4586063499; any later status-only head must use live PR #11 evidence |
| GPT Pro | Plan packet, response, action items, final result | PASS for Stage 04 planning; implementation authorized only as a separate future `/goal` draft |
| Product governance | Stage 04 remains Research Mode evidence-stream planning only | PASS; no business implementation files created |
| Security | No secrets, no provider credentials, no real LLM calls, no live network CI | PASS locally |
| Next stage | GPT Pro gives implementation or next-stage instruction | PASS for drafting a separate implementation `/goal` only after the live PR #11 head is clean; no extraction implementation may start |

Current Stage 04 status: planning-only branch `stage/04-evidence-extraction` has GPT Pro planning PASS and CR-04-011/012/013 remediation head `2601f25` has CI PASS plus Codex no-major. Stage 04 implementation is not authorized; the next allowed step is a separate implementation `/goal` draft only if the live PR #11 head remains clean.
