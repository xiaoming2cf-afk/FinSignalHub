# Stage 03 Connector Package

This package contains source metadata normalizers for FinSignalHub Stage 03.

Allowed behavior:

- Convert fixture or caller-provided provider metadata into Stage 02-compatible `SourceCreate`, `DocumentCreate`, and `ToolCallLogCreate` payloads.
- Preserve provider identity, locator, DOI or external id, retrieval time, publication time, provider metadata, validation status, and transformation notes.
- Keep tests fixture-only and network-free.

Forbidden behavior:

- Live API fetching in default code paths or CI.
- Evidence extraction, abstract summarization, quote-span validation, claim graph logic, research delta computation, MCP business tools, admin UI behavior, chat-first or retrieval-answering behavior, stock prediction, or investment advice.
- Stage 02 schema or migration changes without a blocker and ADR.

Tool call artifact IDs are not populated during normalization because Stage 02 source and document IDs are created by persistence after these payloads are validated. The persistence layer may update tool-call artifacts in a later bounded step without changing this connector contract.
