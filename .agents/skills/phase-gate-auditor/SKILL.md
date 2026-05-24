---
name: phase-gate-auditor
description: Audit FinSignalHub stages against the ten hard phase gates.
---

# Phase Gate Auditor

## When to use

Use before any stage is declared complete, before PR merge, and after GPT Pro review.

## Procedure

1. Read `CONTROL/03_PHASE_ACCEPTANCE.md`.
2. Check the ten gates: scope, functionality, tests, docs, logs, GitHub, GPT Pro, product governance, security, next stage.
3. Verify evidence paths exist and are not empty placeholders.
4. Mark each gate PASS, FAIL, or BLOCKED.
5. Write the result to `reviews/stage_XX/STAGE_ACCEPTANCE_RESULT.md`.

## Required outputs

- Gate table with evidence path and result.
- Final stage result: PASS, FAIL, or BLOCKED.
- Blocker entries for missing hard-gate evidence.

## Failure conditions

- GitHub or GPT Pro evidence is missing but the stage is marked complete.
- Any gate is assumed passed without evidence.
