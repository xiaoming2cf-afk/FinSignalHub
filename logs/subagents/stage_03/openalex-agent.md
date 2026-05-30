# OpenAlex Agent Provider Mapping And Test-Risk Report

Timestamp: 2026-05-30

## Files Touched

- `logs/subagents/stage_03/openalex-agent.md`

No shared code, schema files, connector code, fixtures, or tests were edited.

## Summary

Scope reviewed:

- `AGENTS.md`
- `PLANS/STAGE_03_IMPLEMENTATION_GOAL.md`
- `apps/api/finsignalhub_api/schemas/domain.py`
- `apps/api/finsignalhub_api/models/enums.py`

OpenAlex work metadata can map into existing Stage 02 schemas without schema or migration changes:

| OpenAlex field or derived value | `SourceCreate` target | `DocumentCreate` target | Notes |
| --- | --- | --- | --- |
| caller project id | `project_id` | `project_id` | Supplied by FinSignalHub, not OpenAlex. |
| `ids.openalex` or `id` | `source_identity` | `source_identity`, `normalized_document_ref` | Use a stable `openalex:<work-id>` identity; preserve the provider URL in metadata. |
| OpenAlex work type | `source_type` | `source_type` | Default fixture scope should be `SourceType.LITERATURE`; only use other enum values with explicit fixture coverage. |
| `display_name` | `title` | `title` | Missing title should produce a deterministic validation error rather than a vague document. |
| `primary_location.landing_page_url`, DOI URL, or OpenAlex URL fallback | `url` | `url` | Fallback order must be deterministic and documented in transformation notes. |
| `doi` or `ids.doi` | `doi` | `doi` | Normalize DOI shape consistently and test DOI URL vs bare DOI inputs. |
| OpenAlex work id, e.g. `W...` | `locator` | `locator` | Keeps an external locator without adding schema fields. |
| `publication_date` | `publication_time` | `publication_time` | Parse full dates as aware UTC datetimes; do not fabricate month/day from year-only values. |
| fixture or connector retrieval timestamp | `retrieval_time` | `retrieval_time` | Tests must use fixed fixture timestamps. |
| authorships, external ids, type, publication year/date, locations, open access, concepts, license notes, selected provider metadata | `bibliographic_metadata` | none | Provider-specific fields stay in source metadata, not `DocumentCreate`. |
| metadata-only normalization decisions | none | `transformation_notes` | Must state no evidence extraction, no claim graph, no summary, and any fallback choices. |
| connector validation result | `validation_status` | `validation_status` | Start as `ValidationStatus.PENDING` unless a fixture explicitly validates rejection. |
| Stage 02 tool-call lineage | Stage 02 `ToolCallLog` sidecar, not a new source/document field | Stage 02 `ToolCallLog` sidecar, not a new source/document field | Do not add unsupported lineage fields to `DocumentCreate`. |

The OpenAlex connector primitive should remain metadata normalization only. It must not fetch PDFs, reconstruct abstracts into evidence, summarize literature, create evidence items, compute claims, expose MCP tools, call live OpenAlex in normal tests, or produce financial/investment behavior.

## Risks

- OpenAlex DOI values may appear as DOI URLs or bare identifiers; inconsistent normalization could break source identity and duplicate detection.
- OpenAlex publication metadata may include year-only values; converting year-only data into a full datetime would overstate precision.
- URL selection can be ambiguous across `primary_location`, `best_oa_location`, DOI, and provider URLs; tests need a documented fallback order.
- OpenAlex abstracts and concepts can invite out-of-scope evidence extraction or generic summarization; Stage 03 should keep them as provider metadata or omit them with notes.
- OpenAlex work types may not align perfectly with `SourceType`; unsupported types should fail deterministically or remain literature only within fixture scope.
- License and open-access fields describe provider/source metadata only; Stage 03 must not download content or assume reuse rights.
- Any live OpenAlex request in normal tests would violate the no-network rule and should block Stage 03 acceptance.

## Tests

Tests were not run by this report-only subagent because no connector code or test files were edited.

Recommended OpenAlex fixture tests:

- Valid OpenAlex work maps to `SourceCreate` and `DocumentCreate` with `SourceType.LITERATURE`.
- DOI URL and bare DOI inputs normalize consistently.
- Missing DOI still preserves `source_identity`, `locator`, and URL fallback.
- Missing `display_name` returns a deterministic connector validation error.
- Full `publication_date` maps to an aware datetime; year-only metadata does not fabricate a full date.
- Provider-specific fields remain in `SourceCreate.bibliographic_metadata`.
- `DocumentCreate.transformation_notes` records metadata-only normalization and fallback choices.
- Tool-call lineage is represented through Stage 02 `ToolCallLog`-compatible sidecar output, not unsupported document fields.
- Mocked client/fixture tests prove no live network calls, API keys, login, or paid service assumptions.

## Unresolved Issues

- The exact canonical DOI format should be fixed before implementation tests are written.
- The exact URL fallback order should be fixed in the connector contract before implementation.
- OpenAlex type-to-`SourceType` handling should stay literature-only unless fixtures explicitly approve additional enum mappings.
