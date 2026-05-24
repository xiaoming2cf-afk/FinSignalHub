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

Stage 00 branch is blocked because this directory is not a Git repository.
