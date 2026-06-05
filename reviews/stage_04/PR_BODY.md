# Stage 04: Evidence Extraction Implementation

## Goal

Implement the approved Stage 04 mock-only evidence extraction skeleton for FinSignalHub Research Mode.

The implementation converts Stage 03 normalized `DocumentCreate` inputs plus Stage 04-owned fixture text into provenance-preserving evidence candidate payloads. It does not persist evidence, compute graph state, compute research deltas, export repro packs, expose MCP business tools, build UI behavior, call real providers, call external model services, or require secrets.

## Scope

Included:

- Candidate schemas for evidence text, quote spans, no-quote rationale, relation labels, confidence, provenance, tool-call lineage, and candidate-only output.
- Bounded Stage 04 relation enum.
- Exact quote-span validation against fixture document text.
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

- PASS: `python -m pytest apps/api/tests/test_stage04_extraction.py` -> 12 passed.
- PASS: `python -m pytest apps/api/tests/test_stage02_forbidden_scope.py apps/api/tests/test_stage03_connectors.py apps/api/tests/test_stage04_extraction.py -q` -> 36 passed.
- PASS: `python -m pytest apps/api/tests -q --maxfail=1` -> 88 passed.
- PASS: `python -m compileall apps/api/finsignalhub_api`.
- PASS: `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04`.
- PASS: high-confidence secret scan on changed Stage 04 paths returned no matches.
- PASS: runtime forbidden-scope scan returned no matches.
- PASS: `git diff --check` had only normal Windows line-ending warnings.

## Review

After pushing the implementation head, request:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

GPT Pro final implementation review remains a hard gate after live PR #11 CI, current-head Codex no-major, and unresolved review threads = 0.

## Current Gate Status

- Stage 03: merged at `13ee0a0bc497578b235662ea60c9aa225c62e53f` and tagged `stage-03-source-connectors`.
- Stage 04 branch: `stage/04-evidence-extraction`.
- PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11
- Pre-implementation gate head: `2a6378cf12953e3f376bd29a3cf208c7f2b01d8a`.
- Pre-implementation CI: PASS.
- Pre-implementation Codex: no-major at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/11#issuecomment-4635836603.
- GPT Pro implementation-goal review: PASS, saved in `reviews/stage_04/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md`.
- Implementation local status: PASS.
- Implementation GitHub/Codex status: BLOCKED/PENDING until this implementation head is pushed, CI passes, current-head Codex returns no major issues, and unresolved review threads = 0.
- GPT Pro final implementation status: BLOCKED/PENDING until the final packet is submitted after the live GitHub/Codex gate.
