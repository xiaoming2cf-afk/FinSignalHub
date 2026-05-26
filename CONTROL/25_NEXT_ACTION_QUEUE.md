# 25 Next Action Queue

## Purpose

Maintains the ordered action queue for long-running FinSignalHub work.

## Owner

Autonomous run coordinator.

## When to update

Update when an action is created, started, completed, blocked, superseded, or assigned to a subagent.

## Required fields

- Action ID
- Stage
- Action
- Dependency
- Allowed files
- Required skills
- Required subagents
- Expected artifacts
- Done condition
- Status

## Example format

`A-00.1-001 | Stage 00.1 | create RunLog files | branch exists | CONTROL/23-27, RUNLOG | codex-log-keeper | none | files created | done`

## Current state

| Action ID | Stage | Action | Dependency | Allowed files | Required skills | Required subagents | Expected artifacts | Done condition | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-00.1-001 | 00.1 | Create RunLog protocol and state files | branch created | `CONTROL/23`-`27`, `RUNLOG/` | codex-log-keeper, phase-gate-auditor | none | RunLog control files | required files exist and pass heading checks | done |
| A-00.1-002 | 00.1 | Add plugin helper templates and scripts | A-00.1-001 | `finsignalhub-codex-plugin/templates/`, `finsignalhub-codex-plugin/scripts/` | gpt-pro-review-preparer, github-stage-deployer | none | helper files | scripts/templates exist and are project-specific | done |
| A-00.1-003 | 00.1 | Create Stage 00.1 review artifacts | A-00.1-002 | `reviews/stage_00_1/`, `deployments/stage_00_1/` | gpt-pro-review-preparer, acceptance-evidence-collector | none | packet, PR body, acceptance result | artifacts are non-empty | done |
| A-00.1-004 | 00.1 | Run local governance checks and open PR | A-00.1-003 | governance files only | github-stage-deployer, github-review-resolver | none | PR URL, CI status, Codex review | CI passes and Codex responds with no major issues | done; final no-major response saved externally |
| A-00.1-005 | 00.1 | Submit GPT Pro review and close Stage 00.1 | A-00.1-004 | `reviews/stage_00_1/`, `CONTROL/15`, logs | browser-gpt-pro-reviewer, stage-next-goal-synthesizer, phase-gate-auditor | none | GPT response, action items, final gate result | GPT Pro PASS or documented blocker | done |
| A-01-001 | 01 | Draft Stage 01 plan | Stage 00.1 PASS plus current-head Codex no-major evidence | `PLANS/STAGE_01_PLAN.md`, `reviews/stage_01/` | finsignal-product-governor, gpt-pro-review-preparer | planning subagents only if needed | Stage 01 plan packet | GPT Pro plan review packet ready | done; GPT Pro plan PASS saved |
| A-01-002 | 01 | Recheck Docker before implementation | Stage 01 plan approved by GPT Pro and user | capability logs | ai-capability-radar, codex-log-keeper | none | Docker check evidence | Docker daemon reachable; `docker info`, `docker version`, and `docker compose version` pass; `docker compose config` runs as first implementation-preflight after approval | environment gate done; implementation-preflight compose config pending after approval |
| A-01-003 | 01 | Resolve PR #7 Codex plan findings | A-01-001 | Stage 01 planning and governance files only | github-review-resolver, codex-log-keeper | none | follow-up Codex no-major response or documented blocker | all known findings through CR-01-036 and GPT Pro Docker ordering updates fixed locally; current-head CI and Codex follow-up/no-major evidence captured after push | blocked/pending until next pushed PR head receives CI PASS and fresh no-major response |
| A-01-004 | 01 | Handle remaining implementation gates | A-01-002 and A-01-003 | control logs, PR baseline docs | phase-gate-auditor, codex-log-keeper | none | user approval record; PR #6 baseline decision; implementation-preflight compose config result after approval | explicit user implementation approval and PR #6 baseline handling complete; first implementation step runs `docker compose config` | blocked: user approval and PR #6 baseline pending |
