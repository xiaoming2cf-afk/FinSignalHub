# Crossref Agent Provider Mapping and Test-Risk Report

Timestamp: 2026-05-30T17:19:39-05:00

## Files Touched

- `logs/subagents/stage_03/crossref-agent.md`

## Summary

Scope reviewed: Stage 03 Research Mode source connector primitives only. No business code, evidence extraction, claim graph logic, MCP tools, UI, RAG behavior, stock or investment behavior, live network calls, shared code, or tests were implemented.

Crossref provider mapping for fixture-backed Work metadata:

| Crossref field | Stage 02 target | Mapping note |
| --- | --- | --- |
| `DOI` | `SourceCreate.doi`, `DocumentCreate.doi` | Normalize case and trim URL prefixes; prefer DOI as the stable external locator. |
| `DOI` | `source_identity` | Use `doi:<normalized-doi>` when present. |
| `title[0]` | `title` | First title string becomes the source/document title; fixture tests should cover missing or empty title. |
| `URL` | `url` | Prefer Crossref URL when provided; otherwise derive DOI URL only if DOI exists. |
| `type` | `source_type` | Map journal/book/proceedings/article types to `SourceType.LITERATURE`; map `posted-content` to `SourceType.PREPRINT`; map dataset-like records to `SourceType.DATASET` only when Crossref type is explicit. |
| `issued`, `published-print`, `published-online` | `publication_time` | Choose the earliest deterministic publication date available, normalize partial date-parts to a timezone-aware UTC timestamp by documented rule. |
| fixture retrieval timestamp | `retrieval_time` | Use deterministic fixture time in tests; do not depend on live request time for normal tests. |
| `container-title`, `publisher`, `author`, `ISSN`, `ISBN`, `volume`, `issue`, `page`, `license`, `subject`, `funder`, `reference-count`, `relation`, `prefix`, `member` | `SourceCreate.bibliographic_metadata` | Preserve provider-specific metadata needed for auditability without treating it as evidence text. |
| Crossref API route and normalized DOI | `locator`, `normalized_document_ref` | Use a deterministic provider locator such as `crossref:work:<normalized-doi>`; no full-text parsing. |
| provider transform description | `DocumentCreate.transformation_notes` | Record metadata-only normalization and field fallback choices. |
| fixture validation outcome | `validation_status` | Default to `ValidationStatus.PENDING`; mark rejected only for deterministic malformed fixtures. |
| connector invocation metadata | `ToolCallLogCreate` side artifact | Preserve tool-call lineage through planned Stage 03 connector contract and `ToolCallLog`, not by changing `SourceCreate` or `DocumentCreate`. |

## Risks

- Crossref date-parts may be partial or contain multiple publication fields; tests need deterministic precedence and partial-date normalization.
- Some records may lack DOI, title, URL, or publication date; implementation must either reject deterministically or produce schema-compatible fallbacks without schema changes.
- Crossref `type` values are broader than the current `SourceType` enum; unsupported types should remain literature unless explicitly dataset/preprint, with the raw Crossref type preserved in metadata.
- `SourceCreate` has no `transformation_notes` or lineage field; provenance must be split across `SourceCreate.bibliographic_metadata`, `DocumentCreate.transformation_notes`, and `ToolCallLogCreate`.
- License and availability metadata can be present but does not grant full-text rights; connector primitives must not infer evidence extraction permission.

## Tests

- No tests were edited or run by this subagent.
- Future fixture tests should cover DOI normalization, type-to-`SourceType` mapping, missing title/DOI behavior, partial date-parts, provider metadata preservation, deterministic validation status, and no-network enforcement.
- Tests should use mocked Crossref Work payloads only and fail if HTTP/network access is attempted.

## Unresolved Issues

- Exact fallback policy for Crossref records without DOI remains a connector-contract decision.
- Exact publication-date precedence should be documented before implementation.
- The final lineage shape depends on the Stage 03 base connector contract and `ToolCallLogCreate` usage, not on schema changes.
