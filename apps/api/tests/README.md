# API Tests

Stage 01 API tests verified the `/health` scaffold endpoint.

Stage 02 API tests verify only Research Mode domain model primitives: metadata registration, provenance-bearing fields, Pydantic validation, model-level CRUD routes, Alembic upgrade/downgrade behavior, and forbidden-scope guards.

Tests must not require external APIs, LLM calls, connector credentials, MCP business tools, product UI workflows, stock prediction, investment advice, generic RAG, or dashboard behavior.
