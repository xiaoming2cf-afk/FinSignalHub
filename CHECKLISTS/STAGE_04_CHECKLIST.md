# Stage 04 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Approved Stage 04 implementation files only; no database migration, persistence route, MCP business tool, UI, claim graph, Research Delta, Repro Pack, chatbot/RAG, stock/investment, Risk Mode, Replay Engine, auth, billing, or external provider call | PASS locally; external PR review pending after push |
| Functionality | Candidate schema, quote-span validation, no-quote rationale, relation enum, provenance validation, deterministic mock output, worker skeleton, and mock-only tests | PASS locally |
| Tests | Targeted Stage 04 tests, relevant regression group, full API tests, compileall, phase check, secret scan, forbidden-scope scan, and diff check | PASS locally; implementation head still needs live PR #11 CI after push |
| Docs | Architecture, command docs, review/deployment READMEs, GPT Pro response aliases, final GPT Pro recheck files, and implementation-goal PASS files exist | PASS |
| Logs | CONTROL and RUNLOG entries updated | PASS for local records; live PR #11 remains the source of truth for the current evidence head |
| GitHub | Branch, PR, CI, Codex review, PR URL, unresolved-thread check | BLOCKED/PENDING until the pushed implementation head has CI PASS, current-head Codex no-major, and unresolved review threads = 0. Pre-implementation head `2a6378c` was clean. |
| GPT Pro | Plan packet, response, action items, final result, implementation-goal packet, response, implementation final packet, response, and action items | BLOCKED/PENDING until final implementation packet is submitted after live GitHub gate passes |
| Product governance | Stage 04 remains Research Mode evidence-stream candidate generation only | PASS locally |
| Security | No secrets, no provider credentials, no real LLM calls, no live network CI | PASS locally |
| Next stage | GPT Pro final implementation review must provide Stage 05 instruction | BLOCKED until Stage 04 implementation GitHub/Codex/GPT Pro gates pass |

Current Stage 04 status: implementation local checks PASS; final acceptance BLOCKED/PENDING on live PR #11 CI, current-head Codex no-major, unresolved review threads = 0, and GPT Pro final implementation review.
