# Stage 05 Tasks: Claim Graph and Research Delta Planning

## Stage goal

Plan the Claim Graph and Research Delta layer that will later connect Stage 02 research objects and Stage 04 evidence candidates into provenance-preserving relation and delta workflows. This is planning only until GPT Pro and user gates authorize implementation.

## User needs

Researchers need an auditable plan for connecting claims to evidence, comparing research state over time, and preserving rationale, provenance, and project boundaries so future literature matrices, method cards, dataset cards, evidence cards, research deltas, and Repro Packs remain replayable.

## Files allowed

Planning files:

- `PLANS/STAGE_05_PLAN.md`
- `TASKS/STAGE_05_TASKS.md`
- `CHECKLISTS/STAGE_05_CHECKLIST.md`
- `reviews/stage_05/`
- `deployments/stage_05/`
- `docs/architecture/stage_05_claim_graph_research_delta.md`
- `docs/codex/stage_05_commands.md`
- `logs/subagents/stage_05/`
- Stage 04 terminal handoff files in `reviews/stage_04/`
- required control and RunLog records

Future implementation files, only after approved `/goal`:

- `apps/api/finsignalhub_api/claim_graph/`
- `apps/api/finsignalhub_api/research_delta/`
- `apps/api/tests/test_stage05_claim_graph.py`
- `apps/api/tests/test_stage05_research_delta.py`
- `apps/api/tests/fixtures/stage05_claim_graph/`

## Files forbidden

- Stage 05 runtime package during planning
- Stage 05 tests or fixtures during planning
- Database migrations during planning
- MCP business tools
- Repro Pack export logic
- Admin UI product behavior or dashboard behavior
- Chatbot, generic RAG, stock prediction, investment advice, report generation, model leaderboard, Risk Mode, Replay Engine
- Live external API calls, real LLM calls, API keys, provider credentials, auth, or billing
- Destructive Stage 02/03/04 changes

## Skills required

`finsignal-product-governor`, `evidence-graph-architect`, `phase-gate-auditor`, `codex-log-keeper`, `github-stage-deployer`, `github-review-resolver`, `gpt-pro-review-preparer`, `browser-gpt-pro-reviewer`, `subagent-coordinator`, `acceptance-evidence-collector`, `stage-next-goal-synthesizer`.

## Subagents required

- `claim-graph-architecture-agent`
- `relation-rule-agent`
- `research-delta-agent`
- `project-boundary-validator-agent`
- `test-plan-agent`
- `docs-log-agent`
- `scope-review-agent`

## Implementation tasks

Planning tasks:

1. Save Stage 04 terminal GPT Pro closeout PASS and Stage 05 planning-only instruction.
2. Write Stage 05 plan, tasks, checklist, PR body, GPT Pro review packet, acceptance placeholder, deployment placeholder, architecture doc, command doc, and subagent logs.
3. Define future Claim Graph module boundaries without creating runtime code.
4. Define future Research Delta semantics without creating runtime code.
5. Define relation rationale, provenance, same-project guards, `qualifies` compatibility, and forbidden relation states.
6. Define file authority for each future subagent.
7. Update control logs, artifact registry, dashboard, current state, action queue, and RunLog.
8. Run planning-only checks.
9. Open PR and request Codex review.
10. Submit the plan to GPT Pro for planning gate.

Later implementation tasks must be created only after GPT Pro plan PASS and approved `/goal`.

## Test tasks

Planning-only checks:

- `phase_check.py --stage 05`
- no Stage 05 claim graph package check
- no Stage 05 research delta package check
- no Stage 05 tests or fixtures check
- forbidden-scope scan
- secret scan
- `git diff --check`

Future implementation tests:

- same-project relation creation
- cross-project relation rejection
- relation enum validation
- `qualifies` compatibility for limitation-style evidence
- relation rationale required
- relation provenance required
- claim graph neighborhood output
- Research Delta baseline/current time semantics
- changed-claims delta
- no report-generation wording
- mock-only fixture behavior
- no live network/provider/LLM behavior in CI

## Docs tasks

Document Claim Graph boundary, relation type intent, rationale/provenance fields, same-project validation, Research Delta baseline/current semantics, deferred implementation paths, mock-only test plan, file boundaries, and stop conditions.

## GitHub deployment tasks

Use branch `stage/05-claim-graph-delta`. PR title is `Stage 05: Claim Graph and Research Delta Planning`; PR body comes from `reviews/stage_05/PR_BODY.md`; each pushed head must pass CI and `@codex review`.

## GPT Pro review tasks

Submit the Stage 05 plan packet to GPT Pro. Save response, action items, final result, and any Stage 05 implementation instructions. Do not implement before PASS and a separate `/goal`.

## Stop conditions

Stop if planning requires API keys, live network tests, external LLM calls, production graph computation, database migrations, MCP business tools, Repro Pack export, UI/dashboard behavior, chatbot/RAG behavior, financial prediction, investment advice, Risk Mode, Replay Engine, destructive restructuring, or evidence artifacts that cannot preserve provenance lineage.
