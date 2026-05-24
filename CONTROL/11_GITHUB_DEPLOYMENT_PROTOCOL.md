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

Stage 00 GitHub status is BLOCKED because the workspace is not a Git repository and GitHub CLI is not authenticated.
