---
name: stage-next-goal-synthesizer
description: Convert GPT Pro next-stage instructions into FinSignalHub plan and goal inputs.
---

# Stage Next Goal Synthesizer

## When to use

Use after GPT Pro passes a stage and provides next-stage instructions.

## Procedure

1. Copy raw GPT Pro instruction into `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`.
2. Extract next stage goal, files, acceptance criteria, risks, and stop conditions.
3. Create the next stage goal registry entry only after the current stage gate is resolved.
4. Do not invent next-stage scope without GPT Pro source.

## Required outputs

- Updated next-stage instruction file.
- Draft next-stage goal registry entry.
- Plan inputs for the next `/plan`.

## Failure conditions

- Stage starts from assumed next steps instead of GPT Pro instruction.
