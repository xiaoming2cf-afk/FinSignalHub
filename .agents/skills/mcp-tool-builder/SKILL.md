---
name: mcp-tool-builder
description: Define future FinSignalHub MCP tool schemas, tests, provenance, and call logs.
---

# MCP Tool Builder

## When to use

Use starting Stage 06 or earlier only for planning MCP tool contracts.

## Procedure

1. Confirm the tool maps to Research Mode evidence-stream value.
2. Define schema, input validation, output contract, error shape, provenance fields, and call log behavior.
3. Require tests for schema, handler, errors, provenance, and logging.
4. Reject chat, recommendation, prediction, and unlogged tool behavior.

## Required outputs

- Tool contract.
- Test list.
- Provenance and call-log requirements.

## Failure conditions

- Tool lacks provenance, deterministic schema, or call logging.
- Tool behaves like chat, generic RAG, or investment advice.
