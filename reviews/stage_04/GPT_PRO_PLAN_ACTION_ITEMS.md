# Stage 04 GPT Pro Plan Review Action Items

## Result

Stage 04 planning: PASS.

Implementation status: not authorized. Only a separate Stage 04 implementation `/goal` may be drafted after the planning closeout evidence is saved and the resulting PR head passes live CI plus current-head Codex.

## Closeout Actions

| Item | Status | Evidence |
| --- | --- | --- |
| Save GPT Pro response | done locally | `reviews/stage_04/GPT_PRO_PLAN_REVIEW_RESPONSE.md` |
| Save action items | done locally | this file |
| Update Stage 04 acceptance result | in progress | `reviews/stage_04/STAGE_ACCEPTANCE_RESULT.md` |
| Update current state, action queue, dashboard, RunLog, checkpoint, and artifact registry | in progress | `CONTROL/19`, `CONTROL/24`, `CONTROL/25`, `CONTROL/27`, `CONTROL/18`, `RUNLOG/` |
| Record current head, CI PASS, and Codex no-major evidence | done locally | PR #11 head `d62d8d8eafb73eb207ba401e12f9d073dff61223`; CI links and Codex link in response file |
| Keep Stage 04 implementation unauthorized | active | no extraction implementation files may be created until a separate `/goal` is accepted |

## Authorized Next Draft Only

Draft a separate Stage 04 implementation `/goal` with:

- Objective: implement a mock-only evidence extraction skeleton that can later transform Stage 03 normalized `Document` records into provenance-preserving `EvidenceItem` candidate payloads.
- Allowed paths for the later implementation goal: `apps/api/finsignalhub_api/extraction/`, `apps/api/tests/test_stage04_extraction.py`, `apps/api/tests/fixtures/stage04_extraction/`, Stage 04 docs/reviews/deployments/logs, and required `CONTROL/`, `RUNLOG/`, `TASKS/`, and `CHECKLISTS/` records.
- Required implementation scope: evidence candidate schema, relation type enum, quote-span validator, no-quote rationale validator, provenance preservation validator, deterministic mock LLM adapter, and mock-only worker skeleton.
- Required tests: mock-only extraction tests, no-network enforcement, quote-span valid/invalid cases, no-quote rationale requirement, relation validation, provenance preservation, candidate schema validation, deterministic mock adapter output, worker fixture test, secret scan, forbidden-scope scan, `phase_check.py --stage 04`, compileall, `git diff --check`, CI, Codex, and final GPT Pro implementation review.

## Forbidden Until Separate Goal Starts

- External LLM API calls.
- Real network calls.
- Production extraction pipeline.
- Claim graph computation.
- Research Delta computation.
- Repro Pack export logic.
- MCP business tools.
- UI/dashboard behavior.
- Chatbot/RAG behavior.
- Stock prediction or investment advice.
- Risk Mode or Replay Engine.
- Auth or billing.
- Connector implementation changes unless required by a documented blocker and reviewed separately.

## Stop Conditions For The Future Implementation Goal

Stop if a real LLM API key, external network access, claim graph work, Research Delta work, Repro Pack output, MCP business tools, UI/dashboard behavior, auth/billing, stock/investment behavior, chatbot/RAG behavior, Risk Mode, Replay Engine, unresolved CI/Codex gate, or unreviewed Stage 03 connector modification appears.
