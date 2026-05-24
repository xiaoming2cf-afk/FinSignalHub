# 23 RunLog Protocol

## Purpose

Defines the RunLog-driven operating loop for long FinSignalHub sessions so future Codex runs can resume from repository state instead of memory.

## Owner

Codex log keeper and autonomous run coordinator.

## When to update

Update when the long-run loop changes, a new required read source is added, a checkpoint rule changes, or GPT Pro changes the autonomous run protocol.

## Required fields

- Required read set
- Current stage detection rule
- Next action selection rule
- Checkpoint format
- Blocker recording rule
- Resume rule
- Stop rule

## Example format

`Cycle 0001 | read control files | detected Stage 00.1 | selected next action A-00.1-001 | blocker none`

## Current state

Every cycle must begin by reading `AGENTS.md`, `PLANS.md`, `README.md`, `CONTROL/00` through `CONTROL/20`, this RunLog protocol, `CONTROL/24_CURRENT_STAGE_STATE.md`, `CONTROL/25_NEXT_ACTION_QUEUE.md`, `RUNLOG/LONG_RUN_CURRENT.md`, and the active stage `TASKS` and `CHECKLISTS`.

Current stage is determined in this order:

1. Active blocker requiring user action.
2. Open stage branch or PR.
3. `CONTROL/24_CURRENT_STAGE_STATE.md`.
4. `CONTROL/19_STAGE_DASHBOARD.md`.
5. GPT Pro next-stage instruction in `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`.

Next action is selected from `CONTROL/25_NEXT_ACTION_QUEUE.md`; only actions with satisfied dependencies and allowed files may be executed. Completed actions are marked in the queue and summarized in `RUNLOG/LONG_RUN_CURRENT.md`.

Blockers must be recorded in `CONTROL/20_BLOCKER_LOG.md`, `CONTROL/24_CURRENT_STAGE_STATE.md`, and the current RunLog entry before stopping. Resume by reading the same files and selecting the first unblocked queued action.

Stop safely on login, MFA, permission, payment, secret, destructive Git operation, product drift, missing GitHub access, GPT Pro FAIL requiring user decision, or Docker unavailability when the active stage depends on Docker.
