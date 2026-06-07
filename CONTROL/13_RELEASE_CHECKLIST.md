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

Stage 03 release checklist is complete. Pre-closeout planning head `dfe38f2ecfd600bed1a38f8ad21ce9305fc5ab79` passed both Stage Governance CI jobs and Codex no-major. Chrome follow-up saved GPT Pro `VERDICT: PASS`, resolving B-0040 and B-0057 / CR-03-020 for the planning gate. PR #9 later returned CR-03-028 on stale current-state wording; replacement PR #10 became the active closeout route, passed CI and Codex no-major, and GPT Pro closeout review returned PASS. PR #10 goal-draft head `8f10f95c69c3eaf7d6ada7b878e017b917929e33` passed CI, received Codex no-major, and received GPT Pro implementation-goal PASS. Implementation remediation head `039e3d087c84f6ec61a6107b6f55b628d8a79ee6` passed CI/Codex and GPT Pro final review. CR-03-042 and CR-03-043 were remediated, and GPT Pro re-review returned PASS for CR-03-043. Final evidence head `92970f32f0b22754dad02c661e2b1b9a5d313fec` passed PR #10 CI and Codex no-major, PR #10 was squash-merged into `main` at `13ee0a0bc497578b235662ea60c9aa225c62e53f`, and tag `stage-03-source-connectors` was pushed.

Stage 04 planning closeout, implementation-goal draft, and final implementation review have GPT Pro PASS, but Stage 04 is not released or merged. PR #11 planning head `d62d8d8eafb73eb207ba401e12f9d073dff61223` passed CI and current-head Codex no-major, then GPT Pro returned PASS for the planning gate. Later closeout heads remediated CR-04-011 through CR-04-027. Pre-implementation head `2a6378cf12953e3f376bd29a3cf208c7f2b01d8a` passed CI and Codex no-major. Stage 04 implementation head `f964503646bac5b5efbb52d97f4d434e79763f7b` passed CI, but Codex opened CR-04-029 on blank no-quote rationale validation. Remediation head `79ec29a42b9119dbaf5edd1c88b7fb4e52fe1368` passed CI, received current-head Codex no-major, had unresolved review threads = 0, and GPT Pro returned final implementation PASS. The response-saving evidence-sync patch passed local checks. Stage 04 is not released until this evidence-sync head passes live PR #11 CI, current-head Codex no-major, unresolved review threads = 0, phase-gate-auditor confirms the external gate, tag, and merge.
