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

### ADR-0003: Stage 03 ignores local browser runtime artifacts

- Date: 2026-05-30
- Status: accepted
- Context: Chrome-only GPT Pro follow-up attempts created local `artifacts/runtime/` browser profile data, cache, session, and browser database files. These files are local operational residue, not FinSignalHub evidence artifacts, and may contain browser state that must never be committed.
- Decision: Stage 03 may update `.gitignore` to ignore `artifacts/runtime/` as a bounded security hygiene exception. This exception does not authorize product code, connectors, external-source calls, extraction, MCP business tools, UI behavior, secrets, or runtime feature implementation.
- Consequences: The Stage 03 blocker-evidence commit can safely include governance logs and follow-up packet files without risking accidental browser profile data commits.
- Follow-up: Keep runtime browser profiles out of artifact registries and PR evidence. If any future browser evidence is needed, export only sanitized text summaries or screenshots explicitly approved by the stage protocol.

### ADR-0004: Stage 03 updates Stage 02 forbidden-scope guard for approved connectors

- Date: 2026-05-30
- Status: accepted
- Context: Stage 02 added a guard test that rejected any runtime mention of OpenAlex, Crossref, Semantic Scholar, or arXiv because Stage 02 was not allowed to implement connectors. GPT Pro later approved Stage 03 implementation for source connector primitives using exactly those provider names.
- Decision: Stage 03 may minimally update `apps/api/tests/test_stage02_forbidden_scope.py` so the approved connector provider terms are allowed only inside `apps/api/finsignalhub_api/connectors/`, while forbidden Stage 04+ behaviors remain blocked across runtime files.
- Consequences: Full API tests can remain active instead of being skipped, and the guard continues to prevent extraction, claim graph, Research Delta, MCP business tool, chatbot/RAG, stock/investment, Risk Mode, and Replay Engine drift.
- Follow-up: If Codex or GPT Pro rejects this cross-stage test guard adjustment, narrow the exception or split the Stage 02 guard into stage-aware tests before final Stage 03 acceptance.
