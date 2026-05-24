# Stage 01 Plan: Repo Scaffold

## Context read

Read `AGENTS.md`, `PLANS.md`, `README.md`, `CONTROL/00_MASTER_CONTROL.md`, `CONTROL/01_PRODUCT_DEFINITION.md`, `CONTROL/02_STAGE_ROADMAP.md`, `CONTROL/03_PHASE_ACCEPTANCE.md`, `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`, `CONTROL/16_CAPABILITY_AUDIT.md`, `CONTROL/19_STAGE_DASHBOARD.md`, `CONTROL/20_BLOCKER_LOG.md`, `CONTROL/23_RUNLOG_PROTOCOL.md`, `CONTROL/24_CURRENT_STAGE_STATE.md`, `CONTROL/25_NEXT_ACTION_QUEUE.md`, `CONTROL/27_CHECKPOINT_LOG.md`, `RUNLOG/LONG_RUN_CURRENT.md`, `RUNLOG/LONG_RUN_SUMMARY.md`, `reviews/stage_00_1/STAGE_ACCEPTANCE_RESULT.md`, `reviews/stage_00_1/GPT_PRO_REVIEW_RESPONSE.md`, and `reviews/stage_00_1/GPT_PRO_ACTION_ITEMS.md`.

Stage 00.1 GPT Pro result is PASS. It authorizes Stage 01 planning only. Stage 01 implementation remains blocked until this plan is approved by GPT Pro and the user, Docker daemon is revalidated, PR #6 is merged or Stage 01 remains based on `stage/00-1-governance-cleanup`, and no Stage 01 blocker remains.

## Capability check

| Capability | Stage 01 planning status | Stage 01 implementation status |
| --- | --- | --- |
| Git | available; branch `stage/01-repo-scaffold` created from Stage 00.1 head | available after PR/base decision |
| GitHub CLI | available as `xiaoming2cf-afk` | available |
| GitHub Actions | available; PR #6 governance CI passed | must run on Stage 01 PR |
| Codex review | available; PR #6 current head received no-major response | required for Stage 01 PR |
| Chrome/GPT Pro | available after prior successful Stage 00.1 review | required for Stage 01 plan review and final review |
| Docker | unavailable at planning time: daemon not reachable at `npipe:////./pipe/dockerDesktopLinuxEngine` | blocks implementation until Docker Desktop is running and validation passes |
| Python | available | required for FastAPI/MCP skeleton tests |
| Node/npm | available through `npm.cmd` | required for admin skeleton build |

## Product alignment check

Stage 01 creates only an engineering scaffold so later Research Mode MVP work can expose MCP-first evidence-stream workflows. It must not introduce research domain behavior, chatbot behavior, generic RAG, financial prediction, investment advice, dashboard product features, model leaderboard, Risk Mode, Replay Engine, connectors, evidence extraction, claim graph logic, Research Delta logic, Literature Matrix logic, MethodCard, DatasetCard, Repro Pack logic, or MCP business tools.

Every visible placeholder must describe FinSignalHub as Research Mode-first, MCP-first, evidence-stream oriented, and scaffold-only.

## Scope

Create a minimal monorepo runtime scaffold after plan approval:

- FastAPI backend skeleton with `/health` only.
- MCP server skeleton with health/server-info only.
- Next.js admin skeleton with scaffold status only.
- Docker Compose with Postgres plus API, MCP server, and web admin services.
- Python and JavaScript package roots.
- Minimal tests and CI for scaffold health/build checks.
- Stage 01 docs, logs, review artifacts, deployment evidence, and acceptance evidence.

## Files to create or modify

Planning phase only:

- `PLANS/STAGE_01_PLAN.md`
- `TASKS/STAGE_01_TASKS.md`
- `CHECKLISTS/STAGE_01_CHECKLIST.md`
- `reviews/stage_01/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_01/PR_BODY.md`
- `reviews/stage_01/STAGE_ACCEPTANCE_RESULT.md`
- `deployments/stage_01/GITHUB_PR.md`
- `CONTROL/04_EXECUTION_LOG.md`
- `CONTROL/07_CODEX_GOAL_REGISTRY.md`
- `CONTROL/18_ARTIFACT_REGISTRY.md`
- `CONTROL/19_STAGE_DASHBOARD.md`
- `CONTROL/20_BLOCKER_LOG.md`
- `CONTROL/24_CURRENT_STAGE_STATE.md`
- `CONTROL/25_NEXT_ACTION_QUEUE.md`
- `CONTROL/27_CHECKPOINT_LOG.md`
- `RUNLOG/LONG_RUN_CURRENT.md`
- `RUNLOG/LONG_RUN_SUMMARY.md`

Implementation phase, only after GPT Pro and user approval:

- `docker-compose.yml`
- `pyproject.toml`
- `package.json`
- `apps/api/`
- `apps/mcp_server/`
- `apps/web_admin/`
- `docs/architecture/stage_01_repo_scaffold.md`
- `docs/codex/stage_01_commands.md`
- `.github/workflows/ci.yml`
- `.github/workflows/phase-deploy.yml`

## Files not to touch

Do not create or modify domain models, product migrations, connector implementations, LLM adapters, extraction pipelines, claim graph logic, research delta logic, literature matrix logic, method cards, dataset cards, Repro Pack export logic, Risk Mode, Replay Engine, stock prediction, investment advice, chatbot UI, production auth, billing, or any product runtime beyond health/server-info scaffold.

Do not create Stage 02+ files.

## Skills

Use:

- `finsignal-product-governor`
- `subagent-coordinator`
- `phase-gate-auditor`
- `codex-log-keeper`
- `github-stage-deployer`
- `gpt-pro-review-preparer`
- `browser-gpt-pro-reviewer`
- `github-review-resolver`
- `acceptance-evidence-collector`
- `ai-capability-radar`

## Subagents

Declare these subagents for the implementation phase only after GPT Pro approves this plan:

| Subagent | Responsibility | Allowed files | Forbidden files | Output |
| --- | --- | --- | --- | --- |
| backend-scaffold-agent | FastAPI skeleton, `/health`, API tests | `apps/api/`, `pyproject.toml` | domain models, migrations, product services | `logs/subagents/stage_01/backend-scaffold-agent.md` |
| mcp-scaffold-agent | MCP health/server-info skeleton only | `apps/mcp_server/` | Research Mode business tools | `logs/subagents/stage_01/mcp-scaffold-agent.md` |
| web-admin-scaffold-agent | Next.js scaffold status page only | `apps/web_admin/`, `package.json` | dashboard product behavior, chatbot UI | `logs/subagents/stage_01/web-admin-scaffold-agent.md` |
| docker-ci-agent | Docker Compose and CI checks | `docker-compose.yml`, `.github/workflows/` | product service logic | `logs/subagents/stage_01/docker-ci-agent.md` |
| docs-log-agent | Stage 01 docs, logs, review artifacts | `docs/`, `reviews/stage_01/`, `CONTROL/`, `RUNLOG/`, `deployments/stage_01/` | runtime code except docs snippets | `logs/subagents/stage_01/docs-log-agent.md` |
| browser-smoke-agent | Browser smoke evidence for local scaffold | `logs/subagents/stage_01/browser-smoke-agent.md`, `artifacts/stage_01/` | Chrome/GPT Pro pages | browser smoke log |

Integration owner: Codex main agent. Subagent outputs must be summarized in `reviews/stage_01/SUBAGENT_SUMMARY.md`.

## Implementation steps

Planning steps now:

1. Create this plan and Stage 01 review packet.
2. Submit the plan packet to GPT Pro.
3. Save GPT Pro plan response and action items.
4. Stop before implementation if GPT Pro does not approve the plan or Docker remains unavailable.

Implementation steps later, only after approval:

1. Revalidate Docker daemon and record result.
2. Confirm PR #6 is merged or document Stage 01 base dependency.
3. Create scaffold files only.
4. Run local scaffold checks.
5. Update docs and logs.
6. Push branch, create PR, request `@codex review`, wait for CI, and fix critical findings.
7. Submit Stage 01 final review packet to GPT Pro.
8. Save response/action items and request Stage 02 instructions only after PASS.

## Tests

### Local checks

Planning phase local checks:

- Verify no runtime files are created.
- Verify `PLANS/STAGE_01_PLAN.md` exists.
- Verify Stage 01 review packet exists.
- Verify Docker status is recorded as implementation blocker if unavailable.
- Run secret-pattern scan and `git diff --check`.

### Unit tests

Implementation phase unit tests, only after plan approval:

- API health unit test.
- MCP health/server-info unit test.
- Web admin build or component smoke test.

### Integration tests

Implementation phase integration tests, only after plan approval and Docker validation:

```text
docker compose config
docker compose up --build
curl http://localhost:8000/health
pytest apps/api/tests
pytest apps/mcp_server/tests
npm --prefix apps/web_admin run build
```

Browser smoke must verify the admin scaffold page only after local web runtime exists.

### Acceptance checks

Stage 01 final acceptance requires the ten gates in `reviews/stage_01/STAGE_ACCEPTANCE_RESULT.md`, including scaffold-only scope, CI, Codex review, GPT Pro final review, and GPT Pro Stage 02 instruction.

## Docs

Document scaffold boundaries in `docs/architecture/stage_01_repo_scaffold.md` and command usage in `docs/codex/stage_01_commands.md` during implementation. Planning artifacts must state no business code has been created.

## GitHub deployment

Stage 01 branch: `stage/01-repo-scaffold`.

If PR #6 is not merged, Stage 01 PR should be based on `stage/00-1-governance-cleanup` or the dependency must be logged. Do not open a Stage 01 implementation PR against `main` unless Stage 00.1 has been merged.

Commit format: `stage-01: summary`.

PR title: `Stage 01: Repo Scaffold`.

PR body source: `reviews/stage_01/PR_BODY.md`.

## GPT Pro review

Submit `reviews/stage_01/GPT_PRO_REVIEW_PACKET.md` as a plan review before implementation. GPT Pro must answer PASS, CONDITIONAL PASS, or FAIL for the plan. Stage 01 implementation cannot start on FAIL or unresolved critical CONDITIONAL PASS items.

## Risks

- Docker daemon remains unavailable and blocks implementation.
- PR #6 remains open and Stage 01 starts from the wrong baseline.
- Scaffold grows into product behavior.
- MCP skeleton grows into Research Mode tools too early.
- Web admin grows into a dashboard or chatbot.
- Package setup creates framework lock-in before domain boundaries are approved.

## Stop conditions

Stop before implementation if Docker daemon is unavailable, GPT Pro does not approve the plan, user approval is missing, PR #6 baseline is unresolved, secrets are requested, product behavior appears, or any file outside the Stage 01 boundary is needed.
