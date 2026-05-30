# Stage 03 Plan: Source Connectors

## Context Read

Required context for this plan:

- `AGENTS.md`
- `PLANS.md`
- `CONTROL/01_PRODUCT_DEFINITION.md`
- `CONTROL/02_STAGE_ROADMAP.md`
- `CONTROL/03_PHASE_ACCEPTANCE.md`
- `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`
- `CONTROL/21_SUBAGENT_PROTOCOL.md`
- `RUNLOG/LONG_RUN_SUMMARY.md`
- `reviews/stage_02/STAGE_ACCEPTANCE_RESULT.md`
- `reviews/stage_02/GPT_PRO_FINAL_REVIEW_RESPONSE.md`

Stage 02 is merged and tagged. GPT Pro authorized Stage 03 planning only. This plan does not implement connectors, external calls, ingestion jobs, extraction, claim graph logic, MCP business tools, or UI behavior.

## Capability Check

- Local shell, Python, Node.js, Docker, GitHub CLI, GitHub connector, GitHub Actions, and Codex review are available.
- Chrome extension background tab discovery works and is preferred for GPT Pro. Standalone background Computer Use is not exposed; foreground visual recovery remains suspended while the user is using Chrome.
- Network access may be available, but Stage 03 normal tests must use fixtures and mocks only.

## Product Alignment Check

Stage 03 must preserve FinSignalHub as Research Mode-first, MCP-first, and evidence-stream oriented.

The planned connectors exist only to normalize external or uploaded source metadata into provenance-preserving `SourceCreate` and `DocumentCreate` inputs for later evidence workflows, using the schemas already created in Stage 02. They must not produce evidence extraction, summaries, investment advice, stock signals, dashboards, generic RAG answers, or report output.

## Scope

Stage 03 planning scope:

- Define source connector boundaries for OpenAlex, Crossref, Semantic Scholar, arXiv, and user upload metadata.
- Define a connector base interface and normalized `SourceCreate`/`DocumentCreate` mapping that stays within the existing Stage 02 persisted schemas.
- Define fixture-based mocked tests and no-network CI rules.
- Define file boundaries, subagents, docs, logs, GitHub deployment, Codex review, GPT Pro plan review, risks, and stop conditions.

Stage 03 implementation remains blocked until this plan passes GitHub/Codex and GPT Pro plan review and a later approved `/goal` exists.

## Files To Create Or Modify

Planning files allowed now:

- `PLANS/STAGE_03_PLAN.md`
- `TASKS/STAGE_03_TASKS.md`
- `CHECKLISTS/STAGE_03_CHECKLIST.md`
- `reviews/stage_03/`
- `deployments/stage_03/`
- `docs/architecture/stage_03_source_connectors.md`
- `docs/codex/stage_03_commands.md`
- `logs/subagents/stage_03/`
- Required `CONTROL/`, `RUNLOG/`, `CHANGELOG.md`, and PR evidence records.

Implementation files proposed for a later approved Stage 03 goal:

- `apps/api/finsignalhub_api/connectors/`
- `apps/api/tests/test_stage03_connectors.py`
- `apps/api/tests/fixtures/stage03_connectors/`

## Files Not To Touch

Do not modify Stage 02 domain model behavior, migrations, MCP business tools, evidence extraction modules, claim graph logic, admin UI product behavior, or Repro Pack export logic during Stage 03 planning.

## Skills

Use:

- `finsignal-product-governor`
- `connector-builder`
- `evidence-graph-architect`
- `phase-gate-auditor`
- `codex-log-keeper`
- `github-stage-deployer`
- `github-review-resolver`
- `gpt-pro-review-preparer`
- `browser-gpt-pro-reviewer`
- `subagent-coordinator`
- `acceptance-evidence-collector`

## Subagents

Declare these bounded subagents for the later implementation plan:

- `openalex-agent`: OpenAlex fixture mapping only.
- `crossref-agent`: Crossref fixture mapping only.
- `semantic-scholar-agent`: Semantic Scholar fixture mapping only.
- `arxiv-agent`: arXiv fixture mapping only.
- `user-upload-agent`: uploaded-file metadata normalization plan only.
- `connector-review-agent`: provenance and no-network boundary review.

Each subagent must write `logs/subagents/stage_03/<agent_name>.md` and may modify only files granted in the approved implementation goal.

## Implementation Steps

Planning steps:

1. Create Stage 03 plan, tasks, checklist, review packet, PR body, acceptance placeholder, deployment placeholder, and architecture/commands docs.
2. Update control logs and RunLog to show Stage 03 planning active.
3. Run planning-only checks: phase check, no implementation file check, secret scan, forbidden-scope scan, and `git diff --check`.
4. Commit, push, open PR, request `@codex review`, and wait for CI.
5. Submit the Stage 03 plan packet to GPT Pro through background Chrome extension when possible.

Later implementation steps must be written only after GPT Pro plan PASS and a new approved `/goal`.

## Tests

### Local checks

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03`
- no Stage 03 implementation files exist
- no external API calls added
- likely-secret scan
- `git diff --check`

### Unit tests

No Stage 03 unit tests are run during planning because connector implementation is not authorized. The later implementation goal must add mocked connector unit tests before any Gate 3 pass.

### Integration tests

No Stage 03 integration tests are run during planning. The later implementation goal must keep connector integration tests fixture-based and must not require live external APIs or credentials.

### Acceptance checks

Planning acceptance requires the Stage 03 plan, tasks, checklist, review packet, PR body, deployment placeholder, architecture note, command note, logs, GitHub PR, Codex review, and GPT Pro plan review to exist before implementation may begin.

Tests to include in the later implementation goal:

- `pytest apps/api/tests/test_stage03_connectors.py`
- mocked HTTP tests only
- fixtures for OpenAlex, Crossref, Semantic Scholar, arXiv, and user upload metadata
- normalized `SourceCreate` and `DocumentCreate` mapping validation
- publication/release time mapping validation
- URL, DOI, locator, source identity, source type, and provider metadata mapping validation
- rate-limit and retry behavior with mocks
- no real API keys and no network-dependent CI

## Docs

Docs must define connector contracts, normalized `SourceCreate`/`DocumentCreate` fields, provenance mapping, no-network testing, fixture responsibilities, licensing risks, and stop conditions.

## GitHub Deployment

Use branch `stage/03-source-connectors`. PR title must be `Stage 03: Source Connectors`. PR body comes from `reviews/stage_03/PR_BODY.md`. After PR creation, comment:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

## GPT Pro Review

Submit `reviews/stage_03/GPT_PRO_REVIEW_PACKET.md` to the specified GPT Pro page. GPT Pro must answer PASS, CONDITIONAL PASS, or FAIL for planning. Stage 03 implementation cannot begin until GPT Pro plan review passes and a separate `/goal` exists.

## Risks

- Connector work drifts into extraction, ingestion workflows, summaries, or generic RAG.
- Real network tests or API keys leak into CI.
- Source terms or licensing constraints are ignored.
- User upload becomes full parsing or extraction.
- Normalized source/document payloads lose provenance needed by Stage 04 or require unsupported Stage 02 schema changes.

## Stop Conditions

Stop if:

- A connector requires paid API keys, private credentials, secrets, or login.
- Normal tests require live network calls.
- Work requires evidence extraction, LLM adapters, claim graph computation, research delta computation, MCP business tools, or UI product behavior.
- Connector output cannot preserve source identity, source type, retrieval time, URL/DOI/locator, provider metadata, transformation notes, validation status, and tool-call lineage using existing Stage 02 Source, Document, and ToolCallLog schemas.
