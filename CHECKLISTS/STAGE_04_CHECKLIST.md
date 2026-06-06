# Stage 04 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Approved Stage 04 implementation files only; no database migration, persistence route, MCP business tool, UI, claim graph, Research Delta, Repro Pack, chatbot/RAG, stock/investment, Risk Mode, Replay Engine, auth, billing, or external provider call | PASS locally; CR-04-029 remediation remains inside Stage 04 schema/test boundary |
| Functionality | Candidate schema, quote-span validation, no-quote rationale, relation enum, provenance validation, deterministic mock output, worker skeleton, and mock-only tests | PASS locally; locator-only quote spans now require quote text to appear in `document_text` |
| Tests | Targeted Stage 04 tests, relevant regression group, full API tests, compileall, phase check, secret scan, forbidden-scope scan, and diff check | PASS locally for B-0106: Stage 04 tests passed 15/15, phase_check 04 passed, primary artifact/checkpoint/blocker IDs are unique, high-confidence secret scan had no matches, final RunLog route search is clean for the required branches, and `git diff --check` had only normal Windows line-ending warnings. |
| Docs | Architecture, command docs, review/deployment READMEs, GPT Pro response aliases, final GPT Pro recheck files, and implementation-goal PASS files exist | PASS |
| Logs | CONTROL and RUNLOG entries updated | PASS locally through A-0505/CP-0368 for the B-0106 CR-04-044 final RunLog route remediation. |
| GitHub | Branch, PR, CI, Codex review, PR URL, unresolved-thread check | BLOCKED by B-0106. PR #11 head `cb95156a73bac96c7dd2c3e4a0634355b2b059ac` passed CI, but Codex opened CR-04-044. B-0106 passed local checks and must follow the state-dependent push/live-gate route. |
| GPT Pro | Plan packet, response, action items, final result, implementation-goal packet, response, implementation final packet, response, and action items | PASS for current reviewed head `cd3c1cfeef0dc075f5fd35cfd4d6451c712e75df`. Current-head final response is saved in `reviews/stage_04/GPT_PRO_CURRENT_HEAD_FINAL_REVIEW_RESPONSE.md`; action items are saved in `reviews/stage_04/GPT_PRO_CURRENT_HEAD_FINAL_ACTION_ITEMS.md`. |
| Product governance | Stage 04 remains Research Mode evidence-stream candidate generation only | PASS locally |
| Security | No secrets, no provider credentials, no real LLM calls, no live network CI | PASS locally |
| Next stage | GPT Pro final implementation review must provide Stage 05 instruction | Stage 05 planning-only instructions captured and now include `reviews/stage_05/CODEX_REVIEW_SUMMARY.md`; Stage 05 implementation remains blocked until a separate Stage 05 plan review and implementation-goal approval. |

Current Stage 04 status: current-head GPT Pro PASS captured for head `cd3c1cfeef0dc075f5fd35cfd4d6451c712e75df`; B-0106 CR-04-044 route remediation passed local checks; release/merge/tag remains BLOCKED until this remediation passes live PR #11 CI, current-head Codex no-major, and unresolved review threads = 0.
