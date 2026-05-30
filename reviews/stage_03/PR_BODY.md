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
- CI: PASS for pushed head `00c10afde5e6b53417e9339982e525d7a94556f8`: jobs https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26680087571/job/78638852209 and https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26680086688/job/78638849144. Any later push requires fresh CI before Gate 6 can pass.
- Codex review: PENDING LIVE-HEAD RECHECK after PR body stale-status remediation. Codex reviewed pushed head `00c10afde5e6b53417e9339982e525d7a94556f8` and returned CR-03-009 at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/9#discussion_r3328507889 because this PR body still advertised CR-03-006 as active. This body now records CR-03-006/007/008 as historical and requires a new external Codex result for the exact pushed head before Gate 6 can pass.
- GPT Pro plan review: CONDITIONAL PASS. Response saved in `reviews/stage_03/GPT_PRO_REVIEW_RESPONSE.md`; action items saved in `reviews/stage_03/GPT_PRO_ACTION_ITEMS.md`. B-0040 remains open: corrected artifacts must be committed, PR head CI/Codex must be refreshed, and GPT Pro follow-up must confirm before implementation planning.
- Implementation: not authorized.
