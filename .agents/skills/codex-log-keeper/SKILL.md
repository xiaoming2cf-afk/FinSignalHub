---
name: codex-log-keeper
description: Maintain FinSignalHub execution, goal, artifact, blocker, decision, and changelog records.
---

# Codex Log Keeper

## When to use

Use during every stage execution and before ending a work session.

## Procedure

1. Append execution details to `CONTROL/04_EXECUTION_LOG.md`.
2. Update current goal in `CONTROL/07_CODEX_GOAL_REGISTRY.md`.
3. Register artifacts in `CONTROL/18_ARTIFACT_REGISTRY.md`.
4. Add blockers to `CONTROL/20_BLOCKER_LOG.md`.
5. Add ADRs to `CONTROL/05_DECISION_LOG.md` when decisions change.
6. Update `CHANGELOG.md` only for user-visible changes.

## Required outputs

- Current execution log entry.
- Updated goal status.
- Registered artifacts.
- Blocker entries when gates cannot pass.

## Failure conditions

- A stage ends without updated logs.
- User-visible changes are omitted from changelog.
