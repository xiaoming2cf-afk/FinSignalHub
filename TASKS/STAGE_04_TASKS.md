# Stage 04 Tasks: Evidence Extraction Skeleton Planning

## Stage goal

Plan an evidence extraction skeleton that will later transform Stage 03 normalized documents into provenance-preserving evidence candidates. This is planning only until GPT Pro and user gates authorize implementation.

## User needs

Researchers need repeatable extraction planning so future evidence cards, literature matrices, method cards, dataset cards, claim graph edges, research deltas, and Repro Packs can rely on quoted or explicitly justified evidence candidates instead of opaque summaries.

## Files allowed

Planning files:

- `PLANS/STAGE_04_PLAN.md`
- `TASKS/STAGE_04_TASKS.md`
- `CHECKLISTS/STAGE_04_CHECKLIST.md`
- `reviews/stage_04/`
- `deployments/stage_04/`
- `docs/architecture/stage_04_evidence_extraction.md`
- `docs/codex/stage_04_commands.md`
- `logs/subagents/stage_04/`
- required control and RunLog records

Future implementation files, only after approved `/goal`:

- `apps/api/finsignalhub_api/extraction/`
- `apps/api/tests/test_stage04_extraction.py`
- `apps/api/tests/fixtures/stage04_extraction/`

## Files forbidden

- Stage 04 implementation package during planning
- Stage 04 tests or fixtures during planning
- Production extraction
- External LLM calls
- Real API keys or provider credentials
- Claim graph computation
- Research Delta computation
- Repro Pack export logic
- MCP business tools
- Admin UI product behavior
- Chatbot, generic RAG, stock prediction, investment advice, dashboard behavior, Risk Mode, Replay Engine

## Skills required

`finsignal-product-governor`, `evidence-graph-architect`, `phase-gate-auditor`, `codex-log-keeper`, `github-stage-deployer`, `github-review-resolver`, `gpt-pro-review-preparer`, `browser-gpt-pro-reviewer`, `subagent-coordinator`, `acceptance-evidence-collector`, `stage-next-goal-synthesizer`.

## Subagents required

Planning declares but does not run implementation subagents:

- `extraction-schema-agent`
- `llm-adapter-agent`
- `provenance-agent`
- `dedup-agent`
- `test-agent`
- `docs-agent`

## Implementation tasks

Planning tasks:

1. Write Stage 04 plan, tasks, checklist, PR body, GPT Pro review packet, acceptance placeholder, deployment placeholder, architecture doc, command doc, and subagent log README.
2. Define future extraction candidate schema boundaries without creating implementation code.
3. Define relation label enum boundaries without claim graph computation.
4. Define quote-span validation, no-quote rationale, provenance validation, and mock LLM adapter boundaries.
5. Define file authority for each future subagent.
6. Update control logs, artifact registry, dashboard, current state, action queue, and RunLog.
7. Run planning-only checks.
8. Open PR and request Codex review.
9. Submit the plan to GPT Pro for planning gate.

Later implementation tasks must be created only after GPT Pro plan PASS and approved `/goal`.

## Test tasks

Planning-only checks:

- `phase_check.py --stage 04`
- no Stage 04 extraction package check
- no Stage 04 test/fixture path check
- forbidden-scope scan
- secret scan
- `git diff --check`

Future implementation tests:

- mock LLM extraction adapter only
- quote span validation fixtures
- no-quote rationale validation
- relation enum validation
- provenance completeness validation
- deterministic error-shape tests
- no external network or provider credentials in CI

## Docs tasks

Document extraction boundary, schema intent, relation labels, quote-span and no-quote rules, provenance fields, mock adapter constraints, worker skeleton constraints, file boundaries, and stop conditions.

## GitHub deployment tasks

Use branch `stage/04-evidence-extraction`. PR title is `Stage 04: Evidence Extraction Planning`; PR body comes from `reviews/stage_04/PR_BODY.md`; each pushed head must pass CI and `@codex review`.

## GPT Pro review tasks

Submit the Stage 04 plan packet to GPT Pro. Save response, action items, final result, and any Stage 04 implementation instructions. Do not implement before PASS and a separate `/goal`.

## Stop conditions

Stop if planning requires API keys, live network tests, external LLM calls, production extraction, claim graph computation, research delta computation, MCP business tools, destructive restructuring, or evidence artifacts that cannot preserve quote/provenance lineage.
