# 20 Blocker Log

## Purpose

Records blockers that prevent a stage, gate, tool, browser action, GitHub action, or GPT Pro review from completing.

## Owner

Codex log keeper.

## When to update

Update immediately when a blocker appears, changes, is resolved, or is accepted as deferred.

## Required fields

- Blocker ID
- Timestamp
- Stage
- Capability or gate
- Status
- Blocker
- Impact
- Fallback
- Requires user action
- Resolution owner

## Example format

`B-0001 | Stage 00 | GitHub | open | gh unauthenticated | PR blocked | manual steps | yes | user`

## Current state

| Blocker ID | Timestamp | Stage | Capability or gate | Status | Blocker | Impact | Fallback | Requires user action | Resolution owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B-0001 | 2026-05-24T02:37:02-05:00 | 00 | GitHub remote | partially resolved | local Git repo and `stage/00-control-system` branch now exist, but no GitHub remote is configured | cannot push, create PR, run CI, or request `@codex review` | add GitHub remote after user provides/creates repository | yes | user |
| B-0002 | 2026-05-24T02:37:02-05:00 | 00 | GitHub CLI | open | `gh` is not authenticated; `gh auth login --web` was attempted and timed out without saving auth state | cannot push via `gh`, create PR, or comment review request | user completes `gh auth login`, or provides an authenticated manual PR path | yes | user |
| B-0003 | 2026-05-24T02:37:02-05:00 | 00 | GPT Pro review | resolved | target page originally not submitted through Chrome extension | resolved by Chrome submission and saved response | response saved to `reviews/stage_00/GPT_PRO_REVIEW_RESPONSE.md` | no | Codex |
| B-0004 | 2026-05-24T02:37:02-05:00 | 00 | Docker | open | Docker daemon unavailable or permission required | future Stage 01 Docker checks blocked | start Docker and rerun audit | yes | user |
| B-0005 | 2026-05-24T02:37:02-05:00 | 00 | Stage 00 full acceptance | open | GPT Pro returned CONDITIONAL PASS because GitHub remote, PR, CI, and `@codex review` are missing | Stage 00 cannot become full PASS; Stage 01 must not begin | resolve B-0001 and B-0002, then push branch, create PR, and request Codex review | yes | user |
| B-0006 | 2026-05-24T02:37:02-05:00 | 00 | GitHub Desktop publish | open | GitHub Desktop was opened for this repo, but publishing requires user account/login and repository choice | Codex cannot complete remote creation or PR through Desktop without user action | user publishes current repo or provides remote URL, then Codex can continue push/PR if `gh` is authenticated | yes | user |
| B-0007 | 2026-05-24T02:37:02-05:00 | 00 | Repository account mismatch | open | GitHub plugin user is `lhy18613775`, while browser/push session created `xiaoming2cf-afk/FinSignalHub` | GitHub connector may not manage PR metadata for the browser-created repository | use browser UI for PR and review comment, keep plugin audit record | yes | user |
| B-0008 | 2026-05-24T02:37:02-05:00 | 00 | Codex PR review | open | `@codex review` was requested, but `chatgpt-codex-connector` replied that Codex must be connected to GitHub | Gate 6 cannot fully pass because no Codex findings were produced | connect Codex to GitHub for `xiaoming2cf-afk/FinSignalHub`, then request review again | yes | user |
