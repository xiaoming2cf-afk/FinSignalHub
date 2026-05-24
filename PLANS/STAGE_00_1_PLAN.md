# Stage 00.1 Plan: RunLog Governance Cleanup

## Context read

Read `AGENTS.md`, `PLANS.md`, Stage 00 control files, Stage 00 acceptance artifacts, Stage 01 task/checklist files, and the user-provided run instruction file at `运行要求/FinSignalHub_Codex_RunLog_Autonomous_Prompt.md`.

## Capability check

GitHub CLI is available as active account `xiaoming2cf-afk`. GitHub Actions and `@codex review` are available. Chrome/GPT Pro review is required for final acceptance. Docker CLI exists but the daemon is currently unavailable; this blocks Stage 01 implementation only, not Stage 00.1.

## Product alignment check

Stage 00.1 is governance-only. It strengthens evidence-stream project control and does not implement chatbot, RAG, financial prediction, investment advice, dashboard product behavior, connectors, backend runtime, database, frontend, or MCP business tools.

## Scope

Create RunLog control files, plugin helper scripts, Stage 00.1 review artifacts, and updated registries so long autonomous runs can resume safely from repository state.

## Files to create or modify

RunLog controls, `RUNLOG/`, plugin helper scripts/templates, Stage 00.1 review and deployment artifacts, control logs/registries, release checklist, dashboard, blocker log, and the user-provided `运行要求/` input artifact.

## Files not to touch

No `apps/`, `docker-compose.yml`, `pyproject.toml`, `package.json`, backend, database, connector, frontend, MCP runtime, or business logic files in Stage 00.1.

## Skills

Use `finsignal-product-governor`, `phase-gate-auditor`, `codex-log-keeper`, `github-stage-deployer`, `gpt-pro-review-preparer`, `browser-gpt-pro-reviewer`, `github-review-resolver`, `acceptance-evidence-collector`, and `stage-next-goal-synthesizer`.

## Subagents

No write subagents are required for Stage 00.1. A read-only verification subagent may be used before final acceptance if additional independent audit is useful.

## Implementation steps

1. Create branch `stage/00-1-governance-cleanup`.
2. Add RunLog control files and current/summary logs.
3. Add plugin helper scripts and PR body template.
4. Add Stage 00.1 review packet, PR body, acceptance result, and deployment evidence.
5. Update control logs, artifact registry, dashboard, release checklist, blocker log, and subagent summary.
6. Run local governance checks.
7. Commit, push, create PR, request `@codex review`, wait for CI and Codex.
8. Submit GPT Pro packet and save response/action items.
9. Update acceptance gates and only mark PASS if evidence exists.

## Tests

### Local checks

Run control heading checks, skill section checks, Stage 00.1 artifact existence checks, plugin helper syntax checks, `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 00_1`, Stage 01 missing-plan rejection, recursive forbidden business/runtime path check, RunLog cycle order check, secret-pattern scan, and `git diff --check`.

### Unit tests

Stage 00.1 has no product runtime units because it is governance-only. The unit-test equivalent is helper-script syntax validation plus targeted helper behavior checks for stage normalization, missing artifact failure, RunLog append cycle numbering, repository-relative path rejection, traversal-segment rejection, and recursive forbidden runtime scaffold detection. Product unit tests begin only after an approved Stage 01 scaffold plan creates testable runtime skeletons.

### Integration tests

Stage 00.1 has no backend, database, frontend, MCP server, connector, or Docker integration surface. Integration testing is therefore deferred by design until Stage 01 and later. The integration-equivalent checks for this stage are GitHub Actions governance CI, PR creation, `@codex review`, and GPT Pro review packet submission.

### Acceptance checks

Acceptance requires the ten gates in `reviews/stage_00_1/STAGE_ACCEPTANCE_RESULT.md`: scope, functionality, tests, docs, logs, GitHub, GPT Pro, product governance, security, and next stage. Gate 6 requires branch, PR, CI, Codex review, and PR URL. Gate 7 requires GPT Pro packet, response, action items, final result, and next-stage instruction or an explicit blocker.

## Docs

RunLog files must explain how later Codex sessions resume, select actions, record blockers, and stop safely. `运行要求/README.md` must explain the committed prompt source.

## GitHub deployment

Create PR from `stage/00-1-governance-cleanup`, use `reviews/stage_00_1/PR_BODY.md`, request the required `@codex review`, record PR URL, CI, and Codex response in `deployments/stage_00_1/GITHUB_PR.md`.

## GPT Pro review

Submit `reviews/stage_00_1/GPT_PRO_REVIEW_PACKET.md` to the specified GPT Pro page using Chrome. Save response and action items. Stop on login/MFA/permission/secret/payment prompts.

## Risks

Docker is unavailable for later Stage 01 implementation. Stage 00.1 could accidentally become a scaffolding stage; guard by rejecting runtime/product files. GPT Pro or GitHub may be unavailable; record blockers if so.

## Stop conditions

Stop on product drift, missing GitHub permission, GPT Pro access blockers, secret requests, destructive Git operation, or Docker unavailability when Stage 01 implementation is about to begin.
