# Stage 03 Implementation Goal Draft: Source Connectors

## Stage ID

Stage 03: Source Connectors implementation.

## Approved Plan Path

- `PLANS/STAGE_03_PLAN.md`
- GPT Pro planning follow-up PASS: `reviews/stage_03/GPT_PRO_FOLLOWUP_RESPONSE.md`
- GPT Pro PR #10 closeout PASS: `reviews/stage_03/GPT_PRO_CLOSEOUT_RESPONSE.md`

This file is a `/goal` draft only. It does not start connector implementation by itself.

## Goal Text

Implement Research Mode source connector primitives for OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata. The implementation must normalize source metadata into existing Stage 02 `SourceCreate` and `DocumentCreate` schema-compatible payloads, preserve provenance and tool-call lineage, and use mocked fixture tests only.

The implementation must not create evidence extraction, LLM adapters, claim graph computation, research delta computation, MCP business tools, admin UI product behavior, chatbot behavior, generic RAG, stock prediction, investment advice, dashboard behavior, Risk Mode, or Replay Engine.

## Done When

- Connector base contract exists under the approved connector package path.
- OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata connectors exist with mocked fixture coverage.
- All connector outputs map to existing Stage 02 `SourceCreate` and `DocumentCreate` fields without changing Stage 02 domain semantics or migrations unless an explicit blocker and ADR justify it.
- Connector provenance includes source identity, source type, retrieval timestamp or fixture timestamp, URL/DOI/external locator, provider metadata, transformation notes, validation status, and tool-call lineage fields expected by Stage 02.
- Normal tests do not require live network calls, API keys, private credentials, paid services, or user login.
- Local checks pass, GitHub CI passes, Codex review has no major findings or all critical findings are fixed, and GPT Pro final implementation review returns PASS or accepted CONDITIONAL PASS with critical items resolved.
- Stage 03 acceptance result records PASS, FAIL, or BLOCKED with evidence for all ten gates.

## Files Allowed

Implementation files allowed only after this goal is accepted by GPT Pro and activated:

- `apps/api/finsignalhub_api/connectors/`
- `apps/api/tests/test_stage03_connectors.py`
- `apps/api/tests/fixtures/stage03_connectors/`
- `docs/architecture/stage_03_source_connectors.md`
- `docs/codex/stage_03_commands.md`
- `logs/subagents/stage_03/`
- `reviews/stage_03/`
- `deployments/stage_03/`
- required `CONTROL/`, `RUNLOG/`, checklist, task, and changelog governance records

## Files Not To Touch

- Stage 02 migrations and persisted schema behavior, unless a blocker and ADR are created before the change.
- Evidence extraction modules.
- LLM adapter modules.
- Claim graph or research delta modules.
- MCP business tools.
- Admin UI product behavior.
- Repro Pack export logic.
- Any secret-bearing local configuration.

## Commands To Run

Pre-implementation gate:

```powershell
python finsignalhub-codex-plugin\scripts\phase_check.py --stage 03
git diff --check
```

After connector implementation starts:

```powershell
pytest apps/api/tests/test_stage03_connectors.py
python finsignalhub-codex-plugin\scripts\phase_check.py --stage 03
git diff --check
```

Additional required scans:

- Forbidden-scope scan for extraction, LLM adapter, claim graph, research delta, MCP business tools, UI/dashboard/chatbot/RAG behavior, stock prediction, and investment advice.
- No-network test audit proving connector tests use fixtures/mocks only.
- Secret scan excluding generated runtime artifacts.
- Artifact and checkpoint ID uniqueness checks.

## Logs To Update

- `CONTROL/04_EXECUTION_LOG.md`
- `CONTROL/07_CODEX_GOAL_REGISTRY.md`
- `CONTROL/18_ARTIFACT_REGISTRY.md`
- `CONTROL/19_STAGE_DASHBOARD.md`
- `CONTROL/20_BLOCKER_LOG.md`
- `CONTROL/24_CURRENT_STAGE_STATE.md`
- `CONTROL/25_NEXT_ACTION_QUEUE.md`
- `CONTROL/27_CHECKPOINT_LOG.md`
- `RUNLOG/LONG_RUN_CURRENT.md`
- `RUNLOG/LONG_RUN_SUMMARY.md`

## Review Artifacts To Create

- `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_PACKET.md`
- `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_RESPONSE.md` after GPT Pro answers
- `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_ACTION_ITEMS.md` after GPT Pro answers
- `reviews/stage_03/CODEX_REVIEW_SUMMARY.md`
- `reviews/stage_03/STAGE_ACCEPTANCE_RESULT.md`
- `reviews/stage_03/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md`
- `deployments/stage_03/GITHUB_PR.md`

## GitHub Deployment Actions

Use the active Stage 03 PR route unless GPT Pro or Codex explicitly requires a replacement PR:

- Active closeout PR: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10`
- Branch: `stage/03-source-connectors-closeout-refresh`

Before implementation code starts, the goal draft commit must:

- pass local governance checks;
- push to PR #10 or a documented replacement branch;
- pass GitHub CI on the live PR head;
- receive Codex no-major for the live head or resolve all critical findings.

## GPT Pro Review Actions

Submit `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_PACKET.md` to:

`https://chatgpt.com/g/g-p-6a035355560081918d4a66ef7c70a14e/c/6a131602-2de0-83ea-8b92-09691d87ad89`

GPT Pro must answer:

- PASS: implementation may begin under this goal.
- CONDITIONAL PASS: only non-critical/deferred items may remain; critical items must be fixed before implementation.
- FAIL: implementation remains blocked.

If GPT Pro permits implementation, save the response and action items before creating connector code.

## Phase Gate Requirements

| Gate | Required Evidence Before Implementation Starts |
| --- | --- |
| Scope | GPT Pro confirms the goal is connector normalization only. |
| Functionality | Goal maps connectors to existing Stage 02 source/document schemas. |
| Tests | Mocked fixture test plan and no-network enforcement are explicit. |
| Docs | Architecture and command docs define connector boundaries and provenance. |
| Logs | Goal registry, action queue, current state, artifact registry, and RunLog are updated. |
| GitHub | Live PR head has CI PASS and Codex no-major for the goal draft. |
| GPT Pro | GPT Pro implementation-goal review PASS or accepted CONDITIONAL PASS. |
| Product governance | `finsignal-product-governor` boundary is preserved. |
| Security | No secrets, live credentials, paid API assumptions, or network-dependent CI. |
| Next stage | Implementation remains bounded to Stage 03 and cannot advance to Stage 04. |

## Skills

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

Implementation subagents may run only after GPT Pro accepts this goal:

| Subagent | Responsibility | Allowed Files | Forbidden Files |
| --- | --- | --- | --- |
| `openalex-agent` | OpenAlex fixture mapping and tests | OpenAlex connector slice and shared fixture docs | non-OpenAlex connectors, extraction, MCP tools |
| `crossref-agent` | Crossref fixture mapping and tests | Crossref connector slice and shared fixture docs | non-Crossref connectors, extraction, MCP tools |
| `semantic-scholar-agent` | Semantic Scholar fixture mapping and tests | Semantic Scholar connector slice and shared fixture docs | non-Semantic Scholar connectors, extraction, MCP tools |
| `arxiv-agent` | arXiv fixture mapping and tests | arXiv connector slice and shared fixture docs | non-arXiv connectors, extraction, MCP tools |
| `user-upload-agent` | Uploaded metadata normalization fixture and tests | user-upload metadata connector slice | full document parsing or extraction |
| `connector-review-agent` | Read-only provenance/no-network/security review | logs and review summary only | implementation files unless explicitly assigned |

Each subagent must write `logs/subagents/stage_03/<agent_name>.md` with files touched, summary, risks, tests, and unresolved issues.

## Stop Conditions

Stop and log a blocker if:

- a connector requires API keys, private credentials, login, paid API access, or secrets;
- normal tests require live external network calls;
- connector output requires evidence extraction, LLM adapters, claim graph logic, research delta computation, or MCP business tool exposure;
- implementation requires Stage 02 schema or migration changes without a prior blocker and ADR;
- user-upload work becomes full document parsing rather than metadata normalization;
- source licensing or terms create ambiguity requiring user or GPT Pro decision;
- GitHub CI, Codex review, or GPT Pro implementation-goal review is missing.

## Activation Status

Drafted after PR #10 live head `1f03defb437a9f6f2b694a2697754faa1e1ea7f0` passed CI and Codex no-major. Implementation is still not active until this goal draft itself passes PR #10 live-head CI/Codex after push and GPT Pro accepts the implementation goal.
