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
- CI: PASS for Stage Governance CI.
- Codex review: PASS for live head `ce5b94a4ffdad3b08488fb8f7a6952e12a58b4af`; current no-major response is https://github.com/xiaoming2cf-afk/FinSignalHub/pull/9#issuecomment-4582016952. Active and historical findings are tracked in `reviews/stage_03/CODEX_REVIEW_SUMMARY.md`.
- GPT Pro plan review: CONDITIONAL PASS. Response saved in `reviews/stage_03/GPT_PRO_REVIEW_RESPONSE.md`; action items saved in `reviews/stage_03/GPT_PRO_ACTION_ITEMS.md`. B-0040 remains open: corrected artifacts must be committed, PR head CI/Codex must be refreshed after this evidence push, and GPT Pro follow-up must confirm before implementation planning.
- Implementation: not authorized.
