# Connector Review Agent: Stage 03 Source Connector Primitives

Timestamp: 2026-05-30T17:35:00-05:00

## Files Touched

- `D:\new work\logs\subagents\stage_03\connector-review-agent.md`

## Files Reviewed

- `D:\new work\AGENTS.md`
- `D:\new work\PLANS\STAGE_03_IMPLEMENTATION_GOAL.md`
- `D:\new work\apps\api\finsignalhub_api\schemas\domain.py`
- `D:\new work\apps\api\finsignalhub_api\models\enums.py`
- `D:\new work\apps\api\finsignalhub_api\connectors\base.py`
- `D:\new work\apps\api\finsignalhub_api\connectors\openalex.py`
- `D:\new work\apps\api\finsignalhub_api\connectors\crossref.py`
- `D:\new work\apps\api\finsignalhub_api\connectors\semantic_scholar.py`
- `D:\new work\apps\api\finsignalhub_api\connectors\arxiv.py`
- `D:\new work\apps\api\finsignalhub_api\connectors\user_upload.py`
- `D:\new work\apps\api\finsignalhub_api\connectors\__init__.py`
- `D:\new work\apps\api\tests\test_stage03_connectors.py`
- `D:\new work\apps\api\tests\fixtures\stage03_connectors\*.json`
- `D:\new work\docs\architecture\stage_03_source_connectors.md`
- `D:\new work\docs\codex\stage_03_commands.md`
- `D:\new work\reviews\stage_03\GPT_PRO_IMPLEMENTATION_GOAL_ACTION_ITEMS.md`

## Summary

Stage 03 source connector primitives are aligned with the accepted Research Mode source-metadata normalization scope. The connector modules normalize OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata into Stage 02-compatible `SourceCreate`, `DocumentCreate`, and `ToolCallLogCreate` payloads. No live API client imports, MCP business tools, evidence extraction, claim graph, Research Delta, Repro Pack, chatbot, generic RAG, stock prediction, investment advice, or dashboard behavior were found in the connector package.

Schema compatibility is mostly sound: `SourceCreate` accepts source identity, type, URL, DOI, locator, publication time, retrieval time, bibliographic metadata, and validation status; `DocumentCreate` accepts the same normalized metadata plus `source_id`; `ToolCallLogCreate` accepts tool name/version/schema, called time, argument hash, safe arguments, optional artifact ids, and deterministic error shape. Connector outputs use the Stage 02 `SourceType` enum values for literature, preprint, and user-upload metadata.

## Risks

1. Medium: `ConnectorRunContext.extra_safe_arguments` is merged directly into `ToolCallLogCreate.safe_arguments` in `connectors/base.py` without key filtering or secret-like value checks. A future caller could accidentally persist `api_key`, `token`, `password`, or `secret` values even though the default fixture tests do not do this.

2. Medium: `normalize_user_upload_metadata` stores `record["metadata"]` verbatim under `provider_metadata["provided_metadata"]`. User-supplied metadata can contain private notes, local paths, credentials, or other sensitive keys unless sanitized before it is placed in `SourceCreate.bibliographic_metadata`.

3. Low/Medium: Tool-call lineage is represented by a `ToolCallLogCreate` payload, but `input_artifact_ids` and `output_artifact_ids` are not populated in `build_result`. This is compatible with Stage 02 because those fields are optional, but final provenance may be weaker unless the persistence layer later links created Source/Document artifacts back to the tool-call log.

4. Low: No-network enforcement currently relies on fixture-only normalizers and a test scanning exact import strings such as `import httpx`, `import requests`, `urllib.request`, and `socket.`. Current connector files pass this pattern, but the test would not catch every network route, such as `from httpx import Client`, `urllib3`, or `http.client`.

## Tests And Checks

- Read-only file audit of Stage 03 connector modules, fixture files, Stage 02 schemas, enums, and Stage 03 goal/action documents.
- `rg` scan for network client and network-call indicators across connector modules, fixtures, and Stage 03 tests.
- `rg` scan for secret-like terms across connector modules, fixtures, and Stage 03 tests.
- `rg` scan for forbidden-scope symbols and product drift indicators across connector modules and Stage 03 tests.
- No `pytest` command was run in this subagent pass to preserve the read-only boundary and avoid cache or bytecode writes.

## Unresolved Issues

- Add a sanitizer or reject-list for `extra_safe_arguments` and user-upload `provided_metadata` before final Stage 03 acceptance.
- Expand no-network tests beyond exact import string matching or document the accepted enforcement boundary.
- Confirm where persistence attaches `input_artifact_ids` and `output_artifact_ids` to `ToolCallLogCreate`, or explicitly defer that linkage with acceptance rationale.
