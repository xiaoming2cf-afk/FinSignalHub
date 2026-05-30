# GPT Pro Implementation Goal Review Response: Stage 03

Timestamp: 2026-05-30T15:51:25-05:00

Target GPT Pro page: https://chatgpt.com/g/g-p-6a035355560081918d4a66ef7c70a14e/c/6a131602-2de0-83ea-8b92-09691d87ad89

Submitted packet: `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_PACKET.md`

Live GitHub evidence submitted with the packet:

- PR #10: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10
- Head: `8f10f95c69c3eaf7d6ada7b878e017b917929e33`
- CI PASS:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26693919817/job/78675014690
  - https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26693921040/job/78675017595
- Codex no-major:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10#issuecomment-4584553889

## Verdict

```text
VERDICT: PASS
```

GPT Pro accepted the Stage 03 implementation `/goal` draft and authorized Stage 03 source connector primitives only under the accepted goal scope.

## Response

```text
VERDICT: PASS

MUST FIX BEFORE IMPLEMENTATION:

Save this GPT Pro response and action items under reviews/stage_03/.

Update reviews/stage_03/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md.

Update CONTROL/24_CURRENT_STAGE_STATE.md, CONTROL/25_NEXT_ACTION_QUEUE.md, RUNLOG/LONG_RUN_CURRENT.md, and CONTROL/18_ARTIFACT_REGISTRY.md.

Confirm the implementation branch head still has CI PASS and current-head Codex no-major before connector code starts.

DEFERRED ITEMS:

Broader connector edge-case expansion.

Richer fixture coverage beyond the required minimum.

Advanced rate-limit/retry policy hardening.

Connector performance optimization.

Any Stage 04+ extraction, claim graph, delta, Repro Pack, or MCP business-tool behavior.

AUTHORIZED IMPLEMENTATION SCOPE:

Implement Stage 03 source connector primitives only.

Allowed connector targets: OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata.

Normalize source metadata into existing Stage 02-compatible SourceCreate, DocumentCreate, and ToolCallLog payloads.

Preserve source identity, source type, retrieval timestamp or fixture timestamp, URL/DOI/external locator, provider metadata, transformation notes, validation status, and tool-call lineage.

Allowed files:

apps/api/finsignalhub_api/connectors/

apps/api/tests/test_stage03_connectors.py

apps/api/tests/fixtures/stage03_connectors/

docs/architecture/stage_03_source_connectors.md

docs/codex/stage_03_commands.md

logs/subagents/stage_03/

reviews/stage_03/

deployments/stage_03/

required CONTROL/, RUNLOG/, checklist, task, and changelog governance records.

Forbidden: evidence extraction, LLM adapters, claim graph computation, Research Delta computation, MCP business tools, Repro Pack export logic, admin UI product behavior, chatbot behavior, generic RAG, stock prediction, investment advice, dashboard behavior, Risk Mode, Replay Engine, auth, billing, live external API tests in CI, API keys, credentials, paid API assumptions, or full document parsing for user upload.

REQUIRED TESTS:

pytest apps/api/tests/test_stage03_connectors.py

mocked fixture tests only

no-network CI enforcement

OpenAlex fixture mapping test

Crossref fixture mapping test

Semantic Scholar fixture mapping test

arXiv fixture mapping test

user-upload metadata fixture test

SourceCreate and DocumentCreate compatibility tests

publication/release time mapping tests

DOI, URL, locator, external id, source identity, and source type mapping tests

provider metadata and transformation notes tests

rate-limit/retry behavior with mocks if retry handling exists

secret scan

forbidden-scope scan

python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03

git diff --check

CI PASS and current-head Codex no-major before final GPT Pro implementation review.

REQUIRED SUBAGENTS:

openalex-agent

crossref-agent

semantic-scholar-agent

arxiv-agent

user-upload-agent

connector-review-agent

Each subagent must stay within bounded file authority and write logs/subagents/stage_03/<agent_name>.md.

STOP CONDITIONS:

A real API key, private credential, paid API account, login, or secret is required.

Normal tests require live external network calls.

Connector work starts generating EvidenceItem.

Any LLM adapter, extraction pipeline, claim graph, Research Delta, Repro Pack, MCP business tool, dashboard, chatbot/RAG, stock prediction, investment advice, Risk Mode, Replay Engine, auth, or billing behavior appears.

CI or current-head Codex review becomes pending after a new commit.

Implementation requires Stage 02 schema/migration changes without blocker record and ADR.

NEXT CODEX STEPS:

Save this review as reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md.

Save action items as reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_ACTION_ITEMS.md.

Mark the implementation-goal draft as PASS in reviews/stage_03/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md.

Update current stage state, action queue, RunLog, artifact registry, and checkpoint log.

Begin Stage 03 implementation only under the accepted goal scope.

Use the required subagents and create bounded subagent logs.

Implement connector primitives with mocked fixtures and normalized output only.

Run required local checks, CI, current-head Codex review, and final GPT Pro Stage 03 implementation review before accepting Stage 03.

FINAL_STAGE03_IMPLEMENTATION_GOAL_REVIEW
```

