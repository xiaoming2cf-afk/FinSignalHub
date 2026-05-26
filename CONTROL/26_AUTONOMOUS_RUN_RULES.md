# 26 Autonomous Run Rules

## Purpose

Defines safety and scope rules for long autonomous FinSignalHub sessions.

## Owner

Autonomous run coordinator and product governance lead.

## When to update

Update when the user changes long-run authority, GPT Pro changes stage permissions, or a new stop condition is discovered.

## Required fields

- Allowed progression
- Stage boundaries
- Capability fallback policy
- Browser and secret policy
- Product drift policy
- Stop conditions
- User inspection points

## Example format

`Allowed | Stage 00.1 governance cleanup | no business code | stop on GPT Pro login`

## Current state

Allowed progression for this run is Stage 00.1 governance cleanup, then Stage 01 planning, then Stage 01 implementation only if the Stage 01 plan is approved, GPT Pro permits implementation, and Docker is reachable.

The repository logs are the source of truth. Do not rely on memory. Each cycle must record files read, stage detected, action selected, skills used, commands, files changed, tests, GitHub status, GPT Pro status, blockers, artifacts, and next action.

No stage may be skipped. No implementation may begin without an approved plan. No stage may be marked complete without the ten phase gates. Stage 02 and later are forbidden unless GPT Pro assigns them after Stage 01 final acceptance.

Product drift stop condition: any work that turns FinSignalHub into chat, generic RAG, stock prediction, investment advice, ordinary report generation, financial dashboard, model leaderboard, Risk Mode, or Replay Engine must stop and be logged in `CONTROL/20_BLOCKER_LOG.md`.

Browser safety: Chrome is used only for GPT Pro review with existing login state. Stop on login, MFA, permission, payment, privacy, captcha, secret, or unclear consent prompts. Do not enter passwords, verification codes, API keys, tokens, payment data, or secrets.

Docker state: Docker is not required for Stage 00.1. Stage 01 implementation is blocked until Docker daemon availability is revalidated.
