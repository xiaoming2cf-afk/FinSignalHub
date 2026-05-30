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

Stage 02 implementation release checklist is active. Before accepting, tagging, merging, or requesting Stage 03:

- Full local checks must pass.
- Root support-file exception must stay limited to dependencies, placeholder database routing, and stage-status docs.
- PR #8 implementation head must be pushed.
- GitHub CI must pass for the implementation head.
- Codex must return no major issues for the implementation head.
- GPT Pro final implementation review must pass or accepted CONDITIONAL PASS with critical items resolved for the current remediation head after live CI/Codex clear.
- GPT Pro must provide Stage 03 instructions.

Current Stage 02 release status: PASS / accepted for runtime remediation head `eb4dd0f97ad04ce2173b5d677564d3254ad93313`; final docs/log evidence-sync head still requires fresh CI/Codex after push before merge. The implementation-reviewed head has live CI PASS, Codex no-major evidence at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4579603862, and GPT Pro final implementation PASS saved in `reviews/stage_02/GPT_PRO_REVIEW_RESPONSE.md`. Final evidence follow-up fixed CR-02-037 through CR-02-043; the CR-02-043 runtime remediation head `eb4dd0f97ad04ce2173b5d677564d3254ad93313` passed live CI, received Codex no-major at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4580699730, and received GPT Pro delta/final PASS. Stage 03 implementation is not authorized; only Stage 03 planning may start after these Stage 02 final evidence updates are pushed, pass fresh CI/Codex, and PR #8 is merged.
