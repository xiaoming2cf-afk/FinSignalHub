# Stage 01 Repo Scaffold Architecture

## Purpose

Stage 01 establishes only the runtime shell needed for later Research Mode evidence-stream work.

## Scope

Included scaffold surfaces:

- FastAPI API app with `/health`.
- MCP server placeholder with `/health` and `/server-info`.
- Next.js admin shell with inspect-only scaffold status.
- Docker Compose services for `postgres`, `api`, `mcp_server`, and `web_admin`.

## Explicit Non-Goals

Stage 01 does not implement:

- Research Mode domain models.
- Database migrations or product tables.
- Connectors.
- LLM adapters.
- Evidence extraction.
- Claim graph or research delta logic.
- MCP business tools.
- Repro Pack export.
- Risk Mode or Replay Engine.
- Chatbot UI, financial dashboard behavior, stock prediction, investment advice, generic RAG, or report generation.

## Service Boundary

| Service | Stage 01 responsibility | Future stage |
| --- | --- | --- |
| `postgres` | Compose-managed database container only | Stage 02 models and migrations |
| `api` | `/health` scaffold only | Stage 02 CRUD and schemas |
| `mcp_server` | `/health` and `/server-info` scaffold only | Stage 06 MCP tools |
| `web_admin` | inspect-only scaffold page | Stage 07 inspect-only admin views |

## Provenance Boundary

No research evidence is ingested or transformed in Stage 01. Provenance requirements remain documented in `AGENTS.md` and will become executable only when later stages add evidence-bearing workflows.

