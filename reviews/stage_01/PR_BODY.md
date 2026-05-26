# Stage 01: Repo Scaffold

## Goal

Create a scaffold-only plan and, after GPT Pro/user approval, a minimal repo scaffold for FinSignalHub.

## Product boundary

Stage 01 is not a business implementation stage. It must not implement Research Mode domain models, connectors, extraction, claim graph, research delta, MCP business tools, Repro Pack, Risk Mode, Replay Engine, stock prediction, investment advice, chatbot UI, generic RAG, or dashboard product behavior.

## Current status

Planning only. Runtime implementation is blocked until:

- GPT Pro approves the Stage 01 plan.
- User approves implementation.
- Docker daemon and Compose CLI are revalidated with `docker version` and `docker compose version`.
- Docker readiness remains BLOCKED/PENDING until `docker compose config` passes on an approved `docker-compose.yml`; daemon status alone is not enough to unblock implementation acceptance.
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
