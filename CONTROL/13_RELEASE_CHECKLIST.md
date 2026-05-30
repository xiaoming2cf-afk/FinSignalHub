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

Stage 00 has passed local governance checks, GitHub PR/CI/Codex review, and GPT Pro final confirmation. Stage 00 release evidence is recorded in `deployments/stage_00/RELEASE_NOTE.md`.

Current tag state: `stage-00-control-system` exists. Stage 00.1 has GPT Pro PASS and phase-gate PASS evidence saved. Stage 00.1 PR #6 was merged into `main` at `75f215bc8647dac9c5e4e55b68b3b84100f064b4`; its release note exists at `deployments/stage_00_1/RELEASE_NOTE.md`.

Stage 01 is accepted, tagged, and merged. Local scaffold implementation checks passed, PR #7 implementation head `f30a02e7fd891d578e0f6e54f858ed475a6d6881` was pushed, current-head CI passed, Codex reported no major issues, GPT Pro returned final implementation PASS, final evidence commit `ce9bd7c008e1ec5c4b9a6cec9b1488883fe20742` passed CI/Codex, tag `stage-01-repo-scaffold` was pushed, and PR #7 merged at `6b71850a1a59603fe169cd5a5ddf8d40adfaf8f4`. Stage 01 release evidence is recorded in `deployments/stage_01/RELEASE_NOTE.md`.

Stage 02 implementation release checklist is complete.

Stage 02 passed full local checks, kept the root support-file exception limited to dependencies, placeholder database routing, and stage-status docs, passed PR #8 live CI/Codex, passed GPT Pro final implementation review, passed GPT Pro CR-02-043 delta/final review, pushed tag `stage-02-domain-models`, and merged PR #8 at `c5124e166eee4a563a0642a4dcd3fd2db128d615`.

Current Stage 03 release checklist status: planning active. GPT Pro packet/deployment evidence correction head `2d7929ba6b3c7c930527875516044a6f07dfb31c` passed both Stage Governance CI jobs, but Codex review `4395395251` returned CR-03-016. Gate 6 is blocked until GPT Pro follow-up packet evidence is refreshed, the next live head passes CI, and Codex rechecks. GPT Pro Gate 7 returned CONDITIONAL PASS earlier, with response and action items saved under `reviews/stage_03/`, but follow-up confirmation is blocked by B-0045, B-0046, B-0047, and B-0048. Stage 03 cannot be accepted, tagged, merged, or implemented until B-0040, B-0054, and the current GPT Pro follow-up route blockers are resolved. Stage 03 implementation remains unauthorized.
