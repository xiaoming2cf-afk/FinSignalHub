# GPT Pro Review Packet: Stage 05 Claim Graph and Research Delta Planning

Please review FinSignalHub Stage 05 planning only.

## Project Identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. It helps AI Agents call structured evidence workflows for researchers and later financial research users. The core outputs are research delta, claim graph, evidence card, literature matrix, method card, dataset card, repro pack, and tool-call log.

Forbidden directions remain: chatbot, generic RAG, stock recommendation, investment advice, trading signal, ordinary report generator, standalone dashboard, model leaderboard, Risk Mode, and Replay Engine.

## Stage Goal

Stage 05 planning defines the future Claim Graph and Research Delta implementation boundaries connecting Stage 02 research objects and Stage 04 evidence candidates. It does not implement runtime Claim Graph, Research Delta, database migrations, MCP tools, Repro Pack export, UI/dashboard behavior, or provider integrations.

## Approved Scope

Allowed planning files:

- `PLANS/STAGE_05_PLAN.md`
- `TASKS/STAGE_05_TASKS.md`
- `CHECKLISTS/STAGE_05_CHECKLIST.md`
- `reviews/stage_05/`
- `deployments/stage_05/`
- `docs/architecture/stage_05_claim_graph_research_delta.md`
- `docs/codex/stage_05_commands.md`
- `logs/subagents/stage_05/`
- required `CONTROL/`, `RUNLOG/`, and `CHANGELOG.md` updates

Future implementation paths are referenced but not created:

- `apps/api/finsignalhub_api/claim_graph/`
- `apps/api/finsignalhub_api/research_delta/`
- `apps/api/tests/test_stage05_claim_graph.py`
- `apps/api/tests/test_stage05_research_delta.py`
- `apps/api/tests/fixtures/stage05_claim_graph/`

## Actual Work In This Branch

This branch records Stage 04 terminal closeout evidence, updates governance state to Stage 05 planning active, and creates Stage 05 plan, task, checklist, architecture, command, subagent, PR, deployment, and acceptance review artifacts.

## Planned Checks

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 05`
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 05 --final`
- `python -m compileall apps/api/finsignalhub_api`
- absence checks for Stage 05 runtime package, tests, and fixtures
- high-confidence secret scan
- forbidden-scope scan
- artifact, blocker, and checkpoint row-ID uniqueness checks
- `git diff --check`
- GitHub CI PASS
- current-head Codex no-major
- unresolved review threads = 0

## GitHub And Codex Status

Stage 05 PR #12 exists:

`https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12`

The PR body source is `reviews/stage_05/PR_BODY.md`.

Current GitHub gate state:

Gate 6 is evaluated from live PR #12 evidence at the time this packet is submitted, not from fixed historical commit or CR pointers in this file. Before GPT Pro review, attach the current PR head, current CI results, latest current-head Codex result, and unresolved non-outdated review-thread count.

Required live Gate 6 evidence:

- live PR #12 head OID
- all required CI jobs PASS for that head
- current-head Codex no-major or accepted follow-up for that head
- unresolved non-outdated review threads = 0

GPT Pro submission note: Chrome opened the target page at 2026-06-07T02:02:53-05:00, but the visible page showed a Pro subscription renewal/payment-related prompt. Codex stopped before packet submission. This packet must not be submitted as PASS-ready until live Gate 6 evidence is clean and the payment/renewal prompt is resolved.

Codex review requests used:

- Required full request: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641449668`
- Current-head minimal request after CR-05-001/002 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641495922`
- Current-head minimal request after CR-05-003 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641518560`
- Current-head minimal request after CR-05-004 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641539890`
- Current-head minimal request after CR-05-005 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641564414`
- Current-head minimal request after CR-05-006/007 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641588136`
- Current-head minimal request after CR-05-008 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641612833`
- Current-head full request after CR-05-009 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641664788`
- Current-head minimal request after CR-05-010 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641700224`
- Current-head Codex no-major after CR-05-010 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641706376`
- Current-head request after blocker-evidence commit: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641788055`
- CR-05-011 current blocker: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#discussion_r3368936274`
- Current-head requests after CR-05-011 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641841690` and `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641864183`
- CR-05-012 current blocker: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#discussion_r3368965518`
- Current-head request after CR-05-012 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641909138`
- CR-05-013/014 resolved/superseded blockers: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#discussion_r3368995592` and `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#discussion_r3368995595`
- CR-05-015/016 resolved/superseded blockers: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#discussion_r3369069324` and `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#discussion_r3369069325`
- CR-05-017 resolved/superseded blocker: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#discussion_r3369090776`
- CR-05-018 resolved/superseded blocker: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#discussion_r3369112819`
- CR-05-019 historical blocker: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#discussion_r3369143699`

Required Codex prompt:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

Known Codex findings before this packet refresh:

- CR-05-001: command doc omitted required gate checks. Local remediation added the missing commands.
- CR-05-002: current-stage state still said PR pending creation. Local remediation now points to PR #12.
- CR-05-003: GPT Pro packet still said PR pending creation. Local remediation refreshed the packet.
- CR-05-004: Codex review summary still recorded a stale `aaf3e53...` pre-sync head. This summary refresh remediates it.
- CR-05-005: current-state route still told a clean checked head to rerun checks and create another commit. This route refresh remediates it.
- CR-05-006/007: acceptance next-stage source and PR body gate evidence were stale. This acceptance-source refresh remediates them.
- CR-05-008: Codex summary had conflicting reviewed-head references. Local remediation fixed it.
- CR-05-009: Stage 05 relation plan could drop existing `qualifies` relation. Local remediation preserved `qualifies`.
- CR-05-010: Method, dataset, uncertainty, and supersession semantics still looked like persisted relation types. Remediated for PR head `387b5c0816d7acbb388dca4a705734fd7d8623c2` by gating all non-enum semantics behind rationale, metadata, card-reference annotations, or a future GPT Pro-approved enum migration.
- CR-05-011: The blocker-evidence commit reset Gate 6, but deployment evidence still named the older `387b5c0...` head as current. Remediated in reviewed head `b5c0ccc1954ed452667f80570c63c68bf7aabdef`; superseded by CR-05-012.
- CR-05-012: The payment-prompt blocker cited a screenshot that was ignored by `.gitignore`; superseded by CR-05-013 because unredacted screenshots must not be committed.
- CR-05-013/014: The tracked screenshot exposed private browser context, and Gate 6 records still described the previous missing-screenshot blocker. Amended head `04e328d4d39a8b1826f10c9d507f8fdbf9277eeb` removed the screenshot from tracking/history and used textual blocker evidence, but Codex then advanced the gate to CR-05-015/016.
- CR-05-015/016: B-0107 through B-0115 were closed as historical, B-0120 was superseded, and `CHECKLISTS/STAGE_05_CHECKLIST.md` was pointed to the B-0121 route. These are now historical, not the active Gate 6 pointer.
- CR-05-017: Remediated historical wording blocker; superseded by CR-05-018 after the next Codex review.
- CR-05-018: Remediated acceptance-result live-head blocker; superseded by CR-05-019 after the next Codex review.
- CR-05-019: Historical current-state blocker. The accepted route is now live-head based: when local HEAD already equals PR head, do not create a status commit; verify live CI, current-head Codex, and unresolved non-outdated review threads directly.

## Stage 05 Planning Questions For GPT Pro

Please answer explicitly:

1. Does Stage 05 planning preserve the Research Mode-first, MCP-first, evidence-stream product identity?
2. Are the planned Claim Graph relation boundaries sufficient and not over-scoped?
3. Are relation rationale, provenance, and same-project boundary requirements strong enough?
4. Are Research Delta baseline/current semantics scoped correctly and not drifting into reports, risk scoring, prediction, or investment advice?
5. Are forbidden implementation paths and Stage 06+ boundaries clear enough?
6. What must be fixed before Stage 05 planning can pass?
7. What can be deferred to the Stage 05 implementation goal?
8. May Stage 05 planning be marked PASS, CONDITIONAL PASS, or FAIL?
9. If PASS or accepted CONDITIONAL PASS, please provide the exact Stage 05 implementation `/goal` requirements, allowed files, tests, risks, and stop conditions.

## Required GPT Pro Verdict

Return one of:

- PASS
- CONDITIONAL PASS
- FAIL

If CONDITIONAL PASS, list critical items that must be fixed before implementation and deferred items that may wait.
