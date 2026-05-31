# Stage 03 Source Connector Architecture Plan

## Purpose

Define a Research Mode source connector layer that normalizes source metadata into provenance-preserving `Document` records for later evidence workflows.

## Connector Contract

Each future connector should accept a query or source reference and return a candidate that can be converted into the existing Stage 02 schemas without model or migration changes.

Persisted source payloads must match `SourceCreate`:

- `project_id`
- `source_identity`
- `source_type`
- `title`
- `url`
- `doi`
- `locator`
- `publication_time`
- `retrieval_time`
- `bibliographic_metadata`
- `validation_status`

Persisted document payloads must match `DocumentCreate`:

- `project_id`
- `source_id`
- `title`
- `normalized_document_ref`
- `source_identity`
- `source_type`
- `retrieval_time`
- `publication_time`
- `url`
- `doi`
- `locator`
- `transformation_notes`
- `validation_status`

Connector-specific fields that are not accepted by `DocumentCreate`, such as authors, abstract text, external ids, license notes, raw provider ids, and provider-specific confidence hints, must be retained in `SourceCreate.bibliographic_metadata` or summarized in `DocumentCreate.transformation_notes`. Tool-call lineage must be represented by Stage 02 `ToolCallLog` records and artifact references, not by adding an unsupported field to `DocumentCreate`.

The connector contract must use deterministic errors, must not require secrets in normal tests, and must not require Stage 02 schema or migration changes unless a later plan explicitly records a cross-stage exception.

## Implemented Stage 03 Primitives

Stage 03 now includes fixture/local metadata normalizers under `apps/api/finsignalhub_api/connectors/`:

- `normalize_openalex_record`
- `normalize_crossref_record`
- `normalize_semantic_scholar_record`
- `normalize_arxiv_record`
- `normalize_user_upload_metadata`

Each normalizer returns a `NormalizedConnectorResult` with:

- `source_payload`: validates as `SourceCreate`.
- `document_payload_seed`: validates as `DocumentCreate` after the persistence layer supplies `source_id`.
- `tool_call_payload`: validates as `ToolCallLogCreate`.
- `provider_metadata`: sanitized provider metadata retained for provenance.

The connector package has no default network client. It performs deterministic metadata mapping only.

## Provider Mapping

- OpenAlex: maps work id, DOI, title, publication date, landing page, host venue, license, and authors into literature source/document payloads.
- Crossref: maps DOI, URL, title, issued or published date parts, container title, publisher, type, and authors into literature source/document payloads.
- Semantic Scholar: maps paper id, DOI, arXiv id, corpus id, venue, publication date, publication type, and authors into literature source/document payloads.
- arXiv: maps bare ids, versioned ids, canonical arXiv URLs, PDF URLs, and old-style dotted archive classes such as `physics.ins-det/0301001` or `physics.atom-ph/9901001` into stable `arxiv:<id>` source identity, keeps the versioned id as locator/provider metadata, canonicalizes the abstract URL, and maps DOI, title, publication/update time, category, links, and authors into preprint source/document payloads.
- User upload metadata: maps caller-provided file metadata, hash, citation fields, DOI, URL, and optional metadata into `user_upload_metadata` source/document payloads. It does not parse file content.

## Tool Call Lineage

`ToolCallLogCreate` payloads record the provider normalizer name, schema version, retrieval time, deterministic argument hash, sanitized safe arguments, and `succeeded` status. Core safe-argument provenance fields (`provider`, `query_ref`, `fixture`, `fixture_id`, and `source_identity`) are canonical and cannot be overwritten by extra fixture arguments; extras are sanitized under the `extra` key. `input_artifact_ids` and `output_artifact_ids` are intentionally omitted by normalizers because source and document IDs do not exist until the persistence step creates records. A later bounded persistence step may update those artifact IDs after creation without changing Stage 02 schemas.

arXiv tool-call lineage uses the stable source identity in `safe_arguments.source_identity`. Versioned ids and raw URL-shaped ids remain visible in sanitized provider metadata so replay can distinguish fixture input shape without fragmenting the source identity across preprint versions.

## Sanitization

Connector metadata and safe arguments redact key names containing `api_key`, `apikey`, `authorization`, `password`, `secret`, or `token`. This is a defensive control for fixture and user-upload metadata; it is not a substitute for keeping secrets out of inputs.

## No-Network Rule

Normal tests and CI use fixture data only. The Stage 03 connector modules must not import `httpx`, `requests`, `urllib.request`, or `socket` in default connector code. Live network probes, if ever needed, must be optional, manually invoked, and excluded from default CI.

## Forbidden Boundaries

Stage 03 must not extract evidence, classify relations, compute claim graphs, generate research deltas, expose MCP business tools, produce reports, or provide financial/investment advice.
