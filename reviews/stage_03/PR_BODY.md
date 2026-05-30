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
- CR-03-017 remediation checks: PASS locally; follow-up packet evidence head `fcd68bc` CI PASS, but Codex review `4395424386` returned CR-03-017 on blocker status consistency.
- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/9
- CI: PASS for follow-up packet evidence head `fcd68bc68b50ddd22d6fca8d62f2c8076c7d998c` with jobs https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26684736251/job/78650932138 and https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26684737012/job/78650933976. Any later blocker-status consistency correction must be verified against the live PR head before Gate 6 can pass.
- Codex review: BLOCKED by CR-03-017 from Codex review `4395424386` on follow-up packet evidence head `fcd68bc68b50ddd22d6fca8d62f2c8076c7d998c`; CR-03-016 remediation advanced Codex to this blocker-status consistency finding.
- GPT Pro plan review: CONDITIONAL PASS / FOLLOW-UP BLOCKED. Response saved in `reviews/stage_03/GPT_PRO_REVIEW_RESPONSE.md`; action items saved in `reviews/stage_03/GPT_PRO_ACTION_ITEMS.md`. B-0040 remains open until GPT Pro follow-up confirms. B-0045, B-0046, B-0047, and B-0048 block safe Chrome/background follow-up.
- Implementation: not authorized.
