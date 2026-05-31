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
- Codex CR-03-041 remediation:
  - canonical `ToolCallLog.safe_arguments` provenance fields cannot be overwritten by `extra_safe_arguments`;
  - extra fixture arguments are sanitized under `safe_arguments.extra`;
  - regression test covers spoofed provider, fixture, fixture id, query ref, source identity, and secret-like key inputs.
- Codex CR-03-042 remediation:
  - arXiv raw ids, versioned ids, `arXiv:` prefixed ids, abs URLs, and PDF URLs normalize to stable `arxiv:<id>` source identity;
  - versioned arXiv ids remain preserved as locator/provider metadata;
  - fallback arXiv abs URLs are canonicalized without live network calls.
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
- Accepted planning evidence: head `dfe38f2ecfd600bed1a38f8ad21ce9305fc5ab79` passed CI and Codex no-major, then GPT Pro accepted that evidence.
- Implementation-goal draft gate: PR #10 goal-draft head `8f10f95c69c3eaf7d6ada7b878e017b917929e33` passed live CI and Codex no-major, then GPT Pro returned `VERDICT: PASS`.
- Implementation activation gate: PR #10 head `494c91a93e3110559047fcfba4e5ea3745cc59de` passed live CI and Codex no-major before connector code began.
- Implementation remediation gate: PR #10 remediation head `039e3d087c84f6ec61a6107b6f55b628d8a79ee6` passed governance CI at https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26697384029/job/78684104587 and https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26697382826/job/78684101177, and Codex returned no-major at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10#issuecomment-4585119196.
- GPT Pro final implementation review: PASS. Response is saved in `reviews/stage_03/GPT_PRO_FINAL_REVIEW_RESPONSE.md`; action items are saved in `reviews/stage_03/GPT_PRO_FINAL_ACTION_ITEMS.md`.
- CR-03-041: resolved for implementation head. Extra fixture arguments are sanitized under `safe_arguments.extra`; canonical `provider`, `query_ref`, `fixture`, `fixture_id`, and `source_identity` fields remain authoritative.
- CR-03-042: locally remediated after Codex reviewed evidence-closeout head `bd33c4f1147c48dcf9573cee2c8546bbdfd5daf0` and found unstable arXiv identity normalization. Connector tests now cover bare, versioned, prefixed, abs URL, and PDF URL id forms.
- Stage 04: GPT Pro authorized planning only. Stage 04 implementation is not authorized.
- Closeout note: this CR-03-042 remediation commit must pass live PR #10 CI and current-head Codex before merge or Stage 04 planning PR work. Do not create another self-referential evidence commit solely to record that verification unless a reviewer requires a content correction.
