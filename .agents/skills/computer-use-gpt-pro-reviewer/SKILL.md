---
name: computer-use-gpt-pro-reviewer
description: Govern safe Computer Use recovery for FinSignalHub GPT Pro stage reviews.
---

# Computer Use GPT Pro Reviewer

## When to use

Use this skill only when a FinSignalHub stage is blocked because the Chrome extension or background browser route cannot submit a GPT Pro review packet or capture a GPT Pro response.

This skill is for review-routing governance. It does not create business code, MCP tools, connectors, FastAPI scaffolding, database objects, frontend pages, financial analysis, chatbot behavior, RAG behavior, reports, dashboards, or investment functionality.

## Procedure

1. Read `AGENTS.md`, `CONTROL/06_GPT_PRO_REVIEW_PROTOCOL.md`, `CONTROL/10_COMPUTER_BROWSER_PROTOCOL.md`, `CONTROL/16_CAPABILITY_AUDIT.md`, and the active stage review packet.
2. Confirm the current stage GitHub gate has live evidence: PR URL, current head, CI status, Codex status, and unresolved non-outdated review thread count.
3. Use Computer Use only when the tool is actually exposed in the current Codex tool surface. A local plugin or skill file is not proof that the tool is callable.
4. Prefer background-isolated interaction. Do not send foreground keyboard or mouse events while the user is actively using Chrome unless the user has explicitly provided an idle window for that action.
5. Inspect the visible page state before entering any text. Stop if the page shows login, MFA, captcha, permission, privacy, payment, subscription renewal, password, API key, token, or unclear consent prompts.
6. Submit only the active stage GPT Pro packet plus live Gate 6 supplement. Do not submit secrets, screenshots with private browser context, unrelated conversation history, or stale commit evidence.
7. Capture only the GPT Pro answer needed for acceptance: verdict, required fixes, deferred items, implementation authorization, next-stage instructions, and any risks.
8. Save the response to `reviews/stage_XX/GPT_PRO_REVIEW_RESPONSE.md` and action items to `reviews/stage_XX/GPT_PRO_ACTION_ITEMS.md`.
9. Update `CONTROL/04_EXECUTION_LOG.md`, `CONTROL/07_CODEX_GOAL_REGISTRY.md`, `CONTROL/18_ARTIFACT_REGISTRY.md`, `CONTROL/19_STAGE_DASHBOARD.md`, `CONTROL/20_BLOCKER_LOG.md`, and the active stage acceptance result.
10. If any response-saving commit is created, treat GitHub Gate 6 as reset until the new head has CI PASS, current-head Codex no-major or accepted findings, and unresolved non-outdated review threads equal 0.

## Required outputs

- A saved GPT Pro response and action-item file, or a blocker entry that states why Computer Use could not safely proceed.
- A current-stage execution log entry naming the page, purpose, method, result, and saved evidence path.
- A phase-gate result that marks GPT Pro as PASS, FAIL, or BLOCKED from evidence, not assumption.
- A note in `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md` only when GPT Pro explicitly authorizes the next stage.

## Failure conditions

- Computer Use is claimed available without a callable tool in the current session.
- The workflow inputs credentials, verification codes, payment details, API keys, tokens, or secrets.
- The workflow proceeds through login, MFA, captcha, permission, privacy, payment, subscription renewal, or unclear consent prompts.
- Foreground keyboard or mouse automation is used while the user is actively using Chrome.
- A GPT Pro gate is marked complete without a saved response.
- Screenshots or page captures containing private browser context are committed.
- A new evidence commit is treated as covered by old CI or Codex review.
