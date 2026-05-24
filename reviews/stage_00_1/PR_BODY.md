# Stage 00.1: RunLog Governance Cleanup

## Goal

Add the RunLog-driven control layer required for long autonomous FinSignalHub sessions.

## Product boundary

This PR is governance-only. It does not add product runtime, backend, database, connectors, frontend, MCP business tools, chatbot behavior, generic RAG, stock prediction, investment advice, dashboard behavior, model leaderboard, Risk Mode, or Replay Engine.

## Deliverables

- RunLog control files under `CONTROL/23` through `CONTROL/27`.
- `RUNLOG/LONG_RUN_CURRENT.md` and `RUNLOG/LONG_RUN_SUMMARY.md`.
- Local plugin helper scripts and PR body template.
- Stage 00.1 review packet, PR body, acceptance result, and deployment record.
- User-provided run instruction committed under `运行要求/`.
- Logs, registries, dashboard, release checklist, and blocker log synchronized.

## Checks

- CONTROL required headings.
- Stage 00.1 artifact existence.
- Plugin helper syntax and phase check.
- Forbidden business path check.
- Secret-pattern scan.
- `git diff --check`.

## Known limitations

Docker daemon is unavailable at Stage 00.1 start. It does not block governance cleanup but blocks Stage 01 implementation until revalidated.

## Review status

- CI: PASS on PR #6.
- Codex review: PASS, no major issues on `43c570a1291b262faba32f288b29b0dfbf396029`.
- GPT Pro review: PASS; Stage 01 planning only authorized.
- Stage 01 implementation remains blocked until Stage 01 plan approval, GPT Pro plan review, Docker validation, and PR #6 merge/base decision.

## Required review

Please run `@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems`.
