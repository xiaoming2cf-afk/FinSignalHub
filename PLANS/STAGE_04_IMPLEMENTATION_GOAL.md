# Stage 04 Implementation Goal Draft

## Status

Draft only. This file does not authorize implementation until GPT Pro reviews and accepts the implementation goal.

## Stage ID

Stage 04: Evidence Extraction

## Approved Plan Path

- `PLANS/STAGE_04_PLAN.md`

## Source Authorization

GPT Pro final closeout recheck allowed drafting a separate Stage 04 implementation `/goal` only after PR #11 live GitHub gates were clean.

Current live GitHub evidence before this draft:

- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11
- Reviewed remediation head: `b954aa391f9013342e4092c5500f0ece5b2c25ba`
- CI PASS:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/27037676738/job/79805686417
  - https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/27037679122/job/79805693174
- Codex no-major:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11#issuecomment-4635164432
- Review threads after resolving outdated CR-04-024: unresolved = 0, unresolved current = 0, unresolved outdated = 0.

This draft head must also pass live PR #11 CI, current-head Codex, and GPT Pro implementation-goal review before implementation may start.

## Product Alignment

The future implementation must support Research Mode evidence-stream extraction from Stage 03 normalized documents into future `EvidenceItem` candidates. It must preserve source identity, document reference, quote spans or no-quote rationale, relation labels, confidence, transformation notes, and tool-call lineage.

This goal does not authorize chat answers, generic summaries, reports, stock prediction, investment advice, dashboards, model rankings, Risk Mode, Replay Engine, claim graph computation, Research Delta computation, Repro Pack export, MCP business tools, auth, billing, or frontend behavior.

## Done When

Implementation may be considered done only when all of these are true:

- Extraction schemas exist for candidate evidence, quote spans, no-quote rationale, relation labels, confidence, and provenance.
- Quote-span validation accepts exact spans against fixture document text and rejects invalid spans with deterministic error shapes.
- No-quote candidates require an explicit rationale and source/provenance fields.
- Relation labels are limited to the approved Stage 04 enum and do not compute claim graph edges.
- Provenance validation requires source identity, source type, document reference, retrieval time, transformation notes, confidence, and tool-call lineage.
- Deterministic mock LLM adapter returns fixture-based candidates without network, credentials, paid services, or real provider calls.
- Worker skeleton accepts normalized documents and returns validated candidates through mock-only code paths.
- Mock-only tests cover valid extraction, invalid quote spans, no-quote rationale, relation validation, provenance failures, deterministic mock output, worker fixture behavior, no-network enforcement, and forbidden Stage 05+ scope.
- Docs and logs are updated.
- Local checks pass.
- PR #11 or a successor Stage 04 implementation PR has CI PASS, current-head Codex no-major, unresolved review threads = 0, GPT Pro PASS or accepted CONDITIONAL PASS, and phase-gate-auditor PASS.

## Files Allowed For Future Implementation

Only after GPT Pro accepts this implementation goal:

- `apps/api/finsignalhub_api/extraction/__init__.py`
- `apps/api/finsignalhub_api/extraction/schemas.py`
- `apps/api/finsignalhub_api/extraction/relations.py`
- `apps/api/finsignalhub_api/extraction/provenance.py`
- `apps/api/finsignalhub_api/extraction/quote_span.py`
- `apps/api/finsignalhub_api/extraction/mock_llm.py`
- `apps/api/finsignalhub_api/extraction/worker.py`
- `apps/api/tests/test_stage04_extraction.py`
- `apps/api/tests/fixtures/stage04_extraction/README.md`
- `apps/api/tests/fixtures/stage04_extraction/*.json`
- `docs/architecture/stage_04_evidence_extraction.md`
- `docs/codex/stage_04_commands.md`
- `reviews/stage_04/*`
- `deployments/stage_04/*`
- Required `CONTROL/*`, `RUNLOG/*`, `TASKS/STAGE_04_TASKS.md`, and `CHECKLISTS/STAGE_04_CHECKLIST.md` evidence updates.

## Files Forbidden

- Stage 02 migrations or persisted domain model changes unless GPT Pro explicitly adds them to this goal.
- Stage 03 connector behavior changes unless needed only for test fixtures and explicitly documented.
- Claim graph, Research Delta, Repro Pack, MCP business tools, admin UI, auth, billing, or deployment runtime changes.
- Any file requiring API keys, provider credentials, paid services, live network calls, or private documents.

## Subagents

Use bounded subagents only after goal approval:

- `extraction-schema-agent`: schema and relation enum files only.
- `quote-span-agent`: quote-span and no-quote validation only.
- `provenance-agent`: provenance validators and failure shapes only.
- `mock-llm-adapter-agent`: deterministic mock adapter only.
- `worker-skeleton-agent`: worker orchestration skeleton only.
- `test-agent`: mock-only tests and fixtures only.
- `docs-log-agent`: docs, command notes, logs, and acceptance evidence only.
- `scope-review-agent`: forbidden-scope scan and product-governor evidence only.

Each subagent must write `logs/subagents/stage_04/<agent_name>.md` with files touched, summary, risks, tests, and unresolved issues.

## Commands To Run

Before implementation push:

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04`
- `python -m compileall apps/api/finsignalhub_api`
- `python -m pytest apps/api/tests/test_stage04_extraction.py`
- Forbidden path and forbidden Stage 05+ scope scans.
- High-confidence secret scan.
- No-network enforcement check for extraction tests.
- `git diff --check`

After push:

- `gh pr checks 11 --watch --interval 10`
- Current-head `@codex review`
- Review-thread unresolved count check.
- GPT Pro implementation review through the specified Chrome/GPT Pro page.

## Review Artifacts To Create

- `reviews/stage_04/GPT_PRO_IMPLEMENTATION_REVIEW_PACKET.md`
- `reviews/stage_04/GPT_PRO_IMPLEMENTATION_REVIEW_RESPONSE.md`
- `reviews/stage_04/GPT_PRO_IMPLEMENTATION_ACTION_ITEMS.md`
- Updated `reviews/stage_04/STAGE_ACCEPTANCE_RESULT.md`
- Updated `reviews/stage_04/CODEX_REVIEW_SUMMARY.md`
- Updated `deployments/stage_04/GITHUB_PR.md`

## Phase Gate Requirements

All ten gates must pass: scope, functionality, tests, docs, logs, GitHub, GPT Pro, product governance, security, and next stage.

Missing CI, missing current-head Codex, unresolved review threads, missing GPT Pro review, skipped tests without approved blocker, or product drift means BLOCKED or FAIL.

## Stop Conditions

Stop immediately if implementation requires real LLM calls, external network calls, provider credentials, claim graph computation, Research Delta computation, Repro Pack export, MCP business tools, UI/dashboard behavior, chatbot/RAG behavior, stock prediction, investment advice, Risk Mode, Replay Engine, auth, billing, or unreviewed cross-stage schema changes.
