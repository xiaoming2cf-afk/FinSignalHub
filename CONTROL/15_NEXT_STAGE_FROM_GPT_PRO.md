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

Source stage: Stage 00.1.

GPT Pro result: PASS.

Important condition: Stage 01 planning may begin only. Stage 01 implementation is not authorized until Stage 01 plan exists, GPT Pro approves the Stage 01 plan, Docker daemon is revalidated, PR #6 is merged or Stage 01 branches from `stage/00-1-governance-cleanup`, and no Stage 01 blocker remains.

## Next Stage ID

Stage 01: Repo Scaffold.

## Next Stage Goal

Create the initial FinSignalHub monorepo scaffold plan without implementing business domain logic.

The Stage 01 plan must define a minimal scaffold for:

- FastAPI backend skeleton.
- MCP server skeleton.
- Next.js admin skeleton.
- PostgreSQL service via Docker Compose.
- Redis service placeholder only if justified.
- Health checks.
- Test framework.
- CI workflow.
- Environment configuration.
- Project documentation.

Do not implement any Stage 01 runtime files until the Stage 01 plan is approved by GPT Pro and the user.

Do not implement ResearchProject models, EvidenceItem models, ResearchClaim models, ClaimEvidenceEdge, ResearchDelta, LiteratureMatrix, MethodCard, DatasetCard, ReproPackExport, ToolCallLog, connectors, evidence extraction, claim graph, MCP business tools, Repro Pack logic, Risk Mode, Replay Engine, financial prediction, investment advice, or chatbot UI in Stage 01.

## Allowed Files Or Directories

- `README.md`
- `AGENTS.md`
- `CHANGELOG.md`
- `.env.example`
- `CONTROL/04_EXECUTION_LOG.md`
- `CONTROL/05_DECISION_LOG.md`
- `CONTROL/07_CODEX_GOAL_REGISTRY.md`
- `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`
- `CONTROL/18_ARTIFACT_REGISTRY.md`
- `CONTROL/19_STAGE_DASHBOARD.md`
- `CONTROL/20_BLOCKER_LOG.md`
- `PLANS/STAGE_01_PLAN.md`
- `TASKS/STAGE_01_TASKS.md`
- `CHECKLISTS/STAGE_01_CHECKLIST.md`
- `reviews/stage_01/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_01/PR_BODY.md`
- `reviews/stage_01/STAGE_ACCEPTANCE_RESULT.md`
- `deployments/stage_01/`
- `.github/workflows/ci.yml`
- `.github/workflows/phase-deploy.yml`
- `pyproject.toml`
- `package.json`
- `docker-compose.yml`
- `apps/api/`
- `apps/mcp_server/`
- `apps/web_admin/`
- `docs/architecture/stage_01_repo_scaffold.md`
- `docs/codex/stage_01_commands.md`

## Files Or Areas Not To Touch

- Domain models for ResearchProject, EvidenceItem, ResearchClaim, Document, or similar product entities.
- Alembic migrations for product tables.
- OpenAlex, Crossref, Semantic Scholar, or arXiv connectors.
- Evidence extraction workers.
- LLM adapters.
- Claim graph logic.
- Research delta logic.
- Literature matrix logic.
- Repro Pack export logic.
- Risk Mode.
- Replay Engine.
- Financial prediction logic.
- Investment advice logic.
- Generic chatbot UI.
- Production auth system.
- Billing system.

## Stage 01 Functional Requirements

- FastAPI backend exposes `GET /health` returning status ok and service identity.
- MCP server skeleton starts without business tools. It may expose only health, ping, or server info.
- Next.js admin skeleton shows only a placeholder identifying FinSignalHub as a Research Mode-first evidence-stream plugin and Stage 01 scaffold.
- Docker Compose includes postgres, api, mcp_server, and web_admin.
- Tests cover API health, MCP health/server info, web build, and Docker Compose config.

## Stage 01 Acceptance Criteria

- Stage 00.1 GitHub PR #6 is merged, or Stage 01 branch is explicitly based on `stage/00-1-governance-cleanup` and this dependency is logged.
- Stage 01 plan exists and is approved by GPT Pro before implementation.
- Branch `stage/01-repo-scaffold` is created.
- Docker Compose starts required services.
- API `/health` returns ok.
- MCP server starts and returns server info or health.
- Web admin opens locally.
- Tests pass.
- CI passes or CI blockers are recorded.
- No business domain logic is implemented.
- Docs, logs, PR, `@codex review`, GPT Pro packet, GPT Pro review, and Stage 02 instruction are complete.

## Stage 01 Required Tests

```text
pytest apps/api/tests
pytest apps/mcp_server/tests
npm --prefix apps/web_admin run build
docker compose config
docker compose up --build
curl http://localhost:8000/health
```

If local Docker is unavailable, Codex must not mark Stage 01 complete.

## Stage 01 Risks

- Over-scaffolding into domain models or business logic.
- Docker unavailable.
- Frontend scope creep into dashboard or product UI.
- MCP tool creep into Research Mode business tools before Stage 06.
- GitHub and Docker availability may regress between stages and must be revalidated inside the approved Stage 01 plan and goal.

## Stage 01 Stop Conditions

Stop if Git repo is unavailable, GitHub CLI is unauthenticated without approved manual path, Docker daemon is unavailable, branch/PR/tests cannot be completed, business logic is about to be implemented, GPT Pro cannot be reviewed, secrets are required, or `AGENTS.md` conflicts with latest user instructions.

## Raw GPT Pro Instruction Source

Full Stage 00.1 response is saved at `reviews/stage_00_1/GPT_PRO_REVIEW_RESPONSE.md`.

## Stage 00.1 GPT Pro Confirmation Summary

GPT Pro answered `Stage 00.1: PASS`, stated that governance-only scope was satisfied, and authorized Stage 01 planning only.

## Stage 01 Planning Read List

Before creating `PLANS/STAGE_01_PLAN.md`, read:

- `AGENTS.md`
- `PLANS.md`
- `README.md`
- `CONTROL/00_MASTER_CONTROL.md`
- `CONTROL/01_PRODUCT_DEFINITION.md`
- `CONTROL/02_STAGE_ROADMAP.md`
- `CONTROL/03_PHASE_ACCEPTANCE.md`
- `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`
- `CONTROL/16_CAPABILITY_AUDIT.md`
- `CONTROL/19_STAGE_DASHBOARD.md`
- `CONTROL/20_BLOCKER_LOG.md`
- `CONTROL/23_RUNLOG_PROTOCOL.md`
- `CONTROL/24_CURRENT_STAGE_STATE.md`
- `CONTROL/25_NEXT_ACTION_QUEUE.md`
- `CONTROL/27_CHECKPOINT_LOG.md`
- `RUNLOG/LONG_RUN_CURRENT.md`
- `RUNLOG/LONG_RUN_SUMMARY.md`
- `reviews/stage_00_1/STAGE_ACCEPTANCE_RESULT.md`
- `reviews/stage_00_1/GPT_PRO_REVIEW_RESPONSE.md`
- `reviews/stage_00_1/GPT_PRO_ACTION_ITEMS.md`

## Raw GPT Pro Instruction

```text
/plan
Proceed to Stage 01 planning only.

Before planning, read the control files, RunLog files, Stage 00.1 acceptance result, GPT Pro response, and GPT Pro action items.

Create PLANS/STAGE_01_PLAN.md.

Stage 01 is planning only unless GPT Pro approves the plan.

Do not implement Stage 01 yet.
Do not create runtime files until the plan is approved by GPT Pro.
```
