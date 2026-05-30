# arxiv-agent Stage 03 Mapping and Test-Risk Report

## Scope

Research Mode arXiv metadata connector primitive only. This report does not implement connector code, evidence extraction, claim graph logic, MCP tools, UI behavior, RAG behavior, stock or investment features, live network access, ingestion jobs, or full business behavior.

## Files Touched

- `logs/subagents/stage_03/arxiv-agent.md`

## Context Read

- `AGENTS.md`
- `PLANS/STAGE_03_IMPLEMENTATION_GOAL.md`
- `apps/api/finsignalhub_api/schemas/domain.py`
- `apps/api/finsignalhub_api/models/enums.py`

## Summary

The arXiv connector should normalize fixture-provided preprint metadata into existing Stage 02 schema payloads without schema or migration changes.

Expected `SourceCreate` mapping:

| arXiv metadata | `SourceCreate` field | Notes |
| --- | --- | --- |
| arXiv id, versioned id, or canonical abs URL | `source_identity` | Prefer stable `arxiv:<id>` identity; keep version in `bibliographic_metadata` if present. |
| arXiv preprint | `source_type` | Use `SourceType.PREPRINT`. |
| Title | `title` | Preserve normalized title text only; no summary generation. |
| Canonical abs URL | `url` | Use arXiv abstract URL, not PDF fetch by default. |
| DOI, if present in metadata | `doi` | Optional; do not synthesize. |
| arXiv category or version locator | `locator` | Use concise locator such as primary category or versioned arXiv id. |
| Published or updated timestamp | `publication_time` | Use provider timestamp if fixture includes timezone-safe value. |
| Fixture retrieval timestamp | `retrieval_time` | Required; must be deterministic in tests. |
| Authors, categories, abstract, comments, journal ref, license, version, provider ids | `bibliographic_metadata` | Store provider-specific fields here; do not add unsupported schema fields. |
| Fixture validation outcome | `validation_status` | Use `PENDING` unless fixture validation rules prove a stronger state. |

Expected `DocumentCreate` mapping:

| arXiv metadata | `DocumentCreate` field | Notes |
| --- | --- | --- |
| Stage 02 source id from created source | `source_id` | Provided by persistence/service layer, not by arXiv fixture. |
| Title | `title` | Required. |
| Normalized local metadata reference | `normalized_document_ref` | Optional deterministic fixture ref, not a downloaded PDF path. |
| `arxiv:<id>` | `source_identity` | Match `SourceCreate.source_identity`. |
| Preprint source type | `source_type` | Use `SourceType.PREPRINT`. |
| Fixture retrieval timestamp | `retrieval_time` | Required. |
| Published or updated timestamp | `publication_time` | Optional but should match source when available. |
| Canonical abs URL | `url` | Same provider URL as source. |
| DOI if present | `doi` | Optional. |
| arXiv category/version locator | `locator` | Match source locator where useful. |
| Normalization notes | `transformation_notes` | State that data came from arXiv metadata fixture, with no live network call and no evidence extraction. |
| Fixture validation outcome | `validation_status` | Use `PENDING` unless validation criteria are explicit. |

Tool-call lineage should be represented through a separate Stage 02 `ToolCallLogCreate` record with deterministic `tool_name`, `schema_version`, `called_at`, `argument_hash`, safe arguments, output artifact ids, and `SUCCEEDED` or deterministic failure status. `DocumentCreate` does not include a lineage field, so the connector must not add one.

## Risks

- arXiv may expose multiple identifiers for the same preprint; tests should cover bare id, versioned id, and canonical URL normalization.
- arXiv metadata can include absent DOI, absent journal reference, multiple categories, multiline abstracts, HTML/XML escaping, and non-UTC timestamps.
- Default tests must not hit live arXiv endpoints. Any live probe would violate the Stage 03 normal CI boundary unless explicitly optional and manually invoked.
- Abstract text is metadata only at this stage. It must not become evidence extraction or claim generation.
- Provider-specific fields must stay in `bibliographic_metadata` or `transformation_notes`; Stage 02 schemas should not be changed for arXiv convenience.

## Tests

Recommended mocked fixture tests for later implementation:

- Valid arXiv fixture maps to one `SourceCreate` payload and one `DocumentCreate` payload with `SourceType.PREPRINT`.
- Missing DOI remains `None`; DOI is not inferred from comments or journal reference.
- Versioned id preserves stable `source_identity` and records version metadata without changing the source/document schema.
- Fixture retrieval timestamp is deterministic and timezone-aware.
- Abstract and author metadata are stored in `bibliographic_metadata`; no `EvidenceItemCreate`, claim, delta, MCP, UI, or Repro Pack output is created.
- Network calls are blocked or mocked in default tests.
- Malformed required metadata produces deterministic connector errors and a failed `ToolCallLogCreate` shape rather than partial source/document payloads.

No tests were run for this report because no connector code, fixtures, or tests were implemented.

## Unresolved Issues

- Exact arXiv fixture format is still to be selected during implementation.
- The connector base contract should define whether `publication_time` uses arXiv `published` or `updated` when both exist.
- License and availability fields have no first-class Stage 02 schema fields; they should remain in `bibliographic_metadata` unless a later approved ADR changes the schema.
- Final no-network enforcement approach must be chosen by the implementation owner before tests are added.
