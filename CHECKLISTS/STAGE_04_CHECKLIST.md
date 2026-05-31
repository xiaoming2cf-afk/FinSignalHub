# Stage 04 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Planning files only; no extraction implementation package, tests, fixtures, LLM calls, claim graph, Research Delta, MCP business tools, UI, RAG, stock/investment, Risk Mode, or Replay Engine | PASS for planning scope; closeout head remediation pending |
| Functionality | Plan defines future extraction candidate schema, quote-span validation, no-quote rationale, relation enum, provenance validation, mock LLM adapter, worker skeleton, and mock-only tests | PASS for planning content; implementation not authorized |
| Tests | Planning checks run: phase check, no extraction path, no test/fixture path, forbidden-scope scan, secret scan, diff check | PASS locally |
| Docs | Architecture, command docs, review/deployment READMEs, and GPT Pro response aliases exist | PASS for planning docs; closeout wording remediation pending |
| Logs | CONTROL and RUNLOG entries updated | PASS for planning; CR-04-011/012/013 remediation must be pushed and externally rechecked |
| GitHub | Branch, PR, CI, Codex review, PR URL | BLOCKED for closeout: PR #11 head `f59c33ec4459fe925a4785d26185165a16b863e9` passed CI but Codex returned CR-04-011/012/013; remediation head must pass live CI and current-head Codex |
| GPT Pro | Plan packet, response, action items, final result | PASS for Stage 04 planning; implementation authorized only as a separate future `/goal` draft |
| Product governance | Stage 04 remains Research Mode evidence-stream planning only | PASS; no business implementation files created |
| Security | No secrets, no provider credentials, no real LLM calls, no live network CI | PASS locally |
| Next stage | GPT Pro gives implementation or next-stage instruction | BLOCKED for closeout until CR-04-011/012/013 remediation head passes live PR #11 CI/Codex; no extraction implementation may start |

Current Stage 04 status: planning-only branch `stage/04-evidence-extraction` has GPT Pro planning PASS, but closeout is blocked by CR-04-011/012/013 until the next remediation head passes live PR #11 CI and current-head Codex. Stage 04 implementation is not authorized.
