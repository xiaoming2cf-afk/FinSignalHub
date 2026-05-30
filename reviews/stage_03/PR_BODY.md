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
- CI: PASS for evidence head `5fb9a751fc004d00d1859342b96cb650216f2a46`; next push requires fresh CI.
- Codex review: BLOCKED by CR-03-006 until the non-self-validating Gate 6 wording fix is pushed and rechecked. Evidence head `5fb9a751fc004d00d1859342b96cb650216f2a46` received a Codex no-major issue comment at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/9#issuecomment-4582257443, but inline P2 CR-03-006 remains active.
- GPT Pro plan review: CONDITIONAL PASS. Response saved in `reviews/stage_03/GPT_PRO_REVIEW_RESPONSE.md`; action items saved in `reviews/stage_03/GPT_PRO_ACTION_ITEMS.md`. B-0040 remains open: corrected artifacts must be committed, PR head CI/Codex must be refreshed, and GPT Pro follow-up must confirm before implementation planning.
- Implementation: not authorized.
