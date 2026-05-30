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

Current Stage 03 release checklist status: planning active. GitHub/Codex Gate 6 passed for prior live head `ce5b94a4ffdad3b08488fb8f7a6952e12a58b4af`. Evidence head `5fb9a751fc004d00d1859342b96cb650216f2a46` passed CI and received a Codex no-major issue comment, but CR-03-006 now blocks Gate 6 until the committed acceptance wording is non-self-validating and the next PR head is rechecked. GPT Pro Gate 7 returned CONDITIONAL PASS through the off-screen Edge/CDP background route, with response and action items saved under `reviews/stage_03/`. Stage 03 cannot be accepted, tagged, merged, or implemented until B-0040 and B-0041 are resolved. Stage 03 implementation remains unauthorized.
