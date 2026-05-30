# Stage 03: Source Connectors

## Goal

Plan and implement Research Mode source connector primitives for OpenAlex, Crossref, Semantic Scholar, arXiv, and user upload metadata after PR #10 live-head CI/Codex and GPT Pro accepted the separate Stage 03 implementation `/goal`.

## Scope

Included:

- Stage 03 plan, tasks, checklist, review packet, PR body, acceptance placeholder, deployment placeholder, architecture doc, command doc, and subagent log README.
- Connector contract and normalized `SourceCreate`/`DocumentCreate` mapping plan aligned to the existing Stage 02 schemas.
- Mocked fixture test plan and no-network CI rule.
- Stage 03 implementation `/goal` draft artifacts and GPT Pro goal review evidence:
  - `PLANS/STAGE_03_IMPLEMENTATION_GOAL.md`
  - `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_PACKET.md`
  - `reviews/stage_03/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md`
  - `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md`
  - `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_ACTION_ITEMS.md`
- Connector primitives:
  - `apps/api/finsignalhub_api/connectors/`
  - `apps/api/tests/test_stage03_connectors.py`
  - `apps/api/tests/fixtures/stage03_connectors/`
- Connector docs and subagent evidence under `docs/architecture/stage_03_source_connectors.md`, `docs/codex/stage_03_commands.md`, and `logs/subagents/stage_03/`.

Not included:

- external API calls;
- evidence extraction;
- LLM adapters;
- claim graph or research delta computation;
- MCP business tools;
- admin UI behavior;
- chatbot, generic RAG, stock prediction, investment advice, dashboard behavior, Risk Mode, or Replay Engine.

## Checks

Checks to run before PR:

- `python -m pytest apps/api/tests/test_stage03_connectors.py`
- `python -m pytest apps/api/tests -q`
- `python -m compileall apps/api/finsignalhub_api`
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03`
- forbidden-scope scan
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
- Implementation-goal draft gate: PR #10 goal-draft head `8f10f95c69c3eaf7d6ada7b878e017b917929e33` passed live CI at https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26693919817/job/78675014690 and https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26693921040/job/78675017595, and Codex returned no-major at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10#issuecomment-4584553889.
- GPT Pro plan/closeout/goal review: PASS after Chrome follow-up, PR #10 closeout review, and implementation-goal review. Follow-up response is saved in `reviews/stage_03/GPT_PRO_FOLLOWUP_RESPONSE.md`; closeout response is saved in `reviews/stage_03/GPT_PRO_CLOSEOUT_RESPONSE.md`; implementation-goal response is saved in `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md`; action items are saved in `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_ACTION_ITEMS.md`.
- Implementation: started after PR #10 head `494c91a93e3110559047fcfba4e5ea3745cc59de` passed live CI and Codex no-major for the implementation-goal activation evidence. Connector code is bounded to source metadata normalization into existing Stage 02 schemas and fixture-only tests.
- Closeout note: if this PR body closeout is pushed as a new evidence commit, merge must verify the live PR head has CI PASS and current-head Codex no-major again. Do not require another self-referential evidence commit solely to record that external verification.
