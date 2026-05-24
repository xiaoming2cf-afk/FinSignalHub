# 27 Checkpoint Log

## Purpose

Records durable checkpoints for RunLog-driven work.

## Owner

Codex log keeper.

## When to update

Update after every plan, goal start, subagent result, test run, commit, PR creation, Codex review result, GPT Pro response, blocker change, and phase-gate-auditor result.

## Required fields

- Checkpoint ID
- Timestamp
- Stage
- Event
- Files changed
- Commands or tools
- Result
- Next action

## Example format

`CP-0001 | 2026-05-24T11:41:00-05:00 | 00.1 | branch created | none | git switch -c | pass | create RunLog files`

## Current state

| Checkpoint ID | Timestamp | Stage | Event | Files changed | Commands or tools | Result | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP-0001 | 2026-05-24T11:41:00-05:00 | 00.1 | RunLog-driven plan execution started | none yet | read approved plan; `git switch -c stage/00-1-governance-cleanup` | branch active | create RunLog files and helper artifacts |
| CP-0002 | 2026-05-24T11:45:52-05:00 | 00.1 | Local governance checks passed | RunLog controls, helper scripts, review artifacts, logs | control heading check; phase_check.py; py_compile; artifact existence; skill check; forbidden path check; secret scan; git diff check | pass | commit, push, create PR |
