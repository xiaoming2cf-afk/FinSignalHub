# 18 Artifact Registry

## Purpose

Tracks documents, PRs, review packets, responses, action items, export artifacts, and acceptance evidence.

## Owner

Acceptance evidence collector.

## When to update

Update whenever an artifact is created, changed, submitted, reviewed, or superseded.

## Required fields

- Artifact ID
- Stage
- Type
- Path or URL
- Status
- Owner
- Evidence use

## Example format

`A-0001 | Stage 00 | review packet | reviews/stage_00/GPT_PRO_REVIEW_PACKET.md | created | GPT Pro gate`

## Current state

| Artifact ID | Stage | Type | Path or URL | Status | Owner | Evidence use |
| --- | --- | --- | --- | --- | --- | --- |
| A-0001 | 00 | plan | PLANS/STAGE_00_PLAN.md | created | Codex | Stage 00 scope |
| A-0002 | 00 | capability audit | CONTROL/16_CAPABILITY_AUDIT.md | created | ai-capability-radar | capability gate |
| A-0003 | 00 | review packet | reviews/stage_00/GPT_PRO_REVIEW_PACKET.md | created and submitted to GPT Pro | gpt-pro-review-preparer | GPT Pro gate |
| A-0004 | 00 | PR body | reviews/stage_00/PR_BODY.md | created | github-stage-deployer | GitHub gate |
| A-0005 | 00 | GitHub PR | deployments/stage_00/GITHUB_PR.md | open; PR URL and CI evidence saved | github-stage-deployer | GitHub gate |
| A-0006 | 00 | acceptance result | reviews/stage_00/STAGE_ACCEPTANCE_RESULT.md | final PASS | phase-gate-auditor | phase gate |
| A-0007 | 00 | manual GitHub steps | deployments/stage_00/MANUAL_GITHUB_STEPS.md | created | github-stage-deployer | GitHub fallback |
| A-0008 | 00 | local plugin manifest | finsignalhub-codex-plugin/.codex-plugin/plugin.json | created | plugin workflow lead | plugin registry |
| A-0009 | 00 | subagent summary | reviews/stage_00/SUBAGENT_SUMMARY.md | completed | subagent-coordinator | verification evidence |
| A-0010 | 00 | docs root README | docs/README.md | created after subagent audit | codex-log-keeper | documentation gate |
| A-0011 | 00 | plugin templates README | finsignalhub-codex-plugin/templates/README.md | created after subagent audit | codex-log-keeper | documentation gate |
| A-0012 | 00 | GPT Pro response | reviews/stage_00/GPT_PRO_REVIEW_RESPONSE.md | saved, initial CONDITIONAL PASS plus final PASS confirmation | browser-gpt-pro-reviewer | GPT Pro gate |
| A-0013 | 00 | GPT Pro action items | reviews/stage_00/GPT_PRO_ACTION_ITEMS.md | updated with final PASS and deferred items | gpt-pro-review-preparer | GPT Pro gate |
| A-0014 | 00 | GPT Pro next-stage instruction | CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md | updated with final PASS confirmation | stage-next-goal-synthesizer | next-stage gate |
| A-0015 | 00 | local Git commit | `stage-00: establish control system` lineage on `stage/00-control-system`; latest pushed commit `0d94dff` | pushed | github-stage-deployer | GitHub gate partial evidence |
| A-0016 | 00 | GitHub PR URL | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1 | open | github-stage-deployer | GitHub gate |
| A-0017 | 00 | CI evidence | https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26356648275/job/77584485757 | passed | github-stage-deployer | GitHub gate |
| A-0018 | 00 | Codex review request evidence | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1#issuecomment-4527882690 | review executed | github-review-resolver | GitHub/Codex review gate |
| A-0019 | 00 | Codex review result | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1#pullrequestreview-4352049235 | reviewed with findings | github-review-resolver | GitHub/Codex review gate |
| A-0020 | 00 | Codex final follow-up | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1#issuecomment-4527956299 | no major issues on `6ef3045` | github-review-resolver | GitHub/Codex review gate |
| A-0021 | 00 | Codex latest finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1#discussion_r3294203712 | fixed in `f0c1d70` and re-reviewed | github-review-resolver | GitHub/Codex review gate |
| A-0022 | 00 | Codex latest final response | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1#issuecomment-4527990187 | no major issues on `f0c1d70` | github-review-resolver | GitHub/Codex review gate |
| A-0023 | 00 | GPT Pro final confirmation | reviews/stage_00/GPT_PRO_REVIEW_RESPONSE.md#final-stage-00-confirmation | PASS for Stage 00 / prompt 1 | browser-gpt-pro-reviewer | GPT Pro gate |
| A-0024 | 00 | release note | deployments/stage_00/RELEASE_NOTE.md | created | github-stage-deployer | Stage 00 release evidence |
| A-0025 | 00 | final subagent audit | logs/subagents/stage_00/fermat-final-audit.md | completed with commit/push blocker | subagent-coordinator | final verification evidence |
| A-0026 | 00 | final acceptance commit | `ed0ba1d` on `stage/00-control-system` | pushed, CI passed, Codex no-major-issues | github-stage-deployer | final PR evidence |
| A-0027 | 00 | final acceptance CI evidence | https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26358482261 and https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26358481283 | passed | github-stage-deployer | GitHub gate |
| A-0028 | 00 | final Codex response | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1#issuecomment-4528067149 | no major issues on `ed0ba1d` | github-review-resolver | GitHub/Codex review gate |
| A-0029 | 00 | post-acceptance capability PR | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/2 | merged; CI passed; Codex follow-up found no major issues after fix | github-stage-deployer | follow-up capability evidence |
| A-0030 | 00 | PR #2 Codex finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/2#discussion_r3294400269 | fixed and verified | github-review-resolver | provenance clarity evidence |
| A-0031 | 00 | PR #2 Codex follow-up response | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/2#issuecomment-4528561687 | no major issues after `63c428d` | github-review-resolver | follow-up Codex evidence |
| A-0032 | 00 | GPT Pro post-acceptance capability response | reviews/stage_00/GPT_PRO_POST_ACCEPTANCE_RESPONSE.md | PASS; Stage 01 planning allowed only | browser-gpt-pro-reviewer | post-acceptance GPT Pro evidence |
| A-0033 | 00 | GPT Pro confirmation PR | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/3 | merged; CI passed; Codex no-major-issues | github-stage-deployer | final GPT Pro evidence PR |
| A-0034 | 00 | PR #3 Codex response | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/3#issuecomment-4528988041 | no major issues | github-review-resolver | final Codex evidence |
| A-0035 | 00 | prompt completion confirmation audit | CONTROL/00_MASTER_CONTROL.md; CONTROL/06_GPT_PRO_REVIEW_PROTOCOL.md; CONTROL/11_GITHUB_DEPLOYMENT_PROTOCOL.md; deployments/stage_00/RELEASE_NOTE.md | stale early-blocker wording corrected on confirmation branch | acceptance-evidence-collector | final prompt-by-prompt completion evidence |
| A-0036 | 00 | prompt completion confirmation PR | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/4 | merged; CI passed; Codex found no major issues on final branch commit | github-stage-deployer | final user-prompt confirmation evidence |
| A-0037 | 00 | PR #4 Codex response | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/4#issuecomment-4529061051 | no major issues on final branch commit | github-review-resolver | final prompt-completion Codex evidence |
| A-0038 | 00.1 | approved run instruction input | 运行要求/FinSignalHub_Codex_RunLog_Autonomous_Prompt.md | committed input artifact pending PR | codex-log-keeper | autonomous run source |
| A-0039 | 00.1 | RunLog control files | CONTROL/23_RUNLOG_PROTOCOL.md; CONTROL/24_CURRENT_STAGE_STATE.md; CONTROL/25_NEXT_ACTION_QUEUE.md; CONTROL/26_AUTONOMOUS_RUN_RULES.md; CONTROL/27_CHECKPOINT_LOG.md | created pending review | codex-log-keeper | RunLog governance |
| A-0040 | 00.1 | Stage 00.1 review packet | reviews/stage_00_1/GPT_PRO_REVIEW_PACKET.md | created pending GPT Pro submission | gpt-pro-review-preparer | GPT Pro gate |
| A-0041 | 00.1 | plugin helper scripts | finsignalhub-codex-plugin/scripts/phase_check.py; finsignalhub-codex-plugin/scripts/log_append.py; finsignalhub-codex-plugin/scripts/export_review_packet.py | created pending checks | github-stage-deployer | deterministic governance helpers |
| A-0042 | 00.1 | Stage 00.1 Codex review summary | reviews/stage_00_1/CODEX_REVIEW_SUMMARY.md | updated through CR-00.1-019; current evidence-sync commit requires CI and follow-up review | github-review-resolver | Codex review gate |
| A-0043 | 00.1 | PR #6 Codex no-major-issues response | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#issuecomment-4529453824 | previous no-major-issues response before latest evidence-sync commit | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0044 | 00.1 | PR #6 latest Codex P2 findings | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295036278; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295036279 | resolved by later pushed commits; superseded by current evidence-sync follow-up gate | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0045 | 00.1 | PR #6 log helper Codex P2 finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295060654 | resolved by later pushed commits; superseded by current evidence-sync follow-up gate | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0046 | 00.1 | read-only subagent verification | subagent notification from Lorentz | completed; governance-only boundary, RunLog order, exporter failure behavior passed; GPT Pro blocked until Codex latest review clears | subagent-coordinator | independent Stage 00.1 verification |
| A-0047 | 00.1 | PR #6 phase-check plan-artifact Codex P2 finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295075137 | resolved by later pushed commits; superseded by current evidence-sync follow-up gate | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0048 | 00.1 | PR #6 helper-boundary Codex P2 findings | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295087893; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295087894; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295087896 | resolved by later pushed commits; superseded by current evidence-sync follow-up gate | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0049 | 00.1 | PR #6 traversal-segment Codex P2 findings | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295100569; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295100573 | resolved by later pushed commits; superseded by current evidence-sync follow-up gate | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0050 | 00.1 | PR #6 recursive runtime-guard Codex P2 finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295113966 | resolved by later pushed commits; superseded by current evidence-sync follow-up gate | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0051 | 00.1 | PR #6 plan test-category Codex P2 finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295125966 | resolved by later pushed commits; superseded by current evidence-sync follow-up gate | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0052 | 00.1 | PR #6 local-environment false-positive Codex P1 finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295138487 | fixed and pushed in `4c59773b6f5f6f7ecf9b5ef8dd423258a0d00f36`; CI passed; follow-up Codex review pending | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0053 | 00.1 | PR #6 post-P1 CI evidence | https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26369899386/job/77620115542; https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26369900324/job/77620117626 | passed on `4c59773b6f5f6f7ecf9b5ef8dd423258a0d00f36`; awaiting follow-up Codex review before GPT Pro submission | github-stage-deployer | Stage 00.1 GitHub/Codex gate |
| A-0054 | 00.1 | Stage 00.1 subagent evidence | reviews/stage_00_1/SUBAGENT_SUMMARY.md; logs/subagents/stage_00_1/lorentz-readonly-verification.md | added as required Stage 00.1 governance evidence; phase_check now requires these files | subagent-coordinator | Stage 00.1 subagent gate evidence |
| A-0055 | 00.1 | Newton read-only verification | logs/subagents/stage_00_1/newton-readonly-verification.md | completed; stale evidence findings integrated locally before commit | subagent-coordinator | Stage 00.1 subagent gate evidence |
| A-0056 | 00.1 | PR #6 safe export P2 finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295180243 | fixed in `43c570a1291b262faba32f288b29b0dfbf396029`; Codex follow-up found no major issues | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0057 | 00.1 | PR #6 future-stage phase-check P2 finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295180241 | fixed in `43c570a1291b262faba32f288b29b0dfbf396029`; Codex follow-up found no major issues | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0058 | 00.1 | PR #6 latest Codex no-major response | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#issuecomment-4529747962 | no major issues on `43c570a1291b262faba32f288b29b0dfbf396029`; GPT Pro review may proceed | github-review-resolver | Stage 00.1 GitHub/Codex gate |
| A-0059 | 00.1 | Stage 00.1 GPT Pro response | reviews/stage_00_1/GPT_PRO_REVIEW_RESPONSE.md | PASS; Stage 01 planning only authorized | browser-gpt-pro-reviewer | Stage 00.1 GPT Pro gate |
| A-0060 | 00.1 | Stage 00.1 GPT Pro action items | reviews/stage_00_1/GPT_PRO_ACTION_ITEMS.md | created; implementation blockers carried forward | gpt-pro-review-preparer | Stage 01 boundary evidence |
| A-0061 | 00.1 | Stage 00.1 release note | deployments/stage_00_1/RELEASE_NOTE.md | created; tag pending after PR merge/final accepted commit | github-stage-deployer | release evidence |
| A-0062 | 00.1 | Stage 01 GPT Pro instruction | CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md | updated from Stage 00.1 PASS response | stage-next-goal-synthesizer | next-stage gate |
| A-0063 | 00.1 | Chrome GPT Pro text capture | artifacts/chrome_gpt_stage_00_1_clipboard.txt | retained as text-only source capture for response extraction | browser-gpt-pro-reviewer | GPT Pro source evidence |
| A-0064 | 00.1 | PR #6 final evidence Codex findings | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295227866; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#discussion_r3295227867 | fixed in `897759b74cecff6c461bc5a7f3ee0f71d4071e18`; Codex follow-up found no major issues | github-review-resolver | final GitHub/Codex gate |
| A-0065 | 00.1 | PR #6 final Codex no-major response | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#issuecomment-4529839137 | no major issues on `897759b74cecff6c461bc5a7f3ee0f71d4071e18` | github-review-resolver | Stage 00.1 final GitHub/Codex gate |
| A-0066 | 01 | Stage 01 plan | PLANS/STAGE_01_PLAN.md | created; GPT Pro plan review PASS; all known Codex plan findings through CR-01-011 addressed | gpt-pro-review-preparer | Stage 01 plan gate |
| A-0067 | 01 | Stage 01 GPT Pro plan packet | reviews/stage_01/GPT_PRO_REVIEW_PACKET.md | submitted; GPT Pro plan PASS saved | gpt-pro-review-preparer | GPT Pro plan gate |
| A-0068 | 01 | Stage 01 PR body | reviews/stage_01/PR_BODY.md | created | github-stage-deployer | GitHub PR gate |
| A-0069 | 01 | Stage 01 acceptance placeholder | reviews/stage_01/STAGE_ACCEPTANCE_RESULT.md | created; implementation pending | phase-gate-auditor | phase gate |
| A-0070 | 01 | Stage 01 PR | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7 | open; CI passed on latest observed pushed head; current-head Codex follow-up pending | github-stage-deployer | Stage 01 planning PR evidence |
| A-0071 | 01 | Stage 01 GPT Pro plan response | reviews/stage_01/GPT_PRO_PLAN_REVIEW_RESPONSE.md | PASS; implementation conditional | browser-gpt-pro-reviewer | GPT Pro plan gate |
| A-0072 | 01 | Stage 01 GPT Pro plan action items | reviews/stage_01/GPT_PRO_PLAN_ACTION_ITEMS.md | created | gpt-pro-review-preparer | implementation blocker evidence |
| A-0073 | 01 | PR #7 Codex plan findings | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295252557; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295252560 | CR-01-001/002 fixed; superseded by current-head follow-up gate | github-review-resolver | Stage 01 plan Codex gate |
| A-0074 | 01 | Chrome GPT Pro Stage 01 plan text capture | artifacts/chrome_gpt_stage_01_plan_clipboard.txt | sanitized to retain only project review evidence after Codex privacy finding | browser-gpt-pro-reviewer | GPT Pro plan source evidence |
| A-0076 | 01 | PR #7 artifact/state Codex findings | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295276199; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295276203; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295276205 | CR-01-005/006/007 fixed; superseded by current-head follow-up gate | github-review-resolver | Stage 01 plan Codex gate |
| A-0075 | 01 | PR #7 Codex follow-up findings | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295260288; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295260290 | CR-01-003/004 fixed; superseded by current-head follow-up gate | github-review-resolver | Stage 01 plan Codex gate |
| A-0077 | 01 | PR #7 current-state follow-up finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295289004 | CR-01-008 fixed; superseded by current-head follow-up gate | github-review-resolver | Stage 01 plan Codex gate |
| A-0078 | 01 | PR #7 status-sync follow-up findings | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295301747; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295301748; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295301750 | CR-01-009/010/011 fixed; current-head Codex follow-up pending | github-review-resolver | Stage 01 plan Codex gate |
| A-0079 | 01 | Stage 01 Codex review summary | reviews/stage_01/CODEX_REVIEW_SUMMARY.md | created; summarizes CR-01-001 through CR-01-014 and current follow-up blocker | github-review-resolver | Stage 01 plan Codex gate |
| A-0080 | 01 | PR #7 dashboard status Codex finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295312100 | CR-01-012 fixed locally; current-head Codex follow-up pending | github-review-resolver | Stage 01 dashboard/GitHub gate |
| A-0081 | 01 | PR #7 checklist security Codex finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295320209 | CR-01-013 fixed locally; current-head Codex follow-up pending | github-review-resolver | Stage 01 checklist/GitHub gate |
| A-0082 | 01 | PR #7 functionality blocker Codex finding | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#discussion_r3295327617 | CR-01-014 fixed locally; current-head Codex follow-up pending | github-review-resolver | Stage 01 checklist/GitHub gate |
| A-0083 | 01 | Docker validation evidence | local command output: `docker version`, `docker compose version`, `docker context ls` | PASS on 2026-05-26: Server 29.3.1, Docker Desktop 4.67.0, Compose v5.1.1, context `desktop-linux` | ai-capability-radar | Stage 01 implementation readiness gate |
