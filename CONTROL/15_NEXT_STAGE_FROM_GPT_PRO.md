# 15 Next Stage From GPT Pro

## Purpose

Stores GPT Pro instructions for the next stage.

## Owner

Stage next-goal synthesizer.

## When to update

Update only after GPT Pro passes or conditionally passes the current stage and gives next-stage instructions.

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

`Source Stage 00 | PASS | Next Stage 01 | scaffold repo only | raw instruction pasted below`

## Current state

Source stage: Stage 01.

GPT Pro result: PASS.

Important condition: Stage 01 is accepted. Stage 02 may begin as planning only. Stage 02 implementation is not authorized until the Stage 02 plan exists, GPT Pro plan review passes, user goal approval is recorded, and the Stage 02 GitHub/CI/Codex gates are ready.

## Next Stage ID

Stage 02: Research Mode Domain Models.

## Next Stage Goal

Create the Stage 02 plan for minimum Research Mode domain models and basic CRUD. The plan must define database models, migrations, Pydantic schemas, model-level CRUD services, basic API routers, tests, docs, logs, PR evidence, and GPT Pro plan review.

Do not implement Stage 02 until the Stage 02 plan is reviewed by GPT Pro and the user approves the Stage 02 goal.

## Allowed Planning Files

- `PLANS/STAGE_02_PLAN.md`
- `TASKS/STAGE_02_TASKS.md`
- `CHECKLISTS/STAGE_02_CHECKLIST.md`
- `reviews/stage_02/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_02/PR_BODY.md`
- `reviews/stage_02/STAGE_ACCEPTANCE_RESULT.md`
- `deployments/stage_02/GITHUB_PR.md`
- `CONTROL/04_EXECUTION_LOG.md`
- `CONTROL/07_CODEX_GOAL_REGISTRY.md`
- `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`
- `CONTROL/18_ARTIFACT_REGISTRY.md`
- `CONTROL/19_STAGE_DASHBOARD.md`
- `CONTROL/20_BLOCKER_LOG.md`
- `CONTROL/24_CURRENT_STAGE_STATE.md`
- `CONTROL/25_NEXT_ACTION_QUEUE.md`
- `CONTROL/27_CHECKPOINT_LOG.md`
- `RUNLOG/LONG_RUN_CURRENT.md`
- `RUNLOG/LONG_RUN_SUMMARY.md`

## Stage 02 Implementation File Boundary From GPT Pro

Implementation is not yet authorized. When authorized by GPT Pro and user goal approval, Stage 02 may create or modify only the bounded model-layer areas below:

- `apps/api/app/db/`
- `apps/api/app/models/`
- `apps/api/app/schemas/`
- `apps/api/app/services/`
- `apps/api/app/routers/`
- `apps/api/app/core/`
- `apps/api/tests/`
- `apps/api/alembic/`
- `apps/api/alembic.ini`
- `apps/api/alembic/versions/`
- `docs/architecture/stage_02_domain_models.md`
- `docs/codex/stage_02_commands.md`
- `pyproject.toml`
- `docker-compose.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/phase-deploy.yml`
- `.env.example`
- `README.md`
- `AGENTS.md` only if stage rules need clarification

## Required Stage 02 Model Scope From GPT Pro

The Stage 02 plan must cover these model primitives:

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

Stage 02 may create model tables, schemas, migration, and primitive CRUD. It must not implement business workflows.

## Files Or Areas Not To Touch In Stage 02

- OpenAlex connector.
- Crossref connector.
- Semantic Scholar connector.
- arXiv connector.
- User upload ingestion.
- External API calls.
- LLM adapters.
- LLM extraction.
- Evidence extraction pipeline.
- Quote-span extraction logic beyond a schema field.
- Dedup pipeline.
- Claim graph computation.
- Research delta computation beyond model/table fields.
- Literature matrix generation logic.
- Repro Pack export logic.
- MCP business tools.
- ChatGPT App implementation.
- Claude Connector, Copilot Connector, or other external connector implementation.
- Risk Mode.
- Replay Engine.
- Stock prediction.
- Investment advice.
- Chatbot UI.
- Generic RAG.
- Dashboard product behavior.
- Auth or billing.

## Stage 02 Required Subagents

- `schema-agent`: SQLAlchemy/SQLModel models and relationships.
- `migration-agent`: Alembic setup and migration checks.
- `api-schema-agent`: Pydantic schemas, CRUD routers, and services without business workflow logic.
- `test-agent`: model, migration, CRUD, and forbidden-scope tests.
- `docs-log-agent`: docs, logs, review packet, artifact registry, dashboard, and deployment evidence.

## Stage 02 Required Tests From GPT Pro

The Stage 02 plan must include:

```text
pytest apps/api/tests
alembic upgrade head
alembic downgrade -1 or documented if not supported
alembic upgrade head again
python -m compileall apps/api/app
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02
secret scan
forbidden runtime/scope scan
git diff --check
```

If Postgres is used through Docker, the plan must include `docker compose up -d postgres`, migration pass, and `docker compose down`.

## Stage 02 Acceptance Criteria From GPT Pro

- Stage 02 plan exists and GPT Pro plan review passes.
- SQLAlchemy/SQLModel models exist after implementation is authorized.
- Alembic migration exists and runs after implementation is authorized.
- Pydantic schemas exist after implementation is authorized.
- CRUD routers/services exist for model primitives after implementation is authorized.
- Tests pass.
- No external connectors exist.
- No LLM extraction exists.
- No MCP business tools exist.
- No claim graph or research delta computation exists beyond tables/schemas.
- No Risk Mode, Replay Engine, stock prediction, or investment advice exists.
- Docs, logs, artifact registry, PR, CI, Codex review, GPT Pro final implementation review, and Stage 03 assignment are complete.

## Stage 02 Risks From GPT Pro

- Implementing connectors early is blocking drift.
- Turning `ResearchDelta` into a computation engine is blocking drift.
- Turning `EvidenceItem` into an extraction pipeline is blocking drift.
- Implementing MCP business tools early is blocking drift.
- Over-complex model relationships should be controlled; Stage 02 should stay minimal and relational.
- Irreproducible migrations are blocking.

## Stage 02 Stop Conditions From GPT Pro

Stop and request user or GPT Pro judgment if:

- External data APIs are required.
- A real LLM API key is required.
- Model design exceeds Research Mode P0.
- Alembic migration cannot run and the cause is unclear.
- Auth or billing is required.
- Stage 01 scaffold structure needs a destructive change.
- Investment advice, stock prediction, Risk Mode, or Replay Engine implementation appears.
- Docker/Postgres remains unavailable and migration tests depend on it.

## Raw GPT Pro Instruction Source

Full Stage 01 final implementation response is saved at `reviews/stage_01/GPT_PRO_REVIEW_RESPONSE.md` and duplicated at `reviews/stage_01/GPT_PRO_FINAL_REVIEW_RESPONSE.md`.

## Raw GPT Pro Instruction

```text
GPT Pro Stage 01 final implementation review result: PASS.

Stage 01 is accepted.

Next action:
Begin Stage 02 planning only.

Do not implement Stage 02 yet.

Create PLANS/STAGE_02_PLAN.md.

Stage 02 plan must cover:
- Research Mode domain model scope
- file boundaries
- forbidden scope
- subagents
- migrations
- tests
- CI
- docs
- GitHub PR
- GPT Pro plan review
- stop conditions

After Stage 02 plan is created, prepare reviews/stage_02/GPT_PRO_REVIEW_PACKET.md and submit to GPT Pro for plan review.
```
