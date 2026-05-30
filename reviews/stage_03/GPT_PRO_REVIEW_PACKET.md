# GPT Pro Review Packet: Stage 03 Source Connectors Final Implementation

Please review FinSignalHub Stage 03 final implementation after the current implementation branch head is pushed, CI passes, and Codex review completes.

This packet supersedes the historical Stage 03 planning packet. Do not use stale PR #9 evidence. The active route is PR #10.

## Project Identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. It serves researchers, PhD students, labs, research teams, research-oriented product teams, and innovation teams.

Core outputs remain research delta, claim graph, evidence card, literature matrix, method card, dataset card, Repro Pack, and tool call log.

Forbidden directions remain chatbot, generic RAG, stock prediction, investment advice, ordinary report generator, standalone dashboard behavior, model leaderboard, Risk Mode, and Replay Engine.

## Stage 03 Goal

Implement source connector primitives for:

- OpenAlex
- Crossref
- Semantic Scholar
- arXiv
- user-upload metadata

The implementation must normalize metadata into existing Stage 02-compatible `SourceCreate`, `DocumentCreate`, and `ToolCallLogCreate` payloads. It must preserve source identity, source type, retrieval time, publication time, DOI/URL/locator/external IDs, provider metadata, transformation notes, validation status, and tool-call lineage data without changing Stage 02 migrations or schemas.

## Actual Implementation

- Added `apps/api/finsignalhub_api/connectors/` with a shared connector contract and provider normalizers.
- Added fixture-only tests in `apps/api/tests/test_stage03_connectors.py`.
- Added provider fixtures under `apps/api/tests/fixtures/stage03_connectors/`.
- Added connector package and fixture README files.
- Updated Stage 03 architecture and command docs.
- Updated Stage 03 PR body, acceptance, dashboards, logs, subagent summary, artifact registry, and checkpoint log.
- Updated the Stage 02 forbidden-scope guard so Stage 03-approved connector provider names are allowed only inside the connector package while forbidden Stage 04+ behaviors remain blocked.
- Remediated Codex CR-03-041 by preventing `extra_safe_arguments` from overriding canonical `ToolCallLog.safe_arguments` provenance fields. Extra fixture arguments now live under `safe_arguments.extra`, and regression coverage verifies spoofed `provider`, `fixture`, `fixture_id`, `query_ref`, and `source_identity` values cannot replace canonical fields.

## Explicit Non-Implementation

Stage 03 still does not implement:

- live external API clients or default network calls;
- evidence extraction, quote-span extraction, or LLM adapters;
- claim graph computation or Research Delta computation;
- MCP business tools, ChatGPT/Claude/Copilot/Gemini connector implementation, or Repro Pack export;
- admin UI product behavior, dashboard behavior, chatbot behavior, generic RAG, reports, stock prediction, investment advice, Risk Mode, Replay Engine, auth, or billing.

## Local Tests

Before push, Codex ran:

- `python -m pytest apps/api/tests/test_stage03_connectors.py -q` -> 15 passed.
- `python -m pytest apps/api/tests -q --maxfail=1` -> 68 passed.
- `python -m compileall apps/api/finsignalhub_api` -> passed.
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03` -> passed.
- no-network import scan over connector code -> passed.
- forbidden Stage 04+ schema/artifact scan over connector code -> passed.
- high-confidence secret scan excluding placeholder examples -> passed.
- `git diff --check` -> passed with only normal Windows line-ending warnings.

## GitHub And Codex Evidence

Active PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10

At GPT Pro submission time, Codex must insert:

- current implementation branch head;
- current CI job URLs;
- current Codex review result;
- any critical findings and fixes;
- final PR body state.

If any current-head CI or Codex evidence is missing, GPT Pro must return FAIL or CONDITIONAL PASS and Stage 03 must remain blocked.

## Known Limitations

- Normalizers omit `input_artifact_ids` and `output_artifact_ids` because source/document IDs are created by persistence after payload validation. A later bounded persistence step may update `ToolCallLog` artifact IDs without changing Stage 02 schemas.
- No live provider API behavior is included; all default tests use fixtures.
- User-upload handling is metadata-only and does not parse documents.

## Questions For GPT Pro

Please answer:

1. PASS / CONDITIONAL PASS / FAIL for Stage 03 final implementation.
2. Must-fix issues before Stage 03 can close.
3. Deferrable items.
4. Whether implementation preserves Research Mode-first, MCP-first, evidence-stream product direction.
5. Whether the connector payloads sufficiently preserve provenance for later evidence cards, literature matrices, method cards, dataset cards, claim graph work, research delta, and Repro Pack stages.
6. Whether no-network fixture testing is sufficient for Stage 03.
7. Whether any forbidden Stage 04+ behavior leaked into Stage 03.
8. If PASS, provide exact Stage 04 planning requirements, files, tests, risks, and stop conditions.

Do not authorize Stage 04 implementation. If PASS, authorize Stage 04 planning only.
