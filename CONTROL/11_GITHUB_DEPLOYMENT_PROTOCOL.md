# 11 GitHub Deployment Protocol

## Purpose

Defines branch, commit, PR, CI, Codex review, and release rules for every stage.

## Owner

GitHub stage deployer.

## When to update

Update when branch naming, PR body source, review requirements, CI requirements, or tag rules change.

## Required fields

- Stage id
- Branch
- Commit format
- PR title
- PR body path
- Required comment
- CI result
- Codex review summary
- Release/tag note

## Example format

`Stage 00 | branch stage/00-control-system | PR Stage 00: Control System | blocked: gh unauthenticated`

## Current state

Stage branches:

- `stage/00-control-system`
- `stage/01-repo-scaffold`
- `stage/02-domain-models`
- `stage/03-source-connectors`
- `stage/04-evidence-extraction`
- `stage/05-claim-graph-delta`
- `stage/06-mcp-tools`
- `stage/07-admin-ui`
- `stage/08-repro-pack`
- `stage/09-demo-acceptance`

Commit format: `stage-XX: concise summary`.

PR title format: `Stage XX: Stage Name`.

PR body source: `reviews/stage_XX/PR_BODY.md`.

Required PR comment:

`@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems`

Stage 00 GitHub status is PASS. Branch `stage/00-control-system` was pushed and merged through PR #1. Post-acceptance capability evidence was merged through PR #2, and GPT Pro post-acceptance evidence was merged through PR #3. Governance CI passed on the latest Stage 00 evidence PRs, and Codex follow-up reviews found no major issues.

Persistent GitHub CLI authentication is now available for active account `xiaoming2cf-afk`; `lhy18613775` remains only a non-active secondary login / connector account. Future stages must still record branch, PR, CI, `@codex review`, PR URL, and any account or permission blocker in their own deployment evidence.
