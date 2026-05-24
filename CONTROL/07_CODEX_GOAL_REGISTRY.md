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
| G-0000 | 00 | Establish control system and capability audit | Implement approved Stage 00 governance plan only | CONDITIONAL PASS / BLOCKED | `stage/00-control-system` pushed to `origin` | 2026-05-24T02:37:02-05:00 | 2026-05-24T03:52:23-05:00 | Governance files exist; audit complete; GitHub PR or blocker; GPT Pro PASS or blocker; phase gate result recorded | GitHub PR and CI complete; Codex reviews returned 1 P1 and 3 P2 findings total; fixes in progress | codex-log-keeper, ai-capability-radar, phase-gate-auditor, gpt-pro-review-preparer, github-stage-deployer, browser-gpt-pro-reviewer, acceptance-evidence-collector, stage-next-goal-synthesizer, github-review-resolver | Hypatia completed read-only audit | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1 | REVIEWED WITH FINDINGS: fix `.env.example`, push, rerun `@codex review` | CONDITIONAL PASS | GPT Pro Stage 01 instructions saved; do not start Stage 01 until Codex findings are resolved |
