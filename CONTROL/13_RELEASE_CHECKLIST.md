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

`Stage 00 | local checks pass | GitHub pass | GPT Pro pass | release note created`

## Current state

Stage 00 has passed local governance checks, GitHub PR/CI/Codex review, and GPT Pro final confirmation. Stage 00 release evidence is recorded in `deployments/stage_00/RELEASE_NOTE.md`; a Git tag should point at the final Stage 00 acceptance commit after the final acceptance commit is pushed.
