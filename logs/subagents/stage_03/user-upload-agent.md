# User Upload Agent Report

## Files Touched

- `logs/subagents/stage_03/user-upload-agent.md`

No connector code, tests, fixtures, schemas, models, MCP tools, UI, extraction code, claim graph code, RAG behavior, stock/investment behavior, live network behavior, or business workflow files were created or modified.

## Summary

Product alignment verdict: PASS for metadata normalization only.

The user-upload slice should normalize caller-provided upload metadata into existing Stage 02 schema-compatible payloads. It must not parse uploaded document content, extract evidence, summarize text, classify claims, compute research deltas, expose MCP business tools, or create UI behavior.

Recommended mapping:

- `SourceCreate.project_id`: current research project id supplied by caller.
- `SourceCreate.source_identity`: stable user-upload metadata identity, such as `user-upload:<fixture_id>` or another non-secret upload metadata id.
- `SourceCreate.source_type`: `SourceType.USER_UPLOAD_METADATA`.
- `SourceCreate.title`: caller-provided title, falling back to a safe display filename when title is absent.
- `SourceCreate.url`: optional user-supplied canonical URL only; do not invent a URL from local filesystem paths.
- `SourceCreate.doi`: optional user-supplied DOI metadata only.
- `SourceCreate.locator`: upload metadata locator, storage-safe reference, or display filename; do not store secret-bearing absolute paths.
- `SourceCreate.publication_time`: optional user-supplied publication or release timestamp.
- `SourceCreate.retrieval_time`: upload receipt time or fixture timestamp.
- `SourceCreate.bibliographic_metadata`: safe metadata only, such as filename, declared MIME type, byte size, checksum, supplied author/title fields, upload fixture id, and provider marker `user_upload`.
- `SourceCreate.validation_status`: default `ValidationStatus.PENDING` unless validation rules mark it otherwise.
- `DocumentCreate.project_id`: current research project id.
- `DocumentCreate.source_id`: persisted source id created from the matching source payload.
- `DocumentCreate.title`: same safe title/display filename rule as source title.
- `DocumentCreate.normalized_document_ref`: optional normalized metadata artifact reference; not extracted text.
- `DocumentCreate.source_identity`: same stable upload metadata identity as source.
- `DocumentCreate.source_type`: `SourceType.USER_UPLOAD_METADATA`.
- `DocumentCreate.retrieval_time`: same upload receipt or fixture timestamp.
- `DocumentCreate.publication_time`, `url`, `doi`, `locator`: copied only from safe metadata.
- `DocumentCreate.transformation_notes`: explicit note that only user-upload metadata was normalized and no document parsing or evidence extraction occurred.
- `DocumentCreate.validation_status`: default `ValidationStatus.PENDING`.
- `ToolCallLogCreate`: optional lineage record with `tool_name` like `user-upload-metadata-connector`, `called_at`, argument hash, safe non-secret arguments, input metadata artifact ids, output source/document artifact ids, and deterministic error shape when normalization fails.

## Risks

- User-upload scope can drift into file parsing, OCR, text extraction, summarization, or evidence extraction.
- Local filesystem paths, user names, or private storage identifiers could leak if copied into `url`, `locator`, `bibliographic_metadata`, or tool-call arguments.
- `DocumentCreate.title`, `source_identity`, `source_type`, and `retrieval_time` are required; missing fixture values should fail deterministically rather than be guessed.
- User-supplied DOI, URL, timestamps, file size, MIME type, and checksum may be malformed and need validation without live network checks.
- Schema drift risk exists if upload metadata needs fields not accepted by `SourceCreate`, `DocumentCreate`, or `ToolCallLogCreate`; do not change Stage 02 schema without blocker plus ADR.

## Tests

Required mocked tests for the later implementation:

- User-upload metadata fixture maps to `SourceCreate` with `SourceType.USER_UPLOAD_METADATA`.
- User-upload metadata fixture maps to `DocumentCreate` using the persisted source id and without extracted body text.
- Missing required title/display-name fallback, source identity, retrieval time, and project id produce deterministic validation errors.
- Optional DOI, URL, locator, publication time, MIME type, byte size, checksum, and user-supplied bibliographic fields are preserved only in allowed schema fields.
- `transformation_notes` states metadata-only normalization and no parsing or extraction.
- Tool-call lineage uses safe arguments and artifact ids without raw file content, secrets, or absolute local paths.
- No-network enforcement proves tests use fixtures and mocks only.
- Forbidden-scope scan covers parsing, extraction, claim graph, research delta, MCP business tools, UI, RAG, stock prediction, and investment advice.
- Secret scan and `git diff --check` remain required.

No tests were run by this subagent because this reassignment produced a mapping/test-risk report only.

## Unresolved Issues

- Final exact user-upload fixture shape is not yet defined.
- Storage-safe upload locator format is not yet specified.
- Whether a `ToolCallLogCreate` record is mandatory for every upload metadata normalization or only for connector execution remains an implementation-goal decision.
- Validation rules for rejecting unsafe local paths and private identifiers need implementation test coverage.
