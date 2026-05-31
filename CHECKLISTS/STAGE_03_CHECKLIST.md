# Stage 03 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Source connector primitive implementation remains fixture-only; no external calls or Stage 04+ behavior | PASS |
| Functionality | Connector contracts normalize OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata into existing `SourceCreate`, `DocumentCreate`, and `ToolCallLogCreate` payloads | PASS for reviewed code head `adb41c36e66a25ddfa943950b7e08a685906560e`; CR-03-043 accepted by GPT Pro |
| Tests | Mocked fixture tests, no-network CI rule, local implementation checks, and CR-03-043 regression checks are recorded in `CONTROL/18_ARTIFACT_REGISTRY.md` and `CONTROL/27_CHECKPOINT_LOG.md` | PASS locally and in PR #10 CI for reviewed code head; evidence-closeout commit live CI/Codex pending after push |
| Docs | Architecture and command docs exist | PASS |
| Logs | CONTROL and RUNLOG entries updated | PASS |
| GitHub | Branch, PR, CI, Codex review, PR URL | PASS for reviewed code head `adb41c36e66a25ddfa943950b7e08a685906560e`: CI jobs and current-head Codex no-major evidence are recorded; evidence-closeout commit still requires live CI/Codex after push. |
| GPT Pro | Plan packet, response, action items, final result | PASS for CR-03-043 re-review saved in `reviews/stage_03/GPT_PRO_CR_03_043_REREVIEW_RESPONSE.md`; action items saved in `reviews/stage_03/GPT_PRO_CR_03_043_REREVIEW_ACTION_ITEMS.md`. |
| Product governance | Mapping stays Research Mode evidence-stream oriented | PASS |
| Security | No secrets, no paid/private API dependency, no live network CI | PASS |
| Next stage | GPT Pro gives implementation or next-stage instruction | Stage 04 planning only is authorized by GPT Pro after Stage 03 evidence closeout has live CI/Codex; Stage 04 implementation remains unauthorized. |

Current Stage 03 status: final implementation head `039e3d087c84f6ec61a6107b6f55b628d8a79ee6` passed CI/Codex and GPT Pro final review. CR-03-042 remediation head `dc6cea822cd7f35aee1fe2bd7116aa826ab3eb37` passed CI but Codex returned CR-03-043. CR-03-043 remediation head `adb41c36e66a25ddfa943950b7e08a685906560e` passed CI, received current-head Codex no-major evidence, and GPT Pro re-review PASS. This governance-only evidence update must pass live PR #10 CI/Codex after push before merge or Stage 04 planning PR work.
