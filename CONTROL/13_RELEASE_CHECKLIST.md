# 13 Release Checklist

## Purpose

Defines required checks before a stage release, tag, or acceptance note.

## Owner

Release coordinator.

## When to update

Update when release evidence, tag policy, PR flow, or stage acceptance changes.

## Required fields

- Stage id
- Local checks
- Documentation checks
- Security checks
- GitHub checks
- GPT Pro checks
- Release note or tag

## Example format

`Stage 00 | local checks pass | GitHub blocked | GPT Pro blocked | release blocked`

## Current state

Stage 00 cannot be released until local governance checks run and GitHub/GPT Pro gates are either passed or explicitly blocked. A blocked Stage 00 may be handed back to the user but cannot be called complete.
