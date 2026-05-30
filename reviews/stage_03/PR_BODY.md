# Stage 03: Source Connectors

## Goal

Plan Research Mode source connectors for OpenAlex, Crossref, Semantic Scholar, arXiv, and user upload metadata. This PR is planning-only.

## Scope

Included:

- Stage 03 plan, tasks, checklist, review packet, PR body, acceptance placeholder, deployment placeholder, architecture doc, command doc, and subagent log README.
- Connector contract and normalized `SourceCreate`/`DocumentCreate` mapping plan aligned to the existing Stage 02 schemas.
- Mocked fixture test plan and no-network CI rule.

Not included:

- connector implementation;
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
- CI: PASS for pre-closeout planning head `dfe38f2ecfd600bed1a38f8ad21ce9305fc5ab79`; both Stage Governance CI jobs passed at https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26686644136/job/78655920616 and https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26686643304/job/78655918498.
- Codex review: PASS for pre-closeout planning head `dfe38f2ecfd600bed1a38f8ad21ce9305fc5ab79`; no-major response at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/9#issuecomment-4583152124 after CR-03-020 remediation.
- GPT Pro plan review: PASS after Chrome follow-up. Follow-up response is saved in `reviews/stage_03/GPT_PRO_FOLLOWUP_RESPONSE.md`; action items are saved in `reviews/stage_03/GPT_PRO_FOLLOWUP_ACTION_ITEMS.md`. GPT Pro resolved `B-0040` and `B-0057` / `CR-03-020`.
- Implementation: not started. Actual connector code requires a separate Stage 03 implementation `/goal`, fresh implementation tests, CI, current-head Codex, and GPT Pro final implementation review.
- Closeout note: if this PR body closeout is pushed as a new evidence commit, merge must verify the live PR head has CI PASS and current-head Codex no-major again. Do not require another self-referential evidence commit solely to record that external verification.
