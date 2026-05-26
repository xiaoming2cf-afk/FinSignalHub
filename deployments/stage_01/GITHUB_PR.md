# Stage 01 GitHub PR

## Status

Open.

## Branch

`stage/01-repo-scaffold`

## Base decision

This branch was created from `stage/00-1-governance-cleanup` because PR #6 had not been merged when GPT Pro authorized Stage 01 planning only.

Implementation PR must either:

- wait for PR #6 to merge into `main`, or
- use `stage/00-1-governance-cleanup` as the base and record the dependency.

## PR URL

https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7

## CI

PASS:

- https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26372845227/job/77627949148
- https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26372846543/job/77627952398
- https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26434920535/job/77815447973
- https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26434922256/job/77815453096

## Codex Review

Requested at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#issuecomment-4529857254.

Current findings:

- CR-01-001 P1: replace Windows-only `npm.cmd` in Stage 01 plan commands with cross-platform `npm`.
- CR-01-002 P2: update `CONTROL/24_CURRENT_STAGE_STATE.md` after planning checks passed.
- CR-01-003 P2: remove remaining Windows-only `npm.cmd` guidance from Stage 01 capability table.
- CR-01-004 P2: update `CHECKLISTS/STAGE_01_CHECKLIST.md` after GPT Pro plan PASS and PR #7 status changed.
- CR-01-005 P1: sanitize `artifacts/chrome_gpt_stage_01_plan_clipboard.txt` to remove unrelated browser sidebar/account context.
- CR-01-006 P2: update `CONTROL/24_CURRENT_STAGE_STATE.md` after latest Stage 01 checks.
- CR-01-007 P2: mark Stage 01 plan artifacts as reviewed in `CONTROL/18_ARTIFACT_REGISTRY.md`.
- CR-01-008 P2: refresh `CONTROL/24_CURRENT_STAGE_STATE.md` after latest check-pass checkpoint so it points to commit/push/follow-up, not stale checks.
- CR-01-009 P2: mark Stage 01 checklist scope gate as passed for plan review.
- CR-01-010 P2: refresh `CONTROL/07_CODEX_GOAL_REGISTRY.md` G-0002 to latest follow-up state.
- CR-01-011 P3: remove duplicated milestone in `RUNLOG/LONG_RUN_SUMMARY.md`.
- CR-01-012 P2: align `CONTROL/19_STAGE_DASHBOARD.md` with the latest Stage 01 finding set.
- CR-01-013 P2: mark the completed planning security scan as passed in `CHECKLISTS/STAGE_01_CHECKLIST.md`.
- CR-01-014 P2: include explicit user implementation approval and PR #6 baseline handling in the Stage 01 functionality blocker set.
- CR-01-015 P1: remove stale hardcoded current-head wording from Stage 01 gate/status records.
- CR-01-016 P2: update GPT Pro action items after Docker daemon validation and defer only `docker compose config` until the approved compose file exists.
- CR-01-017 P2: keep Docker readiness BLOCKED/PENDING until `docker compose config` passes on an approved `docker-compose.yml`.
- CR-01-018 P2: update this PR evidence file to include CR-01-015 through CR-01-017.
- CR-01-019 P2: add the Docker compose-config gate to the PR body unblock criteria.
- CR-01-020 P1: enforce GPT Pro's pre-implementation `docker compose config` condition by blocking implementation until GPT Pro/user resolves the ordering conflict.
- CR-01-021 P2: include the compose-ordering blocker in the Stage 01 Codex current-state summary.
- CR-01-022 P2: include the compose-ordering blocker in `RUNLOG/LONG_RUN_SUMMARY.md`.
- CR-01-023 P2: mark Stage 01 checklist GitHub gate as current-head CI/Codex pending after each new push.

All known findings through CR-01-023 are addressed locally in the Stage 01 planning and governance artifacts. The GitHub gate remains blocked/pending until current-head CI and Codex follow-up return no-major-issues evidence after this update.
