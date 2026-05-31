# GPT Pro CR-03-043 Response

Stage: 03
PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10
Reviewed head: `dc6cea822cd7f35aee1fe2bd7116aa826ab3eb37`
Review route: Chrome extension on the specified GPT Pro page
Captured at: 2026-05-30T20:43:26-05:00

## Response

Current Stage 03 verdict: CONDITIONAL PASS. Stage 03 product boundaries remain correct. PR #10 clearly contains source connector primitives and excludes external API calls, evidence extraction, claim graph, Research Delta, MCP business tools, UI, RAG, stock/investment behavior, Risk Mode, Replay Engine, and other forbidden scope.

The current head `dc6cea8` has a new Codex review finding: old-style arXiv ids such as `physics.ins-det/0301001` and `physics.atom-ph/9901001` are rejected by the existing `_ARXIV_OLD_ID_RE`, causing `ConnectorMappingError`. This conflicts with the CR-03-042 claim that bare and versioned arXiv identifiers normalize to a stable arXiv identity.

Codex current-head no-major is not yet stable. PR #10 previously had current-head no-major evidence, but the same current head later received a Codex finding against `apps/api/finsignalhub_api/connectors/arxiv.py`. Therefore the stage cannot be treated as PASS from the earlier no-major comment.

Do not merge PR #10 now. Do not enter Stage 04 planning-only now. PR #10 may remain the active route, but this current-head Codex finding must be fixed first. After the fix, rerun local tests, CI, and request current-head Codex review. Only after a new head has CI PASS plus current-head Codex no-major may PR #10 merge and Stage 04 planning-only begin.

Must-fix:

- Extend `_ARXIV_OLD_ID_RE` to support real old-style arXiv archive classes, including at least `physics.ins-det/0301001`, `physics.atom-ph/9901001`, versioned ids such as `physics.ins-det/0301001v1`, and abs URL / PDF URL forms.
- Add regression tests proving these forms normalize to `source_identity = arxiv:<stable_old_id>` while versioned ids remain in locator/provider metadata.
- Rerun:
  - `python -m pytest apps/api/tests/test_stage03_connectors.py`
  - `python -m pytest apps/api/tests -q`
  - `python -m compileall apps/api/finsignalhub_api`
  - `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03`
  - secret scan, forbidden Stage 04 scan, and `git diff --check`.

Deferred:

- More comprehensive arXiv historical category coverage matrix.
- More provider edge-case fixtures.
- Connector observability and retry/rate-limit hardening.
- Live provider API behavior validation.

The dotted old-style archive class support named by Codex cannot be deferred.

Stage 04 planning-only requirements after PR #10 is fixed and passes: Stage 04 may only plan evidence extraction skeleton work, including extraction schema, relation enum, quote-span validation, no-quote rationale, mock LLM adapter, provenance validation, mock tests, forbidden-scope scan, CI/Codex/GPT Pro gates. It must not implement production extraction, external LLM calls, claim graph, Research Delta, Repro Pack, MCP business tools, UI/dashboard, RAG, stock/investment behavior, Risk Mode, or Replay Engine.
