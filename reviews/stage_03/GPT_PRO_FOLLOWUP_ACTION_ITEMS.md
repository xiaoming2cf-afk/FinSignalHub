# Stage 03 GPT Pro Follow-Up Action Items

## Verdict

`PASS` for the Stage 03 planning gate.

## Must Fix Now

None for the Stage 03 planning gate.

GPT Pro explicitly resolved:

- `B-0040`: prior CONDITIONAL PASS must-fix item.
- `B-0057` / `CR-03-020`: acceptance-result live-head evidence blocker, based on live-head CI PASS and current-head Codex no-major evidence for PR #9 head `dfe38f2ecfd600bed1a38f8ad21ce9305fc5ab79`.

## Required Closeout

- Save the follow-up response and action items under `reviews/stage_03/`.
- Update `reviews/stage_03/STAGE_ACCEPTANCE_RESULT.md`.
- Update `CONTROL/24_CURRENT_STAGE_STATE.md`.
- Update `CONTROL/25_NEXT_ACTION_QUEUE.md`.
- Update `RUNLOG/LONG_RUN_CURRENT.md`.
- Update `CONTROL/18_ARTIFACT_REGISTRY.md`.

## Deferrable

- Chrome login blocker `B-0045` remains operationally relevant for future browser routes, but it no longer blocks this Stage 03 planning gate because the Chrome extension route succeeded.
- CI hardening.
- Richer connector fixture coverage.
- Later implementation refinements, to be judged during Stage 03 implementation review.

## Next Stage 03 Goal Requirements

Codex may draft Stage 03 implementation `/goal` artifacts, but must not implement connector code until the separate user-approved `/goal` begins.

The implementation goal must remain source-connector only:

- Build a connector framework.
- Build mocked connectors for OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata.
- Normalize outputs into Stage 02-compatible `SourceCreate`, `DocumentCreate`, and `ToolCallLog` payloads.

Allowed implementation files when a separate goal begins:

- `apps/api/finsignalhub_api/connectors/`
- Connector schemas/services strictly needed for normalized output.
- `apps/api/tests/test_stage03_connectors.py`
- `apps/api/tests/fixtures/stage03_connectors/`
- Stage 03 docs, logs, review packets, PR body, and deployment artifacts.

Forbidden behavior:

- Evidence extraction.
- LLM adapters.
- External live API dependency in normal tests.
- Claim graph computation.
- Research Delta computation.
- Repro Pack export logic.
- MCP business tools.
- ChatGPT, Claude, Copilot, Gemini connector implementation.
- Risk Mode.
- Replay Engine.
- Chatbot, generic RAG, dashboard behavior.
- Stock prediction.
- Investment advice.
- Auth or billing.

Required tests for implementation:

- Mocked connector tests.
- Normalized `DocumentCreate` output validation.
- Provenance mapping checks.
- No-network test enforcement.
- Fixture coverage for each connector.
- Secret scan.
- Forbidden-scope scan.
- `phase_check.py --stage 03`.
- CI PASS.
- Current-head Codex no-major.
- GPT Pro final implementation review before Stage 03 acceptance.

## Stop Conditions

Stop if implementation requires live API keys, paid credentials, external network tests, LLM extraction, claim graph logic, Research Delta computation, Repro Pack generation, MCP business tools, UI/dashboard behavior, auth/billing, Risk Mode, Replay Engine, stock/investment logic, or destructive repository restructuring.

Stop if GitHub CI or current-head Codex review becomes pending after a new commit.
