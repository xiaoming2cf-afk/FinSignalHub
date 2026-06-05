# Stage 04: Evidence Extraction Planning

## Goal

Plan an evidence extraction skeleton for FinSignalHub Research Mode. This is planning only and does not create extraction implementation code.

## Scope

Included:

- Stage 04 plan, tasks, checklist, review packet, PR body, acceptance placeholder, deployment placeholder, architecture doc, command doc, and subagent log README.
- Future extraction candidate schema boundaries.
- Future relation type enum boundaries.
- Quote-span validation and no-quote rationale plan.
- Provenance validation plan.
- Mock LLM extraction adapter plan with no external calls.
- Future extraction worker skeleton plan.
- Mock-only test plan.
- GitHub, Codex, and GPT Pro plan review gates.

Not included:

- extraction implementation package;
- Stage 04 tests or fixtures;
- production extraction;
- external LLM calls;
- claim graph, Research Delta, or Repro Pack logic;
- MCP business tools;
- UI/dashboard behavior;
- chatbot, generic RAG, stock prediction, investment advice, Risk Mode, or Replay Engine.

## Checks

Checks to run before PR:

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04`
- no `apps/api/finsignalhub_api/extraction/`
- no `apps/api/tests/test_stage04_extraction.py`
- no `apps/api/tests/fixtures/stage04_extraction/`
- forbidden-scope scan
- high-confidence secret scan
- `git diff --check`

## Review

After PR creation, request:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

GPT Pro review remains a hard gate before any Stage 04 implementation can start.

## Current Gate Status

- Stage 03: merged at `13ee0a0bc497578b235662ea60c9aa225c62e53f` and tagged `stage-03-source-connectors`.
- Stage 04 planning branch: `stage/04-evidence-extraction`.
- Local planning checks: PASS for `phase_check.py --stage 04`, forbidden extraction path checks, high-confidence secret scan, `git diff --check`, and registry ID uniqueness.
- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11
- CI: reviewed implementation-goal head `e6cb1052572d84f1c0f0fa7041e210e72d64d104` passed both governance checks. This response-saving evidence-sync head must also pass live PR #11 current-head checks after push; Gate 6 is determined by live PR #11 state, not a stale fixed hash copied into this file.
- Codex review: reviewed implementation-goal head `e6cb1052572d84f1c0f0fa7041e210e72d64d104` received Codex no-major at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11#issuecomment-4635387837. All review threads were resolved before GPT Pro implementation-goal review: unresolved = 0.
- GPT Pro review: PASS for Stage 04 planning, closeout confirmation, final closeout recheck, and implementation-goal draft. Implementation-goal response/action items are saved in `GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md` and `GPT_PRO_IMPLEMENTATION_GOAL_ACTION_ITEMS.md`.
- Stage 04 implementation: not started; blocked until this evidence-sync head passes live CI, current-head Codex, and unresolved review threads = 0, then it must start only under the accepted `/goal`.
