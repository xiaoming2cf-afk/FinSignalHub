---
name: github-review-resolver
description: Summarize and resolve Codex review findings on FinSignalHub PRs.
---

# GitHub Review Resolver

## When to use

Use after `@codex review` comments or requested changes appear on a stage PR.

## Procedure

1. Read review comments and CI status.
2. Classify findings by severity and gate.
3. Fix critical findings or record deferred rationale.
4. Save summary to `reviews/stage_XX/CODEX_REVIEW_SUMMARY.md`.
5. Update acceptance result and blocker log.

## Required outputs

- Codex review summary.
- Critical finding resolution or deferral record.
- Updated phase gate status.

## Failure conditions

- Critical findings are ignored.
- A PR is accepted without review summary.
