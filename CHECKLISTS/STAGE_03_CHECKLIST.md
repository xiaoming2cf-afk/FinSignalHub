# Stage 03 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Source connector primitive implementation remains fixture-only; no external calls or Stage 04+ behavior | PASS |
| Functionality | Connector contracts normalize OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata into existing `SourceCreate`, `DocumentCreate`, and `ToolCallLogCreate` payloads | PASS locally; CR-03-042 remediation pending live CI/Codex |
| Tests | Mocked fixture tests, no-network CI rule, local implementation checks, and CR-03-042 regression checks are recorded in `CONTROL/18_ARTIFACT_REGISTRY.md` and `CONTROL/27_CHECKPOINT_LOG.md` | PASS locally; push/CI/Codex pending |
| Docs | Architecture and command docs exist | PASS |
| Logs | CONTROL and RUNLOG entries updated | PASS |
| GitHub | Branch, PR, CI, Codex review, PR URL | BLOCKED by CR-03-042 until the arXiv stable identity remediation head passes live PR #10 CI and current-head Codex. Evidence-closeout head `bd33c4f1147c48dcf9573cee2c8546bbdfd5daf0` passed CI but received https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10#discussion_r3329475873. |
| GPT Pro | Plan packet, response, action items, final result | PASS for final implementation head `039e3d087c84f6ec61a6107b6f55b628d8a79ee6`; re-review will be required after CR-03-042 remediation head passes live CI/Codex because implementation code changed after the prior final PASS. |
| Product governance | Mapping stays Research Mode evidence-stream oriented | PASS |
| Security | No secrets, no paid/private API dependency, no live network CI | PASS |
| Next stage | GPT Pro gives implementation or next-stage instruction | Stage 04 planning only is authorized by GPT Pro, but blocked until CR-03-042 remediation passes live CI/Codex and final GPT Pro re-review if required. |

Current Stage 03 status: final implementation head `039e3d087c84f6ec61a6107b6f55b628d8a79ee6` passed CI/Codex and GPT Pro final review. Evidence-closeout head `bd33c4f1147c48dcf9573cee2c8546bbdfd5daf0` passed CI but Codex returned CR-03-042. Local remediation stabilizes arXiv source identity and must pass live PR #10 CI/Codex before merge or Stage 04 planning PR work.
