# GPT Pro Implementation Goal Action Items: Stage 03

Timestamp: 2026-05-30T15:51:25-05:00

Source response: `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md`

## Status

GPT Pro returned `VERDICT: PASS` for the Stage 03 implementation `/goal` draft.

## Must Fix Before Implementation

| Item | Status | Evidence |
| --- | --- | --- |
| Save GPT Pro response and action items under `reviews/stage_03/` | done in local evidence update | `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md`; this file |
| Update implementation-goal draft acceptance | in progress in this evidence update | `reviews/stage_03/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md` |
| Update current stage state | in progress in this evidence update | `CONTROL/24_CURRENT_STAGE_STATE.md` |
| Update next action queue | in progress in this evidence update | `CONTROL/25_NEXT_ACTION_QUEUE.md` |
| Update RunLog | in progress in this evidence update | `RUNLOG/LONG_RUN_CURRENT.md`; `RUNLOG/LONG_RUN_SUMMARY.md` |
| Update artifact registry | in progress in this evidence update | `CONTROL/18_ARTIFACT_REGISTRY.md` |
| Confirm implementation branch head still has CI PASS and current-head Codex no-major before connector code starts | satisfied for head `8f10f95c69c3eaf7d6ada7b878e017b917929e33`; any evidence-sync commit must refresh this gate before implementation code starts | PR #10 CI jobs and Codex no-major comment listed in the response file |

## Authorized Implementation Scope

Stage 03 may implement source connector primitives only for:

- OpenAlex
- Crossref
- Semantic Scholar
- arXiv
- user-upload metadata

Connector outputs must normalize into existing Stage 02-compatible `SourceCreate`, `DocumentCreate`, and `ToolCallLog` payloads and preserve source identity, source type, retrieval or fixture timestamp, URL/DOI/external locator, provider metadata, transformation notes, validation status, and tool-call lineage.

## Allowed Files

- `apps/api/finsignalhub_api/connectors/`
- `apps/api/tests/test_stage03_connectors.py`
- `apps/api/tests/fixtures/stage03_connectors/`
- `docs/architecture/stage_03_source_connectors.md`
- `docs/codex/stage_03_commands.md`
- `logs/subagents/stage_03/`
- `reviews/stage_03/`
- `deployments/stage_03/`
- Required `CONTROL/`, `RUNLOG/`, checklist, task, and changelog governance records.

## Forbidden Scope

Do not implement evidence extraction, LLM adapters, claim graph computation, Research Delta computation, MCP business tools, Repro Pack export logic, admin UI product behavior, chatbot behavior, generic RAG, stock prediction, investment advice, dashboard behavior, Risk Mode, Replay Engine, auth, billing, live external API tests in CI, API keys, credentials, paid API assumptions, or full document parsing for user upload.

## Required Tests And Gates

- `pytest apps/api/tests/test_stage03_connectors.py`
- Mocked fixture tests only.
- No-network CI enforcement.
- OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload fixture mapping tests.
- `SourceCreate` and `DocumentCreate` compatibility tests.
- Publication/release time mapping tests.
- DOI, URL, locator, external id, source identity, and source type mapping tests.
- Provider metadata and transformation notes tests.
- Rate-limit/retry behavior tests with mocks if retry handling exists.
- Secret scan.
- Forbidden-scope scan.
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03`
- `git diff --check`
- CI PASS and current-head Codex no-major before final GPT Pro implementation review.

## Required Subagents

- `openalex-agent`
- `crossref-agent`
- `semantic-scholar-agent`
- `arxiv-agent`
- `user-upload-agent`
- `connector-review-agent`

Each subagent must stay within bounded file authority and write `logs/subagents/stage_03/<agent_name>.md`.

## Deferred Items

- Broader connector edge-case expansion.
- Richer fixture coverage beyond the required minimum.
- Advanced rate-limit/retry policy hardening.
- Connector performance optimization.
- Any Stage 04+ extraction, claim graph, delta, Repro Pack, or MCP business-tool behavior.

## Stop Conditions

Stop if a real API key, private credential, paid API account, login, secret, live network test dependency, `EvidenceItem` generation, LLM adapter, extraction pipeline, claim graph, Research Delta, Repro Pack, MCP business tool, dashboard, chatbot/RAG, stock prediction, investment advice, Risk Mode, Replay Engine, auth, billing, or Stage 02 schema/migration change without blocker and ADR becomes necessary.

