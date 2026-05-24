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
| A-0006 | 00 | acceptance result | reviews/stage_00/STAGE_ACCEPTANCE_RESULT.md | created, final BLOCKED | phase-gate-auditor | phase gate |
| A-0007 | 00 | manual GitHub steps | deployments/stage_00/MANUAL_GITHUB_STEPS.md | created | github-stage-deployer | GitHub fallback |
| A-0008 | 00 | local plugin manifest | finsignalhub-codex-plugin/.codex-plugin/plugin.json | created | plugin workflow lead | plugin registry |
| A-0009 | 00 | subagent summary | reviews/stage_00/SUBAGENT_SUMMARY.md | completed | subagent-coordinator | verification evidence |
| A-0010 | 00 | docs root README | docs/README.md | created after subagent audit | codex-log-keeper | documentation gate |
| A-0011 | 00 | plugin templates README | finsignalhub-codex-plugin/templates/README.md | created after subagent audit | codex-log-keeper | documentation gate |
| A-0012 | 00 | GPT Pro response | reviews/stage_00/GPT_PRO_REVIEW_RESPONSE.md | saved, CONDITIONAL PASS | browser-gpt-pro-reviewer | GPT Pro gate |
| A-0013 | 00 | GPT Pro action items | reviews/stage_00/GPT_PRO_ACTION_ITEMS.md | created | gpt-pro-review-preparer | GPT Pro gate |
| A-0014 | 00 | GPT Pro next-stage instruction | CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md | created | stage-next-goal-synthesizer | next-stage gate |
| A-0015 | 00 | local Git commit | `stage-00: establish control system` lineage on `stage/00-control-system`; latest pushed commit `0d94dff` | pushed | github-stage-deployer | GitHub gate partial evidence |
| A-0016 | 00 | GitHub PR URL | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1 | open | github-stage-deployer | GitHub gate |
| A-0017 | 00 | CI evidence | https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26356648275/job/77584485757 | passed | github-stage-deployer | GitHub gate |
| A-0018 | 00 | Codex review request evidence | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1#issuecomment-4527882690 | review executed | github-review-resolver | GitHub/Codex review gate |
| A-0019 | 00 | Codex review result | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1#pullrequestreview-4352049235 | reviewed with findings | github-review-resolver | GitHub/Codex review gate |
| A-0020 | 00 | Codex final follow-up | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1#issuecomment-4527956299 | no major issues | github-review-resolver | GitHub/Codex review gate |
