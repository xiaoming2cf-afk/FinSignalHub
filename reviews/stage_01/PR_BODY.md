# Stage 01: Repo Scaffold

## Goal

Create a scaffold-only plan and, after GPT Pro/user approval, a minimal repo scaffold for FinSignalHub.

## Product boundary

Stage 01 is not a business implementation stage. It must not implement Research Mode domain models, connectors, extraction, claim graph, research delta, MCP business tools, Repro Pack, Risk Mode, Replay Engine, stock prediction, investment advice, chatbot UI, generic RAG, or dashboard product behavior.

## Current status

Planning only.

Satisfied planning gate:

- GPT Pro approved the Stage 01 plan and the response is saved in `reviews/stage_01/GPT_PRO_PLAN_REVIEW_RESPONSE.md`.

Runtime implementation remains blocked until:

- User approves implementation.
- Docker daemon and Compose CLI are revalidated with `docker version` and `docker compose version`.
- Docker readiness remains BLOCKED/PENDING until `docker compose config` passes on an approved `docker-compose.yml`; daemon status alone is not enough to unblock implementation acceptance.
- GPT Pro/user resolves the Docker ordering conflict: GPT Pro requires `docker compose config` before implementation, but no `docker-compose.yml` may be created before an approved implementation or explicit compose-only validation amendment.
- PR #6 is merged or this branch remains explicitly based on `stage/00-1-governance-cleanup`.

## Checks

Planning checks:

- no runtime scaffold files created;
- Stage 01 plan exists;
- GPT Pro plan packet exists;
- secret-pattern scan passes;
- `git diff --check` passes.

## Required review

`@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems`
