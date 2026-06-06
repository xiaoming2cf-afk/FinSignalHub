# Stage 04 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Approved Stage 04 implementation files only; no database migration, persistence route, MCP business tool, UI, claim graph, Research Delta, Repro Pack, chatbot/RAG, stock/investment, Risk Mode, Replay Engine, auth, billing, or external provider call | PASS locally; CR-04-029 remediation remains inside Stage 04 schema/test boundary |
| Functionality | Candidate schema, quote-span validation, no-quote rationale, relation enum, provenance validation, deterministic mock output, worker skeleton, and mock-only tests | PASS locally |
| Tests | Targeted Stage 04 tests, relevant regression group, full API tests, compileall, phase check, secret scan, forbidden-scope scan, and diff check | PASS locally after CR-04-034: phase check passed, Stage 04 tests passed 13/13, row IDs are unique, high-confidence credential scan had no matches, and `git diff --check` had only normal Windows line-ending warnings |
| Docs | Architecture, command docs, review/deployment READMEs, GPT Pro response aliases, final GPT Pro recheck files, and implementation-goal PASS files exist | PASS |
| Logs | CONTROL and RUNLOG entries updated | PASS for local records after CR-04-034 route patch; live PR #11 remains the source of truth for the current evidence head |
| GitHub | Branch, PR, CI, Codex review, PR URL, unresolved-thread check | BLOCKED by B-0098 until the CR-04-034 remediation head has PR #11 CI PASS, current-head Codex no-major, and unresolved review threads = 0. Reviewed head `79ec29a42b9119dbaf5edd1c88b7fb4e52fe1368` passed earlier and GPT Pro accepted it; head `1d5739d0734fd9f86bff51849b2bd1c8234c22a5` passed CI but CR-04-034 found stale completed-step routing in `CONTROL/24_CURRENT_STAGE_STATE.md`. |
| GPT Pro | Plan packet, response, action items, final result, implementation-goal packet, response, implementation final packet, response, and action items | PASS for reviewed head `79ec29a42b9119dbaf5edd1c88b7fb4e52fe1368`. Final response is saved in `reviews/stage_04/GPT_PRO_IMPLEMENTATION_REVIEW_RESPONSE.md`; action items are saved in `reviews/stage_04/GPT_PRO_IMPLEMENTATION_ACTION_ITEMS.md`. |
| Product governance | Stage 04 remains Research Mode evidence-stream candidate generation only | PASS locally |
| Security | No secrets, no provider credentials, no real LLM calls, no live network CI | PASS locally |
| Next stage | GPT Pro final implementation review must provide Stage 05 instruction | Stage 05 planning-only instructions captured and now include `reviews/stage_05/CODEX_REVIEW_SUMMARY.md`; Stage 05 implementation remains blocked until a separate Stage 05 plan review and implementation-goal approval. |

Current Stage 04 status: implementation final GPT Pro PASS captured for head `79ec29a42b9119dbaf5edd1c88b7fb4e52fe1368`; CR-04-034 route remediation passes local checks; release/merge/tag remains BLOCKED/PENDING on the remediation head passing live PR #11 CI, current-head Codex no-major, and unresolved review threads = 0.
