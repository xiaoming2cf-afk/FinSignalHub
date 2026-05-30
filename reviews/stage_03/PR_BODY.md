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
- CR-03-013 remediation checks: PASS locally; `4fd9278` CI PASS; CR-03-014/015 GPT Pro packet and deployment CI-evidence refresh pending live-head recheck.
- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/9
- CI: PASS for current-state evidence correction head `4fd9278db518747d93e968518680783d6310f74e` with jobs https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26683979429/job/78648979607 and https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26683980043/job/78648981384. Any later GPT Pro packet/deployment evidence correction must be verified against the live PR head before Gate 6 can pass.
- Codex review: BLOCKED by CR-03-014/015 from Codex reviews `4395370803` and `4395376770` on current-state evidence correction head `4fd9278db518747d93e968518680783d6310f74e`; CR-03-013 remediation advanced Codex to these GPT Pro packet/deployment CI-evidence findings.
- GPT Pro plan review: CONDITIONAL PASS / FOLLOW-UP BLOCKED. Response saved in `reviews/stage_03/GPT_PRO_REVIEW_RESPONSE.md`; action items saved in `reviews/stage_03/GPT_PRO_ACTION_ITEMS.md`. B-0040 remains open until GPT Pro follow-up confirms. B-0045, B-0046, B-0047, and B-0048 block safe Chrome/background follow-up.
- Implementation: not authorized.
