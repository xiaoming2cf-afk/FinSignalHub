# Semantic Scholar Agent Report

## Files touched

- `logs/subagents/stage_03/semantic-scholar-agent.md`

## Summary

Scope reviewed against `AGENTS.md`, `PLANS/STAGE_03_IMPLEMENTATION_GOAL.md`, `apps/api/finsignalhub_api/schemas/domain.py`, and `apps/api/finsignalhub_api/models/enums.py`. This report is mapping-only for Research Mode source connector primitives. No business code, evidence extraction, claim graph logic, MCP tools, UI, RAG, stock/investment behavior, tests, shared schemas, or live network calls were added.

Semantic Scholar provider metadata should normalize into existing Stage 02 `SourceCreate` and `DocumentCreate` payloads without changing domain schemas:

- `source_identity`: prefer `semantic_scholar:{paperId}` when `paperId` exists; otherwise use a deterministic external identifier fallback such as `doi:{DOI}` or `arxiv:{ArXiv}` from `externalIds`.
- `source_type`: default to `SourceType.LITERATURE`; use `SourceType.PREPRINT` only when fixture metadata explicitly identifies a preprint source such as arXiv. Do not infer financial, dashboard, RAG, or recommendation behavior.
- `title`: map from Semantic Scholar `title`; missing title should produce a deterministic connector validation error rather than an invalid `DocumentCreate`.
- `url`: map from provider paper `url` when present. Keep PDF/open-access URLs inside provider metadata unless the connector contract explicitly chooses one as the source URL.
- `doi`: map from `externalIds.DOI` with normalization limited to string cleanup, not resolver calls.
- `locator`: use a provider locator such as `paperId:{paperId}` and include secondary locators like `corpusId` or external IDs in `bibliographic_metadata`.
- `publication_time`: use a timezone-aware datetime only when the fixture provides an exact parseable publication date. Preserve year-only or partial dates as raw metadata to avoid false precision.
- `retrieval_time`: inject a fixture or mocked retrieval timestamp; never depend on live Semantic Scholar network time in normal tests.
- `bibliographic_metadata`: preserve provider name, `paperId`, `corpusId`, `externalIds`, venue/journal/publication venue, authors, publication types, fields of study, citation counts, open-access PDF metadata, raw publication fields, and provider record hash if available. Abstract text may remain provider metadata but must not become an evidence item.
- `validation_status`: use `ValidationStatus.PENDING` unless later validation logic explicitly changes it.
- `DocumentCreate`: mirror source identity, type, retrieval time, publication time, URL, DOI, and locator from the normalized source; set `normalized_document_ref` to the stable provider identity; set `transformation_notes` to metadata-only normalization with no evidence/full-text extraction.

Tool-call lineage is not a direct field on `SourceCreate` or `DocumentCreate`; Stage 03 should preserve it through the connector envelope, companion `ToolCallLogCreate` records, output artifact IDs, or provider metadata without mutating Stage 02 schemas.

## Risks

- Identifier precedence can create duplicate records if DOI, arXiv ID, and `paperId` conflict across fixtures.
- Year-only publication data can be accidentally converted into a fake exact date.
- Open-access PDF URLs can drift into full-text retrieval or evidence extraction if not kept metadata-only.
- Citation metrics can be mistaken for research judgment; they should remain provider metadata only.
- Missing required `DocumentCreate.title` needs deterministic validation behavior.
- `SourceType.PREPRINT` classification should stay conservative to avoid unsupported inference.
- Direct lineage fields are absent from Stage 02 source/document schemas, so the Stage 03 base contract must define where connector lineage is carried.

## Tests

- Fixture-only Semantic Scholar mapping test for a normal paper with `paperId`, DOI, exact publication date, authors, venue, and provider URL.
- Fixture-only fallback test for missing `paperId` with DOI or arXiv external ID.
- Fixture-only partial-date test proving year-only data remains metadata and does not create false `publication_time`.
- Fixture-only missing-title test expecting deterministic connector validation failure.
- No-network audit proving tests do not call Semantic Scholar, DOI resolvers, PDF URLs, API keys, paid services, login flows, or current wall-clock provider endpoints.
- Schema compatibility assertions for `SourceCreate` and `DocumentCreate` using `SourceType` and `ValidationStatus` enums from Stage 02.
- Negative scope scan to ensure no evidence item, claim graph, research delta, MCP, UI, RAG, stock, investment, or live network behavior appears in the Semantic Scholar slice.

## Unresolved issues

- Confirm the Stage 03 connector envelope or logging contract that carries tool-call lineage for source/document outputs without changing Stage 02 schemas.
- Confirm whether `openAccessPdf.url` may ever become the normalized `url` fallback, or must always remain provider metadata only.
- Confirm exact deterministic error shape for invalid provider records before implementation tests are written.
