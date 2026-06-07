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

Most recent checked PR head before this summary refresh was `2b485e70615900969738bb3b6bf192470dbd43cf`; CI passed for that head and Codex opened CR-05-004 because the Codex summary still recorded `aaf3e53...` as the current pre-sync head. This summary refresh must create a newer head that passes CI, receives current-head Codex no-major, and has unresolved review threads = 0 before GPT Pro should treat GitHub Gate 6 as satisfied.

Codex review requests used:

- Required full request: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641449668`
- Current-head minimal request after CR-05-001/002 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641495922`
- Current-head minimal request after CR-05-003 remediation: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/12#issuecomment-4641518560`

Required Codex prompt:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

Known Codex findings before this packet refresh:

- CR-05-001: command doc omitted required gate checks. Local remediation added the missing commands.
- CR-05-002: current-stage state still said PR pending creation. Local remediation now points to PR #12.
- CR-05-003: GPT Pro packet still said PR pending creation. Local remediation refreshed the packet.
- CR-05-004: Codex review summary still recorded a stale `aaf3e53...` pre-sync head. This summary refresh remediates it.

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
