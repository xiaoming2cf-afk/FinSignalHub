# Stage 05 Plan: Claim Graph and Research Delta Planning

## Context Read

Required context for this plan:

- `AGENTS.md`
- `PLANS.md`
- `CONTROL/01_PRODUCT_DEFINITION.md`
- `CONTROL/02_STAGE_ROADMAP.md`
- `CONTROL/03_PHASE_ACCEPTANCE.md`
- `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`
- `CONTROL/21_SUBAGENT_PROTOCOL.md`
- `CONTROL/24_CURRENT_STAGE_STATE.md`
- `RUNLOG/LONG_RUN_SUMMARY.md`
- `reviews/stage_04/STAGE_ACCEPTANCE_RESULT.md`
- `reviews/stage_04/GPT_PRO_LIVE_HEAD_CLOSEOUT_RESPONSE.md`

Stage 04 is merged and tagged as `stage-04-evidence-extraction`. GPT Pro authorized Stage 05 planning only. This plan does not create Claim Graph runtime code, Research Delta runtime code, database migrations, MCP business tools, Repro Pack logic, UI/dashboard behavior, chatbot/RAG behavior, stock prediction, investment advice, Risk Mode, Replay Engine behavior, live external calls, or real LLM calls.

## Capability Check

- Local shell, Python, Node.js, Git, GitHub CLI, GitHub Actions, and Codex review are available based on prior stage evidence.
- Chrome/GPT Pro review is available only through the approved logged-in Chrome route. Stop on login, captcha, payment, permission, secret, or unclear consent prompts.
- Computer Use or foreground visual recovery may be used only when safely available and without entering secrets. If no safe browser route works, record a GPT Pro blocker instead of downgrading the gate.
- Docker is not required for Stage 05 planning. Any future implementation must recheck Docker only if runtime or integration checks require it.

## Product Alignment Check

Stage 05 planning maps directly to the evidence-stream product identity:

- `ResearchClaim` nodes represent research judgments, not chat answers or investment recommendations.
- `ClaimEvidenceEdge` planning connects claims to provenance-preserving Stage 04 evidence candidates.
- `ResearchDelta` planning compares research state between baseline and current evidence snapshots, not price movement, risk scoring, or trading signals.
- Literature matrix, method card, dataset card, and future Repro Pack readiness depend on explicit relation rationale, provenance, and tool-call lineage.

Product alignment verdict for this planning work: PASS if it remains plan-only and evidence-stream oriented.

## Scope

Stage 05 planning scope:

- Define future Claim Graph architecture boundaries around `ResearchProject`, `ResearchClaim`, Stage 04 evidence candidates, and future `ClaimEvidenceEdge` records.
- Define relation type planning around the Stage 02 accepted `EdgeRelationType` values: `supports`, `contradicts`, `qualifies`, and `background`, without implementing graph persistence or traversal.
- Preserve the Stage 02 accepted `EdgeRelationType` values; limitation-style semantics must map to `qualifies` plus rationale, and method, dataset, uncertainty, or supersession semantics must remain rationale/metadata/card-reference annotations unless a later GPT Pro-approved migration explicitly adds compatible relation values.
- Define relation rationale and provenance requirements for every future edge.
- Define same-project boundary guards so claims and evidence cannot be linked across projects.
- Define Research Delta semantics for baseline/current snapshots, changed claims, added evidence, removed evidence, relation-state changes, and confidence/rationale changes.
- Define mock-only tests and forbidden-scope scans for a later implementation goal.
- Define bounded subagent responsibilities and file ownership for a later implementation goal.
- Prepare GitHub/Codex/GPT Pro plan gate materials.

Stage 05 implementation remains blocked until this plan passes GitHub/Codex and GPT Pro plan review and a later approved `/goal` exists.

## Files To Create Or Modify

Planning files allowed now:

- `PLANS/STAGE_05_PLAN.md`
- `TASKS/STAGE_05_TASKS.md`
- `CHECKLISTS/STAGE_05_CHECKLIST.md`
- `reviews/stage_05/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_05/CODEX_REVIEW_SUMMARY.md`
- `reviews/stage_05/PR_BODY.md`
- `reviews/stage_05/STAGE_ACCEPTANCE_RESULT.md`
- `reviews/stage_05/SUBAGENT_SUMMARY.md`
- `reviews/stage_05/README.md`
- `deployments/stage_05/GITHUB_PR.md`
- `deployments/stage_05/README.md`
- `docs/architecture/stage_05_claim_graph_research_delta.md`
- `docs/codex/stage_05_commands.md`
- `logs/subagents/stage_05/README.md`
- `logs/subagents/stage_05/*.md`
- Stage 04 terminal handoff evidence under `reviews/stage_04/`
- Required `CONTROL/`, `RUNLOG/`, and `CHANGELOG.md` updates.

Future Stage 05 implementation files may be planned but must not be created during planning:

- `apps/api/finsignalhub_api/claim_graph/`
- `apps/api/finsignalhub_api/claim_graph/schemas.py`
- `apps/api/finsignalhub_api/claim_graph/relations.py`
- `apps/api/finsignalhub_api/claim_graph/service.py`
- `apps/api/finsignalhub_api/claim_graph/validators.py`
- `apps/api/finsignalhub_api/research_delta/`
- `apps/api/finsignalhub_api/research_delta/schemas.py`
- `apps/api/finsignalhub_api/research_delta/service.py`
- `apps/api/finsignalhub_api/research_delta/rules.py`
- `apps/api/tests/test_stage05_claim_graph.py`
- `apps/api/tests/test_stage05_research_delta.py`
- `apps/api/tests/fixtures/stage05_claim_graph/`

## Files Not To Touch

Do not modify Stage 02 migrations or domain models, Stage 03 connector runtime, Stage 04 extraction runtime behavior, MCP business tools, Repro Pack export logic, admin UI product behavior, auth, billing, provider clients, external LLM integrations, or deployment runtime behavior during Stage 05 planning.

## Skills

Use:

- `finsignal-product-governor`
- `evidence-graph-architect`
- `phase-gate-auditor`
- `codex-log-keeper`
- `github-stage-deployer`
- `github-review-resolver`
- `gpt-pro-review-preparer`
- `browser-gpt-pro-reviewer`
- `subagent-coordinator`
- `acceptance-evidence-collector`
- `stage-next-goal-synthesizer`

## Subagents

Declare these bounded Stage 05 planning subagents:

- `claim-graph-architecture-agent`: Claim Graph shape, future modules, and non-persistence boundaries.
- `relation-rule-agent`: relation enum, rationale, provenance, and forbidden relation states.
- `research-delta-agent`: baseline/current snapshot semantics and delta payload boundaries.
- `project-boundary-validator-agent`: same-project guards and cross-project rejection plan.
- `test-plan-agent`: mock-only future tests, forbidden-scope scan, and CI checks.
- `docs-log-agent`: architecture docs, command docs, review artifacts, and log evidence.
- `scope-review-agent`: product drift scan and forbidden Stage 06+ behavior scan.

Each subagent writes `logs/subagents/stage_05/<agent_name>.md`, must not edit files outside its declared boundary, and must not create implementation files during planning.

## Implementation Steps

Planning steps:

1. Save terminal Stage 04 GPT Pro live-head closeout PASS and Stage 05 planning-only instruction as handoff evidence on the Stage 05 branch.
2. Create Stage 05 plan, tasks, checklist, review packet, PR body, acceptance placeholder, deployment placeholder, architecture doc, command doc, review/deployment READMEs, and subagent logs.
3. Update control logs, artifact registry, dashboard, current stage state, action queue, blocker log, goal registry, checkpoint log, RunLog, and changelog.
4. Run planning-only checks: phase check, forbidden implementation path absence checks, forbidden-scope scan, secret scan, and `git diff --check`.
5. Commit, push, open PR, request `@codex review`, wait for CI, and resolve critical findings.
6. Submit the Stage 05 plan packet to GPT Pro through the specified Chrome/GPT Pro page.

Later implementation steps must be written only after GPT Pro plan PASS and a new approved `/goal`.

## Tests

### Local checks

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 05`
- `Test-Path apps/api/finsignalhub_api/claim_graph` must be false during planning.
- `Test-Path apps/api/finsignalhub_api/research_delta` must be false during planning.
- `Test-Path apps/api/tests/test_stage05_claim_graph.py` must be false during planning.
- `Test-Path apps/api/tests/test_stage05_research_delta.py` must be false during planning.
- `Test-Path apps/api/tests/fixtures/stage05_claim_graph` must be false during planning.
- High-confidence secret scan must find no real secrets in Stage 05 planning files.
- Forbidden-scope scan must find no Stage 05 runtime implementation, MCP business tools, Repro Pack export logic, UI/dashboard behavior, chatbot/RAG behavior, stock prediction, investment advice, Risk Mode, Replay Engine, live provider calls, or real LLM calls.
- `git diff --check`

### Unit tests

No Stage 05 unit tests are run during planning because Claim Graph and Research Delta implementation is not authorized. A later implementation goal must add mock-only unit tests for same-project relation creation, cross-project rejection, relation enum validation, rationale/provenance requirements, neighborhood output, baseline/current delta semantics, changed-claims delta, no-report-generation wording, and fixture-only behavior.

### Integration tests

No Stage 05 integration tests are run during planning. A later implementation goal must keep default checks fixture-based and must not require live external APIs, real LLM providers, credentials, paid services, network calls, or production data.

### Acceptance checks

Planning acceptance requires Stage 05 plan, tasks, checklist, GPT Pro review packet, PR body, deployment placeholder, architecture note, command note, subagent logs, control logs, GitHub PR, Codex review, CI PASS, and GPT Pro plan review before implementation may begin.

Future implementation tests to plan:

- same-project relation creation tests
- cross-project relation rejection tests
- relation enum validation tests
- `qualifies` compatibility tests for limitation-style evidence
- rejection or metadata-mapping tests for method, dataset, uncertainty, and supersession semantics when no enum migration exists
- relation rationale required tests
- relation provenance required tests
- claim graph neighborhood output tests
- Research Delta baseline/current time tests
- changed-claims delta tests
- no-report-generation tests
- mock-only fixture tests
- forbidden-scope scan
- secret scan
- `phase_check.py --stage 05`
- `python -m compileall apps/api/finsignalhub_api`
- `git diff --check`

## Docs

Docs must define Claim Graph and Research Delta planning boundaries, future module ownership, relation type intent, rationale and provenance requirements, same-project guards, delta baseline/current semantics, deferred implementation paths, mock-only tests, forbidden-scope scans, and stop conditions.

## GitHub Deployment

Use branch `stage/05-claim-graph-delta`.

PR title: `Stage 05: Claim Graph and Research Delta Planning`.

PR body source: `reviews/stage_05/PR_BODY.md`.

After PR creation or after any pushed head that needs review, comment:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

Any pushed head must pass CI and current-head Codex before GPT Pro plan review.

## GPT Pro Review

Submit `reviews/stage_05/GPT_PRO_REVIEW_PACKET.md` to the specified GPT Pro page. GPT Pro must answer PASS, CONDITIONAL PASS, or FAIL for planning. Stage 05 implementation cannot begin until GPT Pro plan review passes and a separate `/goal` exists.

## Risks

- Claim Graph drifts into a graph analytics engine.
- Research Delta drifts into report generation.
- Delta computation drifts into risk scoring, trading signals, prediction, or investment advice.
- Claim/evidence relations are treated as verified truth without provenance.
- The plan replaces existing `qualifies` relation values with a new `limits` value without compatibility or migration rules.
- The plan treats method, dataset, uncertainty, or supersession semantics as persisted relation types before a GPT Pro-approved enum migration exists.
- Cross-project evidence leakage.
- Relation rationale becomes optional or generic metadata.
- Stage 04 candidate semantics are mutated instead of consumed.
- MCP business tools, UI/dashboard behavior, or Repro Pack export appear too early.

## Stop Conditions

Stop if:

- Planning requires real API keys, LLM provider credentials, paid services, live network calls, or private documents.
- Work requires Stage 05 runtime implementation before GPT Pro plan PASS and a later approved `/goal`.
- Work requires MCP business tools, Repro Pack export, UI/dashboard behavior, chatbot/RAG behavior, stock prediction, investment advice, Risk Mode, Replay Engine, auth, or billing.
- Same-project evidence boundaries cannot be defined without destructive Stage 02, Stage 03, or Stage 04 changes.
- A requested feature cannot map to research evidence-stream value.
- Browser/GPT Pro review encounters login, captcha, payment, secret, permission, privacy, or unclear consent prompts.
