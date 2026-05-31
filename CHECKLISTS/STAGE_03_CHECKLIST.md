# Stage 03 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Source connector primitive implementation remains fixture-only; no external calls or Stage 04+ behavior | PASS |
| Functionality | Connector contracts normalize OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata into existing `SourceCreate`, `DocumentCreate`, and `ToolCallLogCreate` payloads | PASS locally; CR-03-043 remediation pending live CI/Codex/GPT Pro |
| Tests | Mocked fixture tests, no-network CI rule, local implementation checks, and CR-03-043 regression checks are recorded in `CONTROL/18_ARTIFACT_REGISTRY.md` and `CONTROL/27_CHECKPOINT_LOG.md` | PASS locally; push/CI/Codex/GPT Pro pending |
| Docs | Architecture and command docs exist | PASS |
| Logs | CONTROL and RUNLOG entries updated | PASS |
| GitHub | Branch, PR, CI, Codex review, PR URL | BLOCKED by CR-03-043 until the old-style arXiv id remediation head passes live PR #10 CI and current-head Codex. CR-03-042 remediation head `dc6cea822cd7f35aee1fe2bd7116aa826ab3eb37` passed CI but received https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10#discussion_r3329560001. |
| GPT Pro | Plan packet, response, action items, final result | CONDITIONAL PASS for CR-03-043 saved in `reviews/stage_03/GPT_PRO_CR_03_043_RESPONSE.md`; re-review is required after CR-03-043 remediation head passes live CI/Codex. |
| Product governance | Mapping stays Research Mode evidence-stream oriented | PASS |
| Security | No secrets, no paid/private API dependency, no live network CI | PASS |
| Next stage | GPT Pro gives implementation or next-stage instruction | Stage 04 planning only is authorized by GPT Pro historically, but currently blocked until CR-03-043 remediation passes live CI/Codex and GPT Pro re-review. |

Current Stage 03 status: final implementation head `039e3d087c84f6ec61a6107b6f55b628d8a79ee6` passed CI/Codex and GPT Pro final review. CR-03-042 remediation head `dc6cea822cd7f35aee1fe2bd7116aa826ab3eb37` passed CI but Codex returned CR-03-043. Local remediation supports old-style dotted arXiv archive classes and must pass live PR #10 CI/Codex/GPT Pro before merge or Stage 04 planning PR work.
