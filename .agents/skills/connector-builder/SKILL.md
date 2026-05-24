---
name: connector-builder
description: Define source connector rules for normalized research documents and mock tests.
---

# Connector Builder

## When to use

Use during Stage 03 connector planning and implementation.

## Procedure

1. Define connector purpose and source boundaries.
2. Normalize output into a Document shape approved by the stage plan.
3. Preserve source identity, retrieval time, license/availability when known, and provenance.
4. Create mock tests before relying on external APIs.
5. Record rate limits and failure modes.

## Required outputs

- Connector contract.
- Mock fixtures and tests.
- Provenance mapping.
- Error handling notes.

## Failure conditions

- Connector has no mock tests.
- Connector output lacks source provenance.
