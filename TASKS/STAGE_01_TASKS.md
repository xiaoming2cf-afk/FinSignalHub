# Stage 01 Tasks: Repo Scaffold

## Stage goal

Create the minimal FinSignalHub repo scaffold only after GPT Pro approves `PLANS/STAGE_01_PLAN.md` and the user approves implementation.

## User needs

Researchers need a stable, reproducible project foundation before Research Mode domain behavior is added. The scaffold must support later MCP-first evidence-stream work without introducing business logic early.

## Files allowed

Planning files:

- `PLANS/STAGE_01_PLAN.md`
- `reviews/stage_01/`
- `deployments/stage_01/`
- Stage logs and registries.

Implementation files after approval:

- `docker-compose.yml`
- `pyproject.toml`
- `package.json`
- `apps/api/`
- `apps/mcp_server/`
- `apps/web_admin/`
- Stage 01 docs and CI updates.

## Files forbidden

ResearchProject, EvidenceItem, ResearchClaim, ClaimEvidenceEdge, ResearchDelta, LiteratureMatrix, MethodCard, DatasetCard, ReproPackExport, ToolCallLog, product migrations, connectors, extraction, claim graph, MCP business tools, Repro Pack behavior, Risk Mode, Replay Engine, demos, chatbot UI, generic RAG, stock prediction, investment advice, and dashboard product behavior.

## Skills required

`finsignal-product-governor`, `subagent-coordinator`, `phase-gate-auditor`, `codex-log-keeper`, `github-stage-deployer`, `gpt-pro-review-preparer`, `browser-gpt-pro-reviewer`, `github-review-resolver`, `acceptance-evidence-collector`, and `ai-capability-radar`.

## Subagents required

Implementation subagents are declared in `PLANS/STAGE_01_PLAN.md`: backend-scaffold-agent, mcp-scaffold-agent, web-admin-scaffold-agent, docker-ci-agent, docs-log-agent, and browser-smoke-agent. They must not run until GPT Pro approves the plan and the user approves implementation.

## Implementation tasks

Planning tasks:

1. Create Stage 01 plan.
2. Create Stage 01 GPT Pro plan review packet.
3. Submit plan packet to GPT Pro.
4. Save response and action items.
5. Stop before implementation if Docker environment checks fail, user approval is missing, or PR #6 baseline handling is unresolved.

Implementation tasks after approval:

1. Confirm PR #6 is merged, or explicitly log that Stage 01 remains based on `stage/00-1-governance-cleanup` before creating any implementation artifact.
2. Revalidate Docker environment with `docker info`, `docker version`, and `docker compose version`.
3. Create minimal `docker-compose.yml` as the first approved implementation-preflight artifact only after the baseline condition is handled.
4. Immediately run `docker compose config`; if it fails, stop and record a blocker before creating further scaffold.
5. Create remaining scaffold files only after compose config passes.
6. Run scaffold tests.
7. Update docs/logs/review artifacts.
8. Open PR, request Codex review, submit final GPT Pro review.

## Test tasks

Planning: no runtime file check, secret scan, `git diff --check`.

Implementation: first-step `docker compose config`, then `docker compose up --build`, API `/health`, MCP health/server-info, web build, API/MCP tests, browser smoke.

## Docs tasks

Document scaffold boundaries, commands, and no-business-logic rule.

## GitHub deployment tasks

Use branch `stage/01-repo-scaffold`. If PR #6 is not merged, base the Stage 01 PR on `stage/00-1-governance-cleanup` or log the dependency. PR body must come from `reviews/stage_01/PR_BODY.md`.

## GPT Pro review tasks

Submit Stage 01 plan packet before implementation. Submit final Stage 01 implementation packet only after scaffold checks and Codex review pass. Request Stage 02 instructions only after final PASS.

## Stop conditions

Stop if scaffold adds product behavior, Docker environment checks fail before implementation, first-step `docker compose config` fails after implementation approval, GPT Pro plan approval is missing, user approval is missing, PR #6 baseline is unresolved, secrets are requested, or Stage 00.1 gates are bypassed.
