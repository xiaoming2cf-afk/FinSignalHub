# GPT Pro CR-03-043 Action Items

Stage: 03
Source response: `reviews/stage_03/GPT_PRO_CR_03_043_RESPONSE.md`
Created at: 2026-05-30T20:43:26-05:00

| Item ID | Action | Required evidence | Status |
| --- | --- | --- | --- |
| GP-03-043-001 | Extend `_ARXIV_OLD_ID_RE` to accept old-style dotted archive classes such as `physics.ins-det/0301001` and `physics.atom-ph/9901001`, including versioned ids and abs/PDF URL forms. | `apps/api/finsignalhub_api/connectors/arxiv.py`; regression tests | done locally; push/CI/Codex pending |
| GP-03-043-002 | Add regression tests proving stable `arxiv:<stable_old_id>` source identity while preserving versioned locator/provider metadata. | `apps/api/tests/test_stage03_connectors.py` | done locally; push/CI/Codex pending |
| GP-03-043-003 | Rerun connector tests, full API tests, compileall, phase check, secret scan, forbidden Stage 04 scan, and diff check. | `CONTROL/18_ARTIFACT_REGISTRY.md`; `CONTROL/27_CHECKPOINT_LOG.md`; execution log | pending final post-log verification |
| GP-03-043-004 | Push the remediation head, sync PR #10 body, wait for CI, and request current-head Codex no-major. | PR #10 commit, CI links, Codex review/comment | pending |
| GP-03-043-005 | Submit GPT Pro re-review after live CI/Codex clears, then merge PR #10 only if GPT Pro accepts the current head. | GPT Pro response/action items/final result | pending |
| GP-03-043-006 | Start Stage 04 planning-only only after PR #10 current head has CI PASS, Codex no-major, and GPT Pro acceptance. | Stage 04 plan artifacts | blocked until Stage 03 closes |
