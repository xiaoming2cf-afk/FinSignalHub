---
name: subagent-coordinator
description: Define and integrate bounded subagent work for FinSignalHub stages.
---

# Subagent Coordinator

## When to use

Use when a stage plan or user explicitly requests subagents.

## Procedure

1. Define each subagent name, responsibility, allowed files, forbidden files, and output format.
2. Avoid overlapping write scopes.
3. Require subagent output under `logs/subagents/stage_XX/<agent_name>.md`.
4. Integrate results into `reviews/stage_XX/SUBAGENT_SUMMARY.md`.
5. Resolve conflicts through the integration owner, not by broad rewrites.

## Required outputs

- Subagent scope list.
- Subagent log files.
- Stage subagent summary.

## Failure conditions

- Subagent edits broad repository scope without boundaries.
- Subagent results are not summarized for review.
