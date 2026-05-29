# 15 Next Stage From GPT Pro

## Purpose

Stores GPT Pro instructions for the next authorized work unit.

## Owner

Stage next-goal synthesizer.

## When to update

Update only after GPT Pro passes or conditionally passes a stage or plan gate and gives next-step instructions.

## Required fields

- Source stage
- GPT Pro result
- Next stage id
- Next stage goal
- Required files
- Acceptance criteria
- Risks
- Constraints
- Raw GPT Pro instruction

## Example format

`Source Stage 02 plan gate | PASS | Next Stage 02 implementation | domain models only | raw instruction pasted below`

## Current state

Source stage: Stage 02 plan gate.

GPT Pro result: PASS.

Important condition: Stage 02 implementation may begin only after explicit user `/goal` approval and after this GPT Pro plan review response/action items are saved. Stage 03 is not authorized.

## Next Stage ID

Stage 02 implementation: Research Mode Domain Models.

## Next Stage Goal

Implement Stage 02: Research Mode Domain Models.

Use the approved `PLANS/STAGE_02_PLAN.md` and the GPT Pro Stage 02 plan review response.

FinSignalHub remains Research Mode-first, MCP-first, and evidence-stream oriented. Stage 02 is domain models only.

## Stage 02 Implementation Scope

Implement:

- Research Mode domain model schema.
- Alembic migration.
- Pydantic schemas.
- Model-level CRUD services and routers.
- Tests.
- Docs.
- Logs.
- Acceptance artifacts.

## Allowed Models

- `ResearchProject`
- `Source`
- `Document`
- `EvidenceItem`
- `ResearchClaim`
- `ClaimEvidenceEdge`
- `ResearchDelta`
- `LiteratureMatrixRow`
- `MethodCard`
- `DatasetCard`
- `ReproPackExport`
- `ToolCallLog`

## Required Provenance Fields

- Source identity.
- Source type.
- Retrieval or ingestion time.
- Publication or release time where applicable.
- URL / DOI / locator where applicable.
- Quoted evidence span or explicit no-quote rationale.
- Transformation notes.
- Confidence.
- Tool-call lineage where applicable.
- Validation status.

## Allowed Files

- `apps/api/finsignalhub_api/db/`
- `apps/api/finsignalhub_api/models/`
- `apps/api/finsignalhub_api/schemas/`
- `apps/api/finsignalhub_api/services/`
- `apps/api/finsignalhub_api/routers/`
- `apps/api/finsignalhub_api/core/`
- `apps/api/alembic/`
- `apps/api/alembic.ini`
- `apps/api/tests/`
- `docs/architecture/stage_02_domain_models.md`
- `docs/codex/stage_02_commands.md`
- `reviews/stage_02/`
- `deployments/stage_02/`
- `logs/subagents/stage_02/`
- `CONTROL/` and `RUNLOG/` files needed for logs, artifacts, and status.

## Forbidden Scope

Do not implement:

- Connectors.
- External API calls.
- LLM adapters.
- Evidence extraction pipeline.
- Dedup pipeline.
- Claim graph computation.
- Research delta computation beyond table/schema fields.
- Literature matrix generation.
- Repro Pack export.
- MCP business tools.
- ChatGPT App.
- Claude Connector.
- Copilot Connector.
- Gemini Connector.
- Risk Mode.
- Replay Engine.
- Stock prediction.
- Investment advice.
- Chatbot UI.
- Generic RAG.
- Dashboard behavior.
- Auth or billing.

## Required Subagents

- `schema-agent`
- `migration-agent`
- `api-schema-agent`
- `test-agent`
- `docs-log-agent`

Each subagent must write a bounded log under `logs/subagents/stage_02/`.

## Required Tests

- `pytest apps/api/tests`
- `alembic upgrade head`
- `alembic downgrade -1` or documented blocker
- `alembic upgrade head`
- `python -m compileall apps/api/finsignalhub_api`
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02`
- Secret scan
- Forbidden scope scan
- `git diff --check`

If Docker/Postgres is required, run `docker compose up -d postgres` and migration checks. If Docker/Postgres is unavailable, record a blocker and do not claim full DB acceptance.

## Done When

1. All approved models exist.
2. Alembic migration exists and runs.
3. Pydantic schemas exist.
4. CRUD services/routers exist for model primitives.
5. Tests pass.
6. No forbidden Stage 03+ logic exists.
7. Docs are updated.
8. Logs are updated.
9. Artifact registry is updated.
10. PR is updated.
11. `@codex review` is requested and critical findings are resolved.
12. CI passes.
13. GPT Pro final implementation review passes.
14. GPT Pro assigns Stage 03.

## Stop Conditions

Stop if:

- External API key is needed.
- LLM API key is needed.
- Connector, extraction, claim graph, delta, or MCP business logic is requested.
- Product scope drifts.
- Database migration cannot run and no safe fallback is available.

## Raw GPT Pro Instruction Source

Full Stage 02 plan gate response is saved at:

- `reviews/stage_02/GPT_PRO_PLAN_REVIEW_RESPONSE.md`
- `reviews/stage_02/GPT_PRO_REVIEW_RESPONSE.md`

## Raw GPT Pro Instruction

```text
Stage 02 plan result: PASS

Stage 02 implementation may begin:
YES, but only after user /goal approval and after this GPT Pro plan review response/action items are saved.

Stage 03:
NOT authorized.

Implementation boundary:
Domain models + migrations + schemas + CRUD primitives + tests + docs/logs only.

Main must-fix before implementation:
Save this review response and update current stage state/action queue/runlog/artifact registry. Then proceed only via explicit /goal.
```
