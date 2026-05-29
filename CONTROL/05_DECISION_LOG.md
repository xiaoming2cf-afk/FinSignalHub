# 05 Decision Log

## Purpose

Records architecture, product, process, plugin, and phase acceptance decisions.

## Owner

Engineering lead and product process lead.

## When to update

Update when a decision changes product direction, architecture, governance, stage flow, security posture, or user-instruction precedence.

## Required fields

- ADR id
- Date
- Status
- Context
- Decision
- Consequences
- Follow-up

## Example format

`ADR-0001 | accepted | Research Mode-first and MCP-first evidence-stream architecture`

## Current state

### ADR-0001: FinSignalHub adopts Research Mode-first, MCP-first, evidence-stream architecture

- Date: 2026-05-24
- Status: accepted
- Context: The project must serve researchers through AI Agent workflows, not become a chat product, stock tool, dashboard, generic RAG, or report generator.
- Decision: FinSignalHub will prioritize Research Mode, MCP tools, connectors, evidence-stream artifacts, provenance, and reproducible exports. Business implementation must map to research delta, claim graph, evidence card, literature matrix, method card, dataset card, repro pack, or tool call log value.
- Consequences: Stage gates block product drift. MCP and connector surfaces are primary. UI work is inspect-only unless a later stage plan proves research value.
- Follow-up: Stage 01 may scaffold repo infrastructure only after Stage 00 GitHub and GPT Pro gates are resolved or explicitly blocked.

### ADR-0002: Stage 02 implementation uses bounded root support-file exceptions

- Date: 2026-05-29
- Status: accepted
- Context: GPT Pro passed the Stage 02 plan and authorized a domain-model implementation goal after user approval. The saved implementation boundary focused on API model/migration/schema/CRUD files, but the approved tests require importable SQLAlchemy, Alembic, Pydantic, and PostgreSQL driver dependencies, plus placeholder database routing for Docker/PostgreSQL migration checks.
- Decision: Stage 02 may modify `pyproject.toml`, `.env.example`, `docker-compose.yml`, root/app README files, and `CHANGELOG.md` only as support files for approved dependency declarations, placeholder-only database URL documentation, PostgreSQL migration verification, and current-stage status documentation. These files must not introduce product runtime behavior, connectors, extraction, MCP business tools, auth, billing, dashboards, stock prediction, investment advice, or secrets.
- Consequences: The exception must be disclosed in PR #8, Stage 02 review packets, blocker/status logs, and acceptance evidence. Codex and GPT Pro must treat the exception as a reviewable scope item, not as implicit permission for broader root configuration or Stage 03+ behavior.
- Follow-up: Before Stage 02 acceptance, verify root support-file changes are limited to dependencies, placeholder env names, database routing, and docs. If Codex or GPT Pro rejects the exception, revert or narrow the support-file changes before final acceptance.
