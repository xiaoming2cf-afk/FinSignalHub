# Stage 03 Tasks: Source Connectors

## Stage goal

Plan Research Mode source connectors that normalize public source metadata and user upload metadata into provenance-preserving `SourceCreate` and `DocumentCreate` inputs that match the existing Stage 02 schemas. This is planning only until GPT Pro and user gates authorize implementation.

## User needs

Researchers need repeatable, provenance-aware source intake so later stages can build evidence cards, claim graph edges, literature matrices, method cards, dataset cards, and Repro Packs without relying on opaque source text.

## Files allowed

Planning files:

- `PLANS/STAGE_03_PLAN.md`
- `TASKS/STAGE_03_TASKS.md`
- `CHECKLISTS/STAGE_03_CHECKLIST.md`
- `reviews/stage_03/`
- `deployments/stage_03/`
- `docs/architecture/stage_03_source_connectors.md`
- `docs/codex/stage_03_commands.md`
- `logs/subagents/stage_03/`
- required control and RunLog records

Later implementation files, only after approved `/goal`:

- `apps/api/finsignalhub_api/connectors/`
- `apps/api/tests/test_stage03_connectors.py`
- `apps/api/tests/fixtures/stage03_connectors/`

## Files forbidden

- Evidence extraction
- LLM adapters
- Claim graph computation
- Research delta engines
- Repro Pack export logic
- MCP business tools
- Admin UI product behavior
- Chatbot, generic RAG, stock prediction, investment advice, dashboard behavior, Risk Mode, Replay Engine

## Skills required

`finsignal-product-governor`, `connector-builder`, `evidence-graph-architect`, `phase-gate-auditor`, `codex-log-keeper`, `github-stage-deployer`, `github-review-resolver`, `gpt-pro-review-preparer`, `browser-gpt-pro-reviewer`, `subagent-coordinator`, `acceptance-evidence-collector`.

## Subagents required

Planning declares but does not run implementation subagents:

- `openalex-agent`
- `crossref-agent`
- `semantic-scholar-agent`
- `arxiv-agent`
- `user-upload-agent`
- `connector-review-agent`

## Implementation tasks

Planning tasks:

1. Write Stage 03 plan, tasks, checklist, PR body, GPT Pro review packet, acceptance placeholder, deployment placeholder, and docs.
2. Define connector base contract and normalized `SourceCreate`/`DocumentCreate` mapping without Stage 02 schema or migration changes.
3. Define mocked fixture strategy and no-network CI rule.
4. Define file authority for each future subagent.
5. Update control logs, artifact registry, dashboard, and RunLog.
6. Run planning-only checks.
7. Open PR and request Codex review.
8. Submit plan to GPT Pro for planning gate.

Later implementation tasks must be created only after GPT Pro plan PASS and approved `/goal`.

## Test tasks

Planning-only checks:

- `phase_check.py --stage 03`
- no implementation files check
- no external API client/runtime call check
- secret scan
- `git diff --check`

Future implementation tests:

- mocked HTTP only
- fixture mapping tests for OpenAlex, Crossref, Semantic Scholar, arXiv, and user upload metadata
- normalized `SourceCreate` and `DocumentCreate` validation
- provenance mapping validation
- no-network CI enforcement

## Docs tasks

Document connector contracts, normalized fields, provenance mapping, fixture ownership, source licensing risks, and stop conditions.

## GitHub deployment tasks

Use branch `stage/03-source-connectors`, PR title `Stage 03: Source Connectors`, PR body from `reviews/stage_03/PR_BODY.md`, CI, and `@codex review`.

## GPT Pro review tasks

Submit the Stage 03 plan packet to GPT Pro. Save response, action items, final result, and any Stage 03 implementation instructions. Do not implement before PASS and a separate `/goal`.

## Stop conditions

Stop if planning requires API keys, live network tests, evidence extraction, LLM adapters, claim graph computation, research delta computation, MCP business tools, destructive restructuring, or licensing decisions that require user judgment.
