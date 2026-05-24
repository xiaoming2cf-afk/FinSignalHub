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
