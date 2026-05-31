# Stage 03 GPT Pro Review Response

## Review Route

- Submitted through an off-screen Microsoft Edge Default profile controlled through CDP.
- GPT Pro conversation URL: `https://chatgpt.com/c/6a1a9671-ea5c-83ea-ac02-02a8c659c6da`
- No password, verification code, API key, token, payment data, or secret was entered.
- Submission used the Stage 03 review packet and PR #9 evidence.

## Encoding Note

The initial raw page-text capture contained mojibake in the saved transcript. This file records the extracted, readable review result and required action items. The follow-up GPT Pro submission must ask GPT Pro to confirm that this normalized response accurately reflects the CONDITIONAL PASS decision and that B-0040 is resolved after refreshed PR evidence.

## Verdict

`CONDITIONAL PASS`

## Readable Response Summary

GPT Pro judged the Stage 03 planning content itself acceptable: the scope is limited to OpenAlex, Crossref, Semantic Scholar, arXiv, user upload metadata, a connector base interface, and mapping provider outputs into the existing Stage 02 `SourceCreate` and `DocumentCreate` schemas. It also confirmed that the plan explicitly excludes connector implementation, live external calls, evidence extraction, claim graph work, MCP business tools, UI behavior, reports, stock/investment functions, and generic RAG behavior.

GPT Pro did not grant final PASS because the repository artifacts appeared stale relative to the PR #9 timeline. The PR timeline showed head `ce5b94a4ffdad3b08488fb8f7a6952e12a58b4af`, passing CI, and Codex no-major evidence, while some committed artifacts still referenced older `4c81fe9` / CR-03-005 blocker wording.

## Must Fix Before Implementation Planning

1. Ensure all Stage 03 gate artifacts remove stale `4c81fe9` / CR-03-005-blocked wording unless it is explicitly historical.
2. Ensure `reviews/stage_03/GPT_PRO_REVIEW_PACKET.md`, `CHECKLISTS/STAGE_03_CHECKLIST.md`, `CONTROL/*`, and `RUNLOG/*` reflect the current gate state or defer to live PR-head verification after a later push.
3. Record exact-head command evidence for `gh pr view 9 --json headRefOid`, `gh pr checks 9`, and Codex no-major for the exact current PR head.
4. Commit corrected review packet and gate artifacts back to PR #9.
5. Keep Stage 03 implementation blocked until a separate approved `/goal` exists.

## Deferrable Items

Live provider API probes, real API keys, paid/private APIs, provider rate-limit tuning beyond mocked behavior, full-text upload parsing, evidence extraction, claim graph, research delta, RAG answering, dashboards, reports, investment advice, and stock prediction are deferrable and not part of Stage 03 planning.

## Product Alignment

GPT Pro confirmed that the plan preserves Research Mode evidence-stream value by treating connectors as source metadata normalization, not answer generation or generic summarization. Provider-specific metadata should stay in `SourceCreate.bibliographic_metadata`, `DocumentCreate.transformation_notes`, existing validation status, or Stage 02 `ToolCallLog`, not new Stage 02 schema fields.

## Testing Judgment

GPT Pro confirmed no-network mocked testing is sufficient for Stage 03 because the stage value is connector contract, mapping, provenance, fixtures, deterministic behavior, mocked retry/rate-limit handling, and malformed fixture handling. Live network probes may only be optional/manual and outside default CI.

## Stage 03 Implementation Requirements If Later Authorized

- Create `apps/api/finsignalhub_api/connectors/` with a base interface and provider-specific fixture-backed implementations.
- Add OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata connectors.
- Emit only existing Stage 02 `SourceCreate`, `DocumentCreate`, and `ToolCallLog` compatible outputs.
- Do not change Stage 02 schemas, migrations, domain models, or persisted contracts.
- Store provider-specific metadata in `SourceCreate.bibliographic_metadata`.
- Store transformation choices in `DocumentCreate.transformation_notes`.
- Represent tool-call lineage through Stage 02 `ToolCallLog`.
- Add `apps/api/tests/test_stage03_connectors.py`.
- Add fixtures under `apps/api/tests/fixtures/stage03_connectors/`.
- Enforce no-network default CI.
- Include tests for source identity, source type, URL, DOI, locator, provider metadata, retrieval/publication times, validation status, transformation notes, deterministic errors, mocked retry/rate-limit behavior, and malformed fixture handling.
- Require exact PR-head CI, Codex no-major, and final GPT Pro review before merge.

## Stop Conditions

Stop connector implementation if any connector requires secrets, credentials, login, paid/private API keys, live-network default CI, Stage 02 schema/migration changes, user-upload full-text parsing/chunking/extraction/RAG ingestion, summary/research-delta/claim-graph/dashboard/report/ranking/investment/advice output, unsafe licensing/provenance ambiguity, or stale PR-head evidence.
