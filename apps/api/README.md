# API

This directory contains the FastAPI package used by FinSignalHub.

Stage 01 provided the health-only scaffold. Stage 02 adds Research Mode domain model primitives only: SQLAlchemy models, Alembic migration wiring, Pydantic schemas, and model-level CRUD routes under `/research-mode/*`.

The API still must not include connectors, LLM adapters, evidence extraction, claim graph computation, research delta computation engines, MCP business tools, Repro Pack export logic, chatbot behavior, generic RAG, dashboard product behavior, stock prediction, investment advice, auth, or billing in Stage 02.
