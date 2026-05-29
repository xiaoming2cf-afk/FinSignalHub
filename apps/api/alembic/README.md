# Stage 02 Alembic

This directory contains the Stage 02 schema migration for Research Mode domain model primitives only.

It must not contain connector, extraction, claim graph computation, Research Delta computation, MCP business tool, Repro Pack export, Risk Mode, Replay Engine, stock prediction, investment advice, chatbot, generic RAG, auth, or billing logic.

Use `FINSIGNALHUB_DATABASE_URL` for migration checks. `DATABASE_URL` is accepted only as a generic fallback.
