# Stage 02 Tasks: Research Mode Domain Models

## Stage goal

Plan and later create Research Mode domain models only after Stage 01 passes, GPT Pro approves the Stage 02 plan, and the user approves the Stage 02 goal.

## User needs

Researchers need structured records for projects, evidence, claims, edges, deltas, matrices, cards, exports, and tool logs.

## Files allowed

Planning files now allowed:

- `PLANS/STAGE_02_PLAN.md`
- `TASKS/STAGE_02_TASKS.md`
- `CHECKLISTS/STAGE_02_CHECKLIST.md`
- `reviews/stage_02/`
- `deployments/stage_02/`
- `logs/subagents/stage_02/`
- Required control, artifact, checkpoint, and RunLog records.

Implementation files are allowed only after GPT Pro plan review and user `/goal` approval:

- `apps/api/finsignalhub_api/db/`
- `apps/api/finsignalhub_api/models/`
- `apps/api/finsignalhub_api/schemas/`
- `apps/api/finsignalhub_api/services/`
- `apps/api/finsignalhub_api/routers/`
- `apps/api/finsignalhub_api/core/`
- `apps/api/tests/`
- `apps/api/alembic/`
- `apps/api/alembic.ini`
- `docs/architecture/stage_02_domain_models.md`
- `docs/codex/stage_02_commands.md`

## Files forbidden

During planning, all implementation files are forbidden.

During later implementation, still forbidden:

- Connectors.
- External API calls.
- LLM adapters.
- Evidence extraction.
- Claim graph computation.
- Research delta computation beyond tables/schemas.
- Repro Pack export logic.
- MCP business tools.
- Admin UI product features.
- Demos.
- Risk Mode, Replay Engine, stock prediction, investment advice, chatbot UI, generic RAG, and dashboard product behavior.

## Skills required

`finsignal-product-governor`, `evidence-graph-architect`, `phase-gate-auditor`, `codex-log-keeper`, `gpt-pro-review-preparer`, `browser-gpt-pro-reviewer`, `github-stage-deployer`, `github-review-resolver`, `subagent-coordinator`, `acceptance-evidence-collector`.

## Subagents required

Required in implementation plan: schema-agent, migration-agent, api-schema-agent, test-agent, docs-log-agent.

## Implementation tasks

Planning tasks:

1. Write `PLANS/STAGE_02_PLAN.md` from GPT Pro Stage 01 final instruction.
2. Update this task file and the Stage 02 checklist.
3. Create Stage 02 PR body, acceptance placeholder, deployment placeholder, and GPT Pro plan review packet.
4. Update logs and artifact registry.
5. Run planning-only checks and confirm no implementation files were created.
6. Open PR and request Codex review.
7. Submit plan packet to GPT Pro.

Later implementation tasks require GPT Pro plan PASS and user `/goal` approval.

## Test tasks

Planning-only checks:

- `phase_check.py --stage 02`
- no Stage 02 implementation file check
- secret scan
- forbidden scope scan
- `git diff --check`

Later implementation tests must include model, migration, schema, and CRUD tests.

## Docs tasks

Document model boundaries, provenance fields, forbidden logic, migration commands, and stage stop conditions.

## GitHub deployment tasks

Use branch `stage/02-domain-models`, PR, CI, and Codex review. PR body must come from `reviews/stage_02/PR_BODY.md`.

## GPT Pro review tasks

Planning: submit Stage 02 plan packet and ask whether implementation may begin after user `/goal` approval.

Implementation: submit final Stage 02 implementation packet and request Stage 03 instructions only after CI/Codex pass.

## Stop conditions

Stop if models support investment advice, generic RAG, unprovenanced claims, external data APIs, real LLM API keys, auth/billing, destructive Stage 01 changes, or Stage 03+ behavior.
