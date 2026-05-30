# Stage 03: Source Connectors

## Goal

Plan Research Mode source connectors for OpenAlex, Crossref, Semantic Scholar, arXiv, and user upload metadata, then draft the separate Stage 03 implementation `/goal` packet after PR #10 live-head CI/Codex and GPT Pro closeout allow goal drafting. This PR still does not implement connector code.

## Scope

Included:

- Stage 03 plan, tasks, checklist, review packet, PR body, acceptance placeholder, deployment placeholder, architecture doc, command doc, and subagent log README.
- Connector contract and normalized `SourceCreate`/`DocumentCreate` mapping plan aligned to the existing Stage 02 schemas.
- Mocked fixture test plan and no-network CI rule.
- Stage 03 implementation `/goal` draft artifacts:
  - `PLANS/STAGE_03_IMPLEMENTATION_GOAL.md`
  - `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_PACKET.md`
  - `reviews/stage_03/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md`

Not included:

- connector implementation;
- connector tests and fixtures;
- external API calls;
- evidence extraction;
- LLM adapters;
- claim graph or research delta computation;
- MCP business tools;
- admin UI behavior;
- chatbot, generic RAG, stock prediction, investment advice, dashboard behavior, Risk Mode, or Replay Engine.

## Checks

Planning-only checks to run before PR:

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03`
- no Stage 03 implementation files exist
- secret scan
- `git diff --check`

## Review

After PR creation, request:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

GPT Pro plan review remains a hard gate before any Stage 03 implementation.

## Current Gate Status

- Local planning checks: PASS.
- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/9
- Replacement closeout PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10
- Pre-closeout planning evidence: head `dfe38f2ecfd600bed1a38f8ad21ce9305fc5ab79` passed CI and Codex no-major, then GPT Pro accepted that evidence. This is the accepted planning evidence, not a claim about the latest PR head after later closeout commits.
- Current closeout gate before goal drafting: PR #10 live head `1f03defb437a9f6f2b694a2697754faa1e1ea7f0` passed governance CI and Codex no-major at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10#issuecomment-4584381224. That evidence allowed goal drafting only.
- Current implementation-goal draft gate: if this PR body or draft artifacts are pushed as a new commit, verify the active closeout PR with `gh pr view 10 --json headRefOid,statusCheckRollup,reviews,comments`, require both governance checks to pass on the new live head, and require Codex no-major for that live head before GPT Pro goal review can activate implementation.
- GPT Pro plan/closeout review: PASS after Chrome follow-up and PR #10 closeout review. Follow-up response is saved in `reviews/stage_03/GPT_PRO_FOLLOWUP_RESPONSE.md`; closeout response is saved in `reviews/stage_03/GPT_PRO_CLOSEOUT_RESPONSE.md`; action items are saved in `reviews/stage_03/GPT_PRO_CLOSEOUT_ACTION_ITEMS.md`. GPT Pro resolved `B-0040`, `B-0057` / `CR-03-020`, and `B-0062` at the closeout-content level.
- Implementation: not started. Actual connector code requires the goal draft to be pushed, pass live-head CI/Codex, and receive GPT Pro PASS or accepted CONDITIONAL PASS before implementation begins.
- Closeout note: if this PR body closeout is pushed as a new evidence commit, merge must verify the live PR head has CI PASS and current-head Codex no-major again. Do not require another self-referential evidence commit solely to record that external verification.
