# GPT Pro Stage 02 Plan Action Items

Source response: `reviews/stage_02/GPT_PRO_PLAN_REVIEW_RESPONSE.md`

## Result

Stage 02 plan gate: PASS.

Stage 02 implementation may begin only after:

1. This GPT Pro plan review response is saved.
2. Action items are saved.
3. Current stage state, action queue, RunLog, dashboard, and artifact registry are updated.
4. The user gives explicit Stage 02 `/goal` approval.

Stage 03 is not authorized.

## Must-Fix Before Implementation

- Save `reviews/stage_02/GPT_PRO_PLAN_REVIEW_RESPONSE.md`.
- Save this action item file and the generic `reviews/stage_02/GPT_PRO_ACTION_ITEMS.md`.
- Update `reviews/stage_02/STAGE_ACCEPTANCE_RESULT.md`.
- Update `CONTROL/24_CURRENT_STAGE_STATE.md`.
- Update `CONTROL/25_NEXT_ACTION_QUEUE.md`.
- Update `CONTROL/27_CHECKPOINT_LOG.md`.
- Update `RUNLOG/LONG_RUN_CURRENT.md` and `RUNLOG/LONG_RUN_SUMMARY.md`.
- Update `CONTROL/18_ARTIFACT_REGISTRY.md`.
- Update `CONTROL/19_STAGE_DASHBOARD.md`.
- Keep implementation blocked until explicit user `/goal` approval.

## Implementation Boundary

Allowed scope after user `/goal` approval:

- Domain models.
- Alembic migrations.
- Pydantic schemas.
- Model-level CRUD services and routers.
- Tests.
- Docs and logs.

Forbidden scope remains:

- Connectors.
- External API calls.
- LLM adapters.
- Evidence extraction.
- Dedup pipeline.
- Claim graph computation.
- Research delta computation beyond model/table fields.
- Literature matrix generation.
- Repro Pack export.
- MCP business tools.
- ChatGPT App, Claude Connector, Copilot Connector, Gemini Connector.
- Risk Mode.
- Replay Engine.
- Stock prediction.
- Investment advice.
- Chatbot UI.
- Generic RAG.
- Dashboard product behavior.
- Auth or billing.

## Required Next Step

Prepare the Stage 02 implementation `/goal` from `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`, then wait for explicit user approval before implementing.
