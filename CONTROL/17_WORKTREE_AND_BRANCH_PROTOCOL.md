# 17 Worktree And Branch Protocol

## Purpose

Defines branch, worktree, and cross-stage file-boundary rules.

## Owner

GitHub stage deployer.

## When to update

Update when stage branch names, file boundaries, or merge-conflict rules change.

## Required fields

- Stage id
- Branch or worktree
- Allowed files
- Forbidden files
- Cross-stage exception
- Conflict record
- Test result

## Example format

`Stage 00 | stage/00-control-system | CONTROL, docs, skills | backend forbidden | no exception`

## Current state

Rules:

- No direct development on main.
- Each stage uses `stage/XX-short-name` or an isolated worktree.
- Each stage may modify only files authorized by its plan.
- Cross-stage changes require an ADR entry, blocker entry, PR body note, and acceptance evidence.
- Merge conflicts must record files, resolution, risk, and tests.
- Do not merge without GitHub and GPT Pro gates.

Stage 00 branch `stage/00-control-system` exists locally and on `origin`. The workspace is now a Git repository with `main` as the PR base. Stage 01 must use `stage/01-repo-scaffold` or an isolated worktree and may not modify Stage 00 acceptance evidence except for append-only references required by the Stage 01 plan.
