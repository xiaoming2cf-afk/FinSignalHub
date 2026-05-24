# 07 Codex Goal Registry

## Purpose

Tracks every approved Codex goal and its acceptance state.

## Owner

Codex log keeper.

## When to update

Update at goal creation, checkpoint changes, PR creation, review updates, GPT Pro updates, and goal close.

## Required fields

- Goal ID
- Stage
- Title
- Prompt text
- Status
- Branch/worktree
- Started at
- Updated at
- Done-when
- Current checkpoint
- Skills used
- Subagents used
- PR URL
- Codex review status
- GPT Pro status
- Next stage source

## Example format

`G-0000 | Stage 00 | active | branch blocked | GPT Pro blocked`

## Current state

| Goal ID | Stage | Title | Prompt text | Status | Branch/worktree | Started at | Updated at | Done-when | Current checkpoint | Skills used | Subagents used | PR URL | Codex review status | GPT Pro status | Next stage source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G-0000 | 00 | Establish control system and capability audit | Implement approved Stage 00 governance plan only | PASS / COMPLETE | `stage/00-control-system` merged; follow-up evidence branches merged/open as recorded | 2026-05-24T02:37:02-05:00 | 2026-05-24T09:45:25-05:00 | Governance files exist; audit complete; GitHub PR or blocker; GPT Pro PASS or blocker; phase gate result recorded | Stage 00 complete: PRs #1-#4, CI, Codex reviews, GPT Pro final confirmation, logs, prompt-by-prompt confirmation, and acceptance evidence saved | codex-log-keeper, ai-capability-radar, phase-gate-auditor, gpt-pro-review-preparer, github-stage-deployer, browser-gpt-pro-reviewer, acceptance-evidence-collector, stage-next-goal-synthesizer, github-review-resolver | Hypatia and Fermat completed read-only audits; final confirmation used bounded local verification only | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/2; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/3; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/4 | PASS: latest PR #4 Codex response found no major issues | PASS: final GPT Pro confirmation and post-acceptance capability confirmation saved | GPT Pro authorized Stage 01 planning; do not implement Stage 01 before approved Stage 01 plan and goal |
| G-0001 | 00.1 | RunLog governance cleanup | Implement approved RunLog-driven Stage 00.1 governance cleanup only | ACTIVE | `stage/00-1-governance-cleanup` | 2026-05-24T11:41:00-05:00 | 2026-05-24T13:49:14-05:00 | RunLog files exist; helper scripts exist; PR and Codex review complete; GPT Pro PASS or blocker saved; phase gate result recorded | PR #6 open; latest local-environment false-positive P1 finding fixed locally; checks, follow-up CI, and Codex review pending before GPT Pro review | finsignal-product-governor, phase-gate-auditor, codex-log-keeper, github-stage-deployer, gpt-pro-review-preparer, browser-gpt-pro-reviewer, github-review-resolver, acceptance-evidence-collector, stage-next-goal-synthesizer | Lorentz read-only verification completed | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6 | pending after local P1 fix | pending | Stage 00 final GPT Pro instruction and user-approved RunLog prompt |
