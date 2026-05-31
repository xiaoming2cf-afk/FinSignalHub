# GPT Pro Review Packet: Stage 03 Implementation Goal Draft

## Request

Please review this Stage 03 implementation `/goal` draft for FinSignalHub. Do not review connector implementation code, because connector code has not started.

Please answer with one of:

- PASS: the implementation goal is acceptable and connector implementation may begin under this goal.
- CONDITIONAL PASS: list critical items that must be fixed before implementation and deferred items that may remain.
- FAIL: explain why implementation must not begin.

If PASS or accepted CONDITIONAL PASS, provide exact implementation requirements, file boundaries, tests, risk controls, and final acceptance steps for Codex to execute next.

## Project Identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. Its primary users are researchers, PhD students, research groups, research-oriented product teams, and innovation project teams. Its core outputs are research delta, claim graph, evidence card, literature matrix, method card, dataset card, and reproducible export pack.

FinSignalHub is not a chatbot, stock recommendation tool, investment adviser, generic RAG system, generic literature summarizer, report generator, financial dashboard, or model leaderboard.

## Prior Gate Evidence

- Stage 02 implementation merged and tagged.
- Stage 03 planning PASS is saved in `reviews/stage_03/GPT_PRO_FOLLOWUP_RESPONSE.md`.
- Stage 03 PR #10 closeout PASS is saved in `reviews/stage_03/GPT_PRO_CLOSEOUT_RESPONSE.md`.
- GPT Pro allowed only drafting Stage 03 implementation `/goal` artifacts next.
- Actual connector implementation remains blocked until this implementation goal is accepted.

## GitHub Evidence Before Draft

- Active PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10
- Live head before drafting this packet: `1f03defb437a9f6f2b694a2697754faa1e1ea7f0`
- CI PASS jobs:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26693379468/job/78673610551
  - https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26693380166/job/78673612338
- Codex no-major response for that head:
  - https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10#issuecomment-4584381224

After this packet is committed and pushed, the live PR head must be checked again. Older CI/Codex evidence must not be treated as proof for the new pushed head.

## Goal Draft Under Review

Primary file:

- `PLANS/STAGE_03_IMPLEMENTATION_GOAL.md`

Companion artifact:

- `reviews/stage_03/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md`

The draft says implementation may start only after this goal draft passes live PR CI/Codex and this GPT Pro review.

## Proposed Stage 03 Implementation Scope

Implement Research Mode source connector primitives for:

- OpenAlex
- Crossref
- Semantic Scholar
- arXiv
- user-upload metadata

The implementation should normalize source metadata into existing Stage 02 `SourceCreate` and `DocumentCreate` schema-compatible payloads. It must preserve source identity, source type, retrieval timestamp or fixture timestamp, URL/DOI/external locator, provider metadata, transformation notes, validation status, and tool-call lineage.

## Explicit Non-Scope

Do not implement:

- evidence extraction;
- LLM adapters;
- claim graph computation;
- research delta computation;
- MCP business tools;
- admin UI product behavior;
- Repro Pack export logic;
- chatbot behavior;
- generic RAG;
- stock prediction;
- investment advice;
- dashboard behavior;
- Risk Mode;
- Replay Engine.

## Allowed Files After Goal Acceptance

- `apps/api/finsignalhub_api/connectors/`
- `apps/api/tests/test_stage03_connectors.py`
- `apps/api/tests/fixtures/stage03_connectors/`
- `docs/architecture/stage_03_source_connectors.md`
- `docs/codex/stage_03_commands.md`
- `logs/subagents/stage_03/`
- `reviews/stage_03/`
- `deployments/stage_03/`
- required `CONTROL/`, `RUNLOG/`, checklist, task, and changelog governance records

## Forbidden Files And Behavior

- No Stage 02 migration or schema behavior change unless a blocker and ADR are created first.
- No live external API tests in normal CI.
- No API keys, private credentials, paid API assumptions, user login, or secrets.
- No connector output that bypasses provenance or ToolCallLog lineage.
- No full document parsing in user-upload work; metadata normalization only.

## Required Tests

At minimum:

- `pytest apps/api/tests/test_stage03_connectors.py`
- mocked fixture tests only;
- no-network CI enforcement;
- OpenAlex fixture mapping test;
- Crossref fixture mapping test;
- Semantic Scholar fixture mapping test;
- arXiv fixture mapping test;
- user-upload metadata fixture test;
- `SourceCreate` and `DocumentCreate` compatibility tests;
- publication/release time mapping tests;
- DOI, URL, locator, external id, source identity, and source type mapping tests;
- provider metadata and transformation notes tests;
- rate-limit/retry behavior with mocks if connector client surfaces retry handling;
- secret scan;
- forbidden-scope scan;
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03`;
- `git diff --check`.

## Required Subagents

After goal acceptance only:

- `openalex-agent`
- `crossref-agent`
- `semantic-scholar-agent`
- `arxiv-agent`
- `user-upload-agent`
- `connector-review-agent`

Each subagent must have bounded file authority and must write `logs/subagents/stage_03/<agent_name>.md`.

## Acceptance Gates

Please judge whether the goal draft sufficiently specifies the ten hard gates:

1. scope
2. functionality
3. tests
4. docs
5. logs
6. GitHub
7. GPT Pro
8. product governance
9. security
10. next stage

Missing live-head GitHub CI/Codex evidence or missing GPT Pro implementation review must keep implementation blocked.

## Questions For GPT Pro

1. Does `PLANS/STAGE_03_IMPLEMENTATION_GOAL.md` sufficiently constrain Stage 03 implementation?
2. Are the allowed files and forbidden files correct?
3. Are the mocked tests and no-network CI requirements sufficient?
4. Is the provenance mapping sufficient for later evidence extraction, claim graph, research delta, literature matrix, method card, dataset card, and repro pack work?
5. Are any critical changes required before connector implementation begins?
6. If implementation may begin, what exact requirements and steps should Codex execute next?

## Requested Output Format

Please answer in this structure:

```text
VERDICT: PASS | CONDITIONAL PASS | FAIL

MUST FIX BEFORE IMPLEMENTATION:
- ...

DEFERRED ITEMS:
- ...

AUTHORIZED IMPLEMENTATION SCOPE:
- ...

REQUIRED TESTS:
- ...

REQUIRED SUBAGENTS:
- ...

STOP CONDITIONS:
- ...

NEXT CODEX STEPS:
1. ...
```
