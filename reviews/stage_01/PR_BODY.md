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

- GPT Pro permits implementation from the current implementation-gate packet.
- Docker daemon and Compose CLI are revalidated with `docker info`, `docker version`, and `docker compose version`.
- GPT Pro Docker ordering response is saved: `docker compose config` is implementation-preflight, not pure pre-implementation validation.
- After user implementation approval, the first Stage 01 implementation step must create minimal `docker-compose.yml` and immediately run `docker compose config`; if it fails, implementation stops before further scaffold.

User approval status:

- User implementation approval is recorded from the 2026-05-26 continuation-plan confirmation.

Baseline status:

- PR #6 is merged into `main` at `75f215bc8647dac9c5e4e55b68b3b84100f064b4`.
- PR #7 now targets `main`.

## Checks

Planning checks:

- no runtime scaffold files created;
- Stage 01 plan exists;
- GPT Pro plan packet exists;
- secret-pattern scan passes;
- `git diff --check` passes.

## Required review

`@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems`
