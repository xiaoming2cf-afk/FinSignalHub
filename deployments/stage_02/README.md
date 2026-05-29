# Stage 02 Deployment Evidence

## Purpose

This directory records GitHub deployment evidence for the Stage 02 planning PR. It is not a release directory and does not imply Stage 02 implementation has started.

## How future stages use this directory

- `GITHUB_PR.md` records the PR URL, branch, CI evidence, Codex review evidence, and GitHub gate status.
- Future release notes or manual GitHub fallback steps for Stage 02 must be added here only after the relevant gate exists.

## Maintenance rules

Keep this directory aligned with live GitHub evidence. Gate 6 must use the live PR head, CI, and Codex review state at review time rather than stale committed hash claims.
