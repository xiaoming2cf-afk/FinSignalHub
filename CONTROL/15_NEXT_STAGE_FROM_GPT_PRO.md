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

Source stage: Stage 00.

GPT Pro result: PASS after final confirmation.

Important condition: Stage 01 planning may begin. Stage 01 implementation still requires an approved Stage 01 plan and formal Stage 01 goal. Stage 01 cannot pass without Docker Compose validation, CI, GitHub PR, Codex review, GPT Pro review, and Stage 02 instruction evidence.

## Next Stage ID

Stage 01: Repo Scaffold.

## Next Stage Goal

Create the initial FinSignalHub monorepo runtime scaffold without implementing business domain logic.

The scaffold must include:

- FastAPI backend skeleton.
- MCP server skeleton.
- Next.js admin skeleton.
- PostgreSQL service via Docker Compose.
- Redis service placeholder only if justified.
- Basic health checks.
- Test framework.
- CI workflow.
- Environment configuration.
- Project documentation.

Do not implement ResearchProject models, EvidenceItem models, connectors, evidence extraction, claim graph, MCP business tools, Repro Pack logic, Risk Mode, Replay Engine, financial prediction, investment advice, or chatbot UI in Stage 01.

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

- Stage 00 GitHub blockers are resolved or explicitly accepted by the user.
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
- GitHub deployment still blocked.

## Stage 01 Stop Conditions

Stop if Git repo is unavailable, GitHub CLI is unauthenticated without approved manual path, Docker daemon is unavailable, branch/PR/tests cannot be completed, business logic is about to be implemented, GPT Pro cannot be reviewed, secrets are required, or `AGENTS.md` conflicts with latest user instructions.

## Raw GPT Pro Instruction Source

Full initial response and final confirmation are saved at `reviews/stage_00/GPT_PRO_REVIEW_RESPONSE.md`.

## Final GPT Pro Confirmation Summary

GPT Pro answered `PASS for Stage 00 / prompt 1`, stated that there are no Stage 00 must-fix items, authorized Stage 00 to be marked complete, and authorized Stage 01 planning. Deferred items are persistent `gh` authentication, Docker daemon availability for Stage 01, GitHub Actions Node.js runtime changes, and standalone Computer Use automation confirmation.
