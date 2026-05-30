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

## Planned Connectors

- OpenAlex: literature metadata from fixture responses.
- Crossref: DOI and publication metadata from fixture responses.
- Semantic Scholar: paper metadata and external ids from fixture responses.
- arXiv: preprint metadata from fixture responses.
- User upload metadata: local file metadata and user-provided citation fields, not document parsing or extraction.

## No-Network Rule

Normal tests and CI must use fixture data and mocked clients. Live network probes, if ever needed, must be optional, manually invoked, and excluded from default CI.

## Forbidden Boundaries

Stage 03 must not extract evidence, classify relations, compute claim graphs, generate research deltas, expose MCP business tools, produce reports, or provide financial/investment advice.
