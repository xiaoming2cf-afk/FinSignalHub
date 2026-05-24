# Stage 01 Tasks: Repo Scaffold

## Stage goal

Create infrastructure skeleton only after GPT Pro gives Stage 01 instructions.

## User needs

Researchers need a stable project foundation before domain behavior is added.

## Files allowed

To be defined in Stage 01 plan. Expected: monorepo config, FastAPI skeleton, MCP server skeleton, Next.js admin skeleton, Docker Compose, PostgreSQL config, CI, health checks.

## Files forbidden

Domain models, connectors, extraction, claim graph, MCP tool behavior, and demos.

## Skills required

`phase-gate-auditor`, `github-stage-deployer`, `codex-log-keeper`, `finsignal-product-governor`.

## Subagents required

Plan must decide. No default subagent execution before GPT Pro instruction.

## Implementation tasks

To be filled after GPT Pro Stage 01 instruction. Trigger: `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md` receives Stage 01 goal.

## Test tasks

Health checks and scaffold checks only.

## Docs tasks

Document scaffold boundaries and no business logic.

## GitHub deployment tasks

Use branch `stage/01-repo-scaffold`, PR, CI, Codex review.

## GPT Pro review tasks

Submit Stage 01 packet and request Stage 02 instructions.

## Stop conditions

Stop if scaffold adds product behavior or bypasses Stage 00 gates.
