# Stage 03 Source Connector Architecture Plan

## Purpose

Define a Research Mode source connector layer that normalizes source metadata into provenance-preserving `Document` records for later evidence workflows.

## Connector Contract

Each future connector should accept a query or source reference and return normalized document candidates with:

- `source_identity`
- `source_type`
- `title`
- `abstract_or_description`
- `authors_or_creators`
- `publication_time` or `release_time`
- `retrieval_time`
- `url`
- `doi`
- `external_ids`
- `license_or_terms_note`
- `transformation_notes`
- `confidence`
- `tool_call_lineage`

The connector contract must use deterministic errors and must not require secrets in normal tests.

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
