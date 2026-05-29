# 07 Codex Goal Registry

## Purpose

Tracks every approved Codex goal and its acceptance state.

## Owner

Codex log keeper.

## When to update

Update at goal creation, checkpoint changes, PR creation, review updates, GPT Pro updates, and goal close.

## Required fields

- Goal ID
- Stage
- Title
- Prompt text
- Status
- Branch/worktree
- Started at
- Updated at
- Done-when
- Current checkpoint
- Skills used
- Subagents used
- PR URL
- Codex review status
- GPT Pro status
- Next stage source

## Example format

`G-0000 | Stage 00 | active | branch blocked | GPT Pro blocked`

## Current state

| Goal ID | Stage | Title | Prompt text | Status | Branch/worktree | Started at | Updated at | Done-when | Current checkpoint | Skills used | Subagents used | PR URL | Codex review status | GPT Pro status | Next stage source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G-0000 | 00 | Establish control system and capability audit | Implement approved Stage 00 governance plan only | PASS / COMPLETE | `stage/00-control-system` merged; follow-up evidence branches merged/open as recorded | 2026-05-24T02:37:02-05:00 | 2026-05-24T09:45:25-05:00 | Governance files exist; audit complete; GitHub PR or blocker; GPT Pro PASS or blocker; phase gate result recorded | Stage 00 complete: PRs #1-#4, CI, Codex reviews, GPT Pro final confirmation, logs, prompt-by-prompt confirmation, and acceptance evidence saved | codex-log-keeper, ai-capability-radar, phase-gate-auditor, gpt-pro-review-preparer, github-stage-deployer, browser-gpt-pro-reviewer, acceptance-evidence-collector, stage-next-goal-synthesizer, github-review-resolver | Hypatia and Fermat completed read-only audits; final confirmation used bounded local verification only | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/2; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/3; https://github.com/xiaoming2cf-afk/FinSignalHub/pull/4 | PASS: latest PR #4 Codex response found no major issues | PASS: final GPT Pro confirmation and post-acceptance capability confirmation saved | GPT Pro authorized Stage 01 planning; do not implement Stage 01 before approved Stage 01 plan and goal |
| G-0001 | 00.1 | RunLog governance cleanup | Implement approved RunLog-driven Stage 00.1 governance cleanup only | PASS / COMPLETE / MERGED | `stage/00-1-governance-cleanup` merged to `main` | 2026-05-24T11:41:00-05:00 | 2026-05-26T12:08:26-05:00 | RunLog files exist; helper scripts exist; PR and Codex review complete; GPT Pro PASS saved; phase gate result recorded; PR merged | PR #6 merged at `75f215bc8647dac9c5e4e55b68b3b84100f064b4`; CI passed; final Codex no-major response saved at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6#issuecomment-4529839137 | finsignal-product-governor, phase-gate-auditor, codex-log-keeper, github-stage-deployer, gpt-pro-review-preparer, browser-gpt-pro-reviewer, github-review-resolver, acceptance-evidence-collector, stage-next-goal-synthesizer | Lorentz and Newton read-only verification completed | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/6 | PASS: no major issues on merged PR head | PASS: Stage 00.1 accepted; Stage 01 planning only | Stage 00.1 GPT Pro PASS response |
| G-0002 | 01 | Stage 01 repo scaffold planning and implementation | Create Stage 01 plan and scaffold-only implementation after gates pass | PASS / ACCEPTED / MERGED | `stage/01-repo-scaffold` merged to `main` | 2026-05-24T15:15:16-05:00 | 2026-05-26T15:57:58-05:00 | Stage 01 plan exists; GPT Pro plan PASS saved; known Codex plan findings through CR-01-040 addressed; GPT Pro Docker ordering and implementation gate CONDITIONAL PASS saved; Docker environment and compose config passed; scaffold-only implementation exists; implementation head `f30a02e7fd891d578e0f6e54f858ed475a6d6881` has CI PASS and Codex no-major; GPT Pro final implementation review returned PASS; final evidence commit `ce9bd7c008e1ec5c4b9a6cec9b1488883fe20742` passed CI/Codex, tag `stage-01-repo-scaffold` was pushed, and PR #7 merged at `6b71850a1a59603fe169cd5a5ddf8d40adfaf8f4` | Stage 01 closed; next valid action is Stage 02 planning only, not implementation | finsignal-product-governor, subagent-coordinator, phase-gate-auditor, codex-log-keeper, gpt-pro-review-preparer, browser-gpt-pro-reviewer, ai-capability-radar, github-review-resolver, acceptance-evidence-collector, github-stage-deployer, stage-next-goal-synthesizer | product-scope-audit, runtime-ci-audit, docs-log-audit; read-only GPT final evidence verifier | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7 | PASS: final evidence head Codex no-major at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7#issuecomment-4548674092 | PASS: Stage 01 final implementation review saved at `reviews/stage_01/GPT_PRO_REVIEW_RESPONSE.md`; Stage 02 planning only authorized | GPT Pro Stage 01 final review response |
| G-0003 | 02 | Stage 02 Research Mode domain models planning | Draft Stage 02 plan only; do not implement models, migrations, CRUD, connectors, MCP tools, extraction, or UI behavior until all plan gates pass | PASS / superseded by G-0004 implementation goal | `stage/02-domain-models` | 2026-05-26T15:57:58-05:00 | 2026-05-29T11:20:00-05:00 | Stage 02 plan, tasks, checklist, PR body, review packet, deployment evidence, Codex history, GPT Pro plan PASS, and current-head CI/Codex no-major evidence exist | PR #8 head `8800022f55d79db951b57a61a1d1c7b3301cea9d` has CI PASS and Codex no-major at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4576703382; GPT Pro plan PASS saved; user later approved direct execution without repeated confirmation | finsignal-product-governor, evidence-graph-architect, phase-gate-auditor, codex-log-keeper, gpt-pro-review-preparer, browser-gpt-pro-reviewer, github-stage-deployer, github-review-resolver, subagent-coordinator, acceptance-evidence-collector, stage-next-goal-synthesizer | Archimedes, Volta, Linnaeus, Meitner completed read-only planning/gate audits | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8 | PASS for planning head `8800022`; implementation head still pending | PASS for plan; Stage 03 not authorized | GPT Pro Stage 02 plan review response |
| G-0004 | 02 | Stage 02 Research Mode domain models implementation | Implement approved Research Mode domain models, migrations, schemas, CRUD primitives, tests, docs, logs, and final review artifacts only; do not implement connectors, extraction, claim graph computation, research delta engines, MCP business tools, product UI behavior, reports, stock tools, investment advice, or generic RAG | active / Codex remediation in progress | `stage/02-domain-models` | 2026-05-29T11:20:00-05:00 | 2026-05-29T15:10:00-05:00 | Approved models, Alembic migration, schemas, CRUD services/routes, tests, docs/logs exist; local checks pass; implementation head pushed to PR #8; CI passes; Codex no-major; GPT Pro final implementation review PASS; GPT Pro assigns Stage 03 | Codex returned CR-02-020 through CR-02-036 across implementation heads. Code remediation through CR-02-033 is pushed and CI-passed; documentation remediation through CR-02-035 is pushed and CI-passed on head `0d46aa12cce60533cc0c6bb35d58af0c01b716b1`; CR-02-036 is a documentation-only Gate 6 CI evidence refresh now tracked as the active branch-head remediation awaiting latest-head CI and current-head Codex no-major before GPT Pro final review. | finsignal-product-governor, evidence-graph-architect, phase-gate-auditor, codex-log-keeper, gpt-pro-review-preparer, browser-gpt-pro-reviewer, github-stage-deployer, github-review-resolver, subagent-coordinator, acceptance-evidence-collector | schema-agent, migration-agent, api-schema-agent, test-agent, docs-log-agent; plus read-only stale gate auditors, Mendel, Hegel, and Pauli read-only remediation audits | https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8 | CR-02-036 branch-head remediation needs latest-head CI/Codex follow-up | pending final implementation review; plan PASS already saved | GPT Pro Stage 02 plan review response plus user direct-execution approval |
