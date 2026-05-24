# 00 Master Control

## Purpose

Central index for FinSignalHub governance. This file tells Codex which control records to read before planning or executing a stage.

## Owner

Codex acting as FinSignalHub engineering lead, product process lead, and phase acceptance lead.

## When to update

Update at the start and end of every stage, whenever a control file is added, or when user instructions change the operating system.

## Required fields

- Stage id
- Current stage status
- Required control files
- Hard gates
- Latest blocker summary
- Latest GPT Pro instruction source

## Example format

`Stage 00 | active | hard gates: GitHub, GPT Pro | blockers: gh unauthenticated, no repo | next source: pending GPT Pro`

## Current state

Stage 00 is PASS / COMPLETE. FinSignalHub remains locked to Research Mode-first, MCP-first, evidence-stream oriented governance. Stage 00 established the control system, capability audit, local skills, local plugin draft, GitHub/Codex review loop, GPT Pro review loop, stage task/checklist system, and acceptance evidence without implementing business runtime, backend, database, connectors, frontend, or MCP tools.

Stage 01 planning is allowed only because GPT Pro authorized it after Stage 00 PASS. Stage 01 implementation is still forbidden until a Stage 01 plan is written, the user approves it, and a formal Stage 01 goal is started.

Required read order for future stages:

1. `AGENTS.md`
2. `PLANS.md`
3. `CONTROL/00_MASTER_CONTROL.md`
4. `CONTROL/01_PRODUCT_DEFINITION.md`
5. `CONTROL/02_STAGE_ROADMAP.md`
6. `CONTROL/03_PHASE_ACCEPTANCE.md`
7. `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`
8. Current stage plan, tasks, checklist, and blockers
