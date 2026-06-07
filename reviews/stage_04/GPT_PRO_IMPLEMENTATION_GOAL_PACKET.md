# GPT Pro Implementation Goal Review Packet: Stage 04

Please review this as a Stage 04 implementation `/goal` draft only. Do not treat it as implementation code.

## Project Identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. The product helps AI Agents call structured evidence workflows for researchers and later financial research users.

Primary outputs are research delta, claim graph, evidence card, literature matrix, method card, dataset card, repro pack, and tool-call logs. Stage 04 is only about future evidence extraction from normalized documents into validated evidence candidates. It must not become a chatbot, generic RAG system, report generator, stock prediction tool, investment advisor, dashboard, model leaderboard, Risk Mode, or Replay Engine.

## Review Request

Please judge whether the attached Stage 04 implementation goal draft is complete enough to authorize a later implementation run.

Required answer format:

- VERDICT: PASS, CONDITIONAL PASS, or FAIL
- Is this implementation goal draft complete enough to start Stage 04 implementation after GitHub gates pass?
- What must be fixed before implementation?
- What can be deferred?
- Are the allowed files correct?
- Are the forbidden files and product boundaries strict enough?
- Are the tests sufficient and mock-only?
- Are the subagent boundaries sufficient?
- Is any scope drifting into claim graph, Research Delta, Repro Pack, MCP business tools, dashboard, chatbot/RAG, stock/investment, Risk Mode, or Replay Engine?

## Current GitHub Evidence Before This Draft

- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11
- Current clean planning closeout remediation head before goal drafting: `b954aa391f9013342e4092c5500f0ece5b2c25ba`
- CI PASS:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/27037676738/job/79805686417
  - https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/27037679122/job/79805693174
- Codex no-major:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11#issuecomment-4635164432
- Review threads after resolving outdated CR-04-024: unresolved = 0, unresolved current = 0, unresolved outdated = 0.

This goal-draft commit must also pass CI and current-head Codex before this packet is final.

## GPT Pro Source Authorization

GPT Pro final closeout recheck returned PASS and allowed only drafting a separate Stage 04 implementation `/goal`.

Source files:

- `reviews/stage_04/GPT_PRO_FINAL_CLOSEOUT_RECHECK_RESPONSE.md`
- `reviews/stage_04/GPT_PRO_FINAL_CLOSEOUT_RECHECK_ACTION_ITEMS.md`

## Goal Draft Under Review

Primary draft:

- `PLANS/STAGE_04_IMPLEMENTATION_GOAL.md`

Acceptance draft:

- `reviews/stage_04/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md`

## Intended Future Implementation Scope

If GPT Pro accepts this goal, the next implementation run may create:

- extraction schemas
- relation enum
- quote-span validation
- no-quote rationale validation
- provenance validation
- deterministic mock LLM adapter
- worker skeleton
- mock-only tests and fixtures
- docs, logs, review packets, and acceptance evidence

## Future Files Allowed Only After Approval

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
- `logs/subagents/stage_04/*.md`
- Stage 04 docs, logs, PR, review, and control evidence files.

## Still Forbidden Until Goal Acceptance

- Creating the future implementation files listed above.
- Runtime extraction schemas or implementation code.
- Real LLM calls or external network calls.
- API keys, provider credentials, paid services, or private documents.
- Claim graph computation.
- Research Delta computation.
- Repro Pack logic.
- MCP business tools.
- Admin UI, dashboard, chatbot, RAG, report generation, stock prediction, investment advice, model leaderboard, Risk Mode, Replay Engine, auth, or billing.
- Unreviewed Stage 02 persisted schema changes.
- Unreviewed Stage 03 connector behavior changes.

## Required Future Tests

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04`
- `python -m compileall apps/api/finsignalhub_api`
- `python -m pytest apps/api/tests/test_stage04_extraction.py`
- valid and invalid quote-span cases
- no-quote rationale requirement
- relation enum validation
- provenance required-field validation
- deterministic mock adapter output
- worker fixture test
- no-network enforcement
- forbidden Stage 05+ scope scan
- high-confidence secret scan
- `git diff --check`
- CI PASS
- current-head Codex no-major
- unresolved review threads = 0
- GPT Pro final implementation review

## Subagent Boundaries

- `extraction-schema-agent`: schemas and relation enum only.
- `quote-span-agent`: quote-span and no-quote validation only.
- `provenance-agent`: provenance validators and deterministic error shapes only.
- `mock-llm-adapter-agent`: deterministic fixture adapter only, no real provider calls.
- `worker-skeleton-agent`: worker orchestration skeleton only.
- `test-agent`: mock-only tests and fixtures only.
- `docs-log-agent`: docs, logs, and review evidence only.
- `scope-review-agent`: product-governor and forbidden-scope evidence only.

## Known Limitations

- No implementation has been created yet.
- GPT Pro has not yet accepted this implementation goal.
- This goal-draft head must pass GitHub CI/Codex before implementation can start.
- Any implementation must remain mock-only by default and must not require external services.

## Questions For GPT Pro

1. VERDICT: PASS, CONDITIONAL PASS, or FAIL?
2. Is this implementation goal strict enough to prevent product drift?
3. Are allowed files complete and minimal?
4. Are forbidden files and behaviors complete?
5. Are tests sufficient for Stage 04 implementation acceptance?
6. Are subagent boundaries clear enough?
7. If PASS or accepted CONDITIONAL PASS, provide the exact Stage 04 implementation `/goal` text and ordered steps to execute next.
