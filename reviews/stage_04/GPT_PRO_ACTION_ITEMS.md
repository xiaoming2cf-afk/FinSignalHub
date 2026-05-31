# Stage 04 GPT Pro Action Items

This file is the protocol-compatible action-item pointer for Stage 04.

The full Stage 04 planning action items are saved at:

- `reviews/stage_04/GPT_PRO_PLAN_ACTION_ITEMS.md`

## Required Closeout

| Item | Status |
| --- | --- |
| Save GPT Pro planning response | done locally |
| Save GPT Pro planning action items | done locally |
| Update Stage 04 acceptance, current state, dashboard, action queue, RunLog, artifact registry, and checkpoint log | done locally before final closeout checks |
| Preserve Stage 04 implementation prohibition | active |
| Push evidence-only closeout commit | pending |
| Run live PR #11 CI and current-head Codex review after push | pending |

## Authorized Next Action

Draft a separate Stage 04 implementation `/goal` only after the evidence-only closeout head passes live PR #11 CI and current-head Codex review.

## Still Forbidden

Do not create `apps/api/finsignalhub_api/extraction/`, `apps/api/tests/test_stage04_extraction.py`, or `apps/api/tests/fixtures/stage04_extraction/` until the separate implementation goal is drafted, reviewed, and accepted. Do not add external LLM calls, real network calls, production extraction, claim graph computation, Research Delta, Repro Pack export, MCP business tools, UI/dashboard behavior, chatbot/RAG behavior, stock prediction, investment advice, Risk Mode, Replay Engine, auth, or billing.
