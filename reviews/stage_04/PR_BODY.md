# Stage 04: Evidence Extraction Implementation

## Goal

Implement the approved Stage 04 mock-only evidence extraction skeleton for FinSignalHub Research Mode.

The implementation converts Stage 03 normalized `DocumentCreate` inputs plus Stage 04-owned fixture text into provenance-preserving evidence candidate payloads. It does not persist evidence, compute graph state, compute research deltas, export repro packs, expose MCP business tools, build UI behavior, call real providers, call external model services, or require secrets.

## Scope

Included:

- Candidate schemas for evidence text, quote spans, no-quote rationale, relation labels, confidence, provenance, tool-call lineage, and candidate-only output.
- Bounded Stage 04 relation enum.
- Exact quote-span validation against fixture document text, including locator-only spans that must still match source text.
- No-quote rationale validation for metadata-only inputs.
- Provenance validation between normalized document payloads and candidates.
- Deterministic mock model output from fixtures only.
- Worker skeleton that validates candidate payloads and does not persist them.
- Mock-only Stage 04 tests and fixtures.
- Stage 04 architecture docs, command docs, subagent logs, review artifacts, deployment evidence, and control logs.

Not included:

- Database migrations or persisted domain model changes.
- Connector behavior changes or live provider calls.
- External model calls, provider SDKs, paid services, credentials, or secrets.
- Claim graph, Research Delta, Repro Pack, MCP business tools, UI/dashboard behavior, chatbot, generic RAG, stock prediction, investment advice, Risk Mode, Replay Engine, auth, or billing.

## Local Checks

- PASS: `python -m pytest apps/api/tests/test_stage04_extraction.py -q` -> 15 passed.
- PASS: `python -m pytest apps/api/tests/test_stage02_forbidden_scope.py apps/api/tests/test_stage03_connectors.py apps/api/tests/test_stage04_extraction.py -q` -> 39 passed.
- PASS: `python -m pytest apps/api/tests -q --maxfail=1` -> 91 passed.
- PASS: `python -m compileall apps/api/finsignalhub_api`.
- PASS: `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04`.
- PASS: high-confidence secret scan on changed Stage 04 paths returned no matches.
- PASS: runtime forbidden-scope scan returned no matches.
- PASS: `git diff --check` had only normal Windows line-ending warnings.
- PASS for B-0102 evidence-sync: Stage 04 tests 15/15, compileall, phase check, high-confidence credential scan, artifact/checkpoint/blocker ID uniqueness, and `git diff --check`.
- PASS for B-0103 CR-04-040/041 remediation: Stage 04 tests 15/15, phase check, high-confidence credential scan, artifact/checkpoint/blocker ID uniqueness, and `git diff --check`.

## Review

After pushing the implementation head, request:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

GPT Pro final implementation review returned PASS for reviewed head `79ec29a42b9119dbaf5edd1c88b7fb4e52fe1368`. Later governance-only CR-04-030 through CR-04-038 findings are historical. CR-04-039 locator-only quote validation was remediated, pushed, passed live CI/Codex/thread gates as PR #11 head `cd3c1cfeef0dc075f5fd35cfd4d6451c712e75df`, and GPT Pro returned current-head PASS.

Current follow-up B-0103: PR #11 evidence-sync head `00e28d697ac292ac000b91e3839f1d8cd5367a93` passed CI, but Codex opened CR-04-040/041 because `CHANGELOG.md` contained internal gate bookkeeping and `CONTROL/24_CURRENT_STAGE_STATE.md` still routed next work through completed local checks. This patch removes the changelog entry, updates current-state routing, and passed CP-0361 local checks. The remediation head must pass live PR #11 CI, current-head Codex no-major, and unresolved review threads = 0 before merge/tag.

## Current Gate Status

- Stage 03: merged at `13ee0a0bc497578b235662ea60c9aa225c62e53f` and tagged `stage-03-source-connectors`.
- Stage 04 branch: `stage/04-evidence-extraction`.
- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11
- Pre-implementation gate head: `2a6378cf12953e3f376bd29a3cf208c7f2b01d8a`.
- Pre-implementation CI: PASS.
- Pre-implementation Codex: no-major at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11#issuecomment-4635836603.
- GPT Pro implementation-goal review: PASS, saved in `reviews/stage_04/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md`.
- Implementation local status: PASS.
- Implementation GitHub/Codex status: BLOCKED by B-0103. Head `00e28d697ac292ac000b91e3839f1d8cd5367a93` passed CI, but Codex opened CR-04-040/041. The B-0103 remediation passed local checks and must pass live PR #11 CI, current-head Codex no-major, and unresolved review threads = 0 before merge/tag.
- GPT Pro final implementation status: PASS for reviewed head `cd3c1cfeef0dc075f5fd35cfd4d6451c712e75df`. Current-head response: `reviews/stage_04/GPT_PRO_CURRENT_HEAD_FINAL_REVIEW_RESPONSE.md`; action items: `reviews/stage_04/GPT_PRO_CURRENT_HEAD_FINAL_ACTION_ITEMS.md`.
- Next-stage status: GPT Pro authorized Stage 05 planning only. Stage 05 implementation remains blocked until a separate Stage 05 plan review and implementation-goal approval.
