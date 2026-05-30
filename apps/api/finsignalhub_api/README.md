# API Package

This package contains the FastAPI application for FinSignalHub.

Allowed after Stage 02 implementation approval:

- deterministic `/health` response showing Stage 02 domain primitive scope;
- Research Mode domain models under `models/`;
- database session/config primitives under `db/` and `core/`;
- Pydantic schemas under `schemas/`;
- generic CRUD helpers and model-level routers under `services/` and `routers/`.

Forbidden until later approved stages:

- connector, extraction, claim graph, Research Delta, Repro Pack, chatbot, RAG, dashboard, prediction, or investment behavior.
