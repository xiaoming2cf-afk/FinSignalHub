# Stage 04 Plan: Evidence Extraction Skeleton

## Context Read

Required context for this plan:

- `AGENTS.md`
- `PLANS.md`
- `CONTROL/01_PRODUCT_DEFINITION.md`
- `CONTROL/02_STAGE_ROADMAP.md`
- `CONTROL/03_PHASE_ACCEPTANCE.md`
- `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`
- `CONTROL/21_SUBAGENT_PROTOCOL.md`
- `RUNLOG/LONG_RUN_SUMMARY.md`
- `reviews/stage_03/STAGE_ACCEPTANCE_RESULT.md`
- `reviews/stage_03/GPT_PRO_CR_03_043_REREVIEW_RESPONSE.md`

Stage 03 is merged and tagged. GPT Pro authorized Stage 04 planning only. This plan does not create extraction implementation code, extraction tests, extraction fixtures, external LLM calls, claim graph logic, Research Delta logic, Repro Pack logic, MCP business tools, UI behavior, or live network behavior.

## Capability Check

- Local shell, Python, Node.js, Docker, GitHub CLI, GitHub connector, GitHub Actions, and Codex review are available based on prior stage evidence.
- Chrome extension is the preferred route for GPT Pro page review. Standalone background Computer Use is still a capability limitation and must not be treated as available unless a real tool surface is exposed.
- Network access may exist, but Stage 04 planning and later default tests must be mock-only and must not require API keys, external LLM providers, or live source calls.

## Product Alignment Check

Stage 04 must preserve FinSignalHub as Research Mode-first, MCP-first, and evidence-stream oriented.

The Stage 04 plan exists to prepare a bounded evidence extraction skeleton that can later convert Stage 03 normalized documents into future `EvidenceItem` candidates with quote-span provenance, relation classification, extraction confidence, and replayable tool-call lineage. It must not produce chat answers, generic summaries, reports, investment advice, stock predictions, dashboards, model rankings, Risk Mode, or Replay Engine behavior.

## Scope

Stage 04 planning scope:

- Define future extraction schemas for evidence candidates, quote spans, no-quote rationales, relation labels, confidence fields, and provenance validation.
- Define relation type enum boundaries for method, dataset, observation, limitation, background, and claim-supporting evidence without implementing claim graph computation.
- Define quote-span validation and no-quote rationale validation against normalized document references.
- Define a mock LLM extraction adapter plan that is deterministic, fixture-based, and disabled from real external calls in CI.
- Define an extraction worker skeleton plan that references future paths only; no extraction package or test implementation is created in this planning stage.
- Define mock-only tests, no-network checks, forbidden-scope checks, subagent boundaries, GitHub deployment, Codex review, GPT Pro plan review, risks, and stop conditions.

Stage 04 implementation remains blocked until this plan passes GitHub/Codex and GPT Pro plan review and a later approved `/goal` exists.

## Files To Create Or Modify

Planning files allowed now:

- `PLANS/STAGE_04_PLAN.md`
- `TASKS/STAGE_04_TASKS.md`
- `CHECKLISTS/STAGE_04_CHECKLIST.md`
- `reviews/stage_04/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_04/PR_BODY.md`
- `reviews/stage_04/STAGE_ACCEPTANCE_RESULT.md`
- `reviews/stage_04/CODEX_REVIEW_SUMMARY.md`
- `reviews/stage_04/SUBAGENT_SUMMARY.md`
- `deployments/stage_04/GITHUB_PR.md`
- `docs/architecture/stage_04_evidence_extraction.md`
- `docs/codex/stage_04_commands.md`
- `logs/subagents/stage_04/README.md`
- Required `CONTROL/`, `RUNLOG/`, and PR evidence records.

Future implementation paths may be referenced but must not be created during planning:

- `apps/api/finsignalhub_api/extraction/`
- `apps/api/tests/test_stage04_extraction.py`
- `apps/api/tests/fixtures/stage04_extraction/`

## Files Not To Touch

Do not modify connector behavior, Stage 02 migrations, Stage 02 domain models, MCP business tools, claim graph logic, research delta logic, Repro Pack logic, admin UI product behavior, auth, billing, or frontend behavior during Stage 04 planning.

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

Declare these bounded subagents for a later implementation goal:

- `extraction-schema-agent`: future extraction schema and enum definitions only.
- `llm-adapter-agent`: future mock LLM adapter contract only; no external calls.
- `provenance-agent`: quote-span, source identity, retrieval time, and tool-call lineage validation plan.
- `dedup-agent`: future duplicate evidence candidate handling plan only.
- `test-agent`: mock-only extraction test plan.
- `docs-agent`: method, dataset, limitation, and provenance documentation plan.

Each subagent must write `logs/subagents/stage_04/<agent_name>.md`, must not modify files outside the approved implementation goal, and must not create Stage 04 implementation files during planning.

## Implementation Steps

Planning steps:

1. Create Stage 04 plan, tasks, checklist, review packet, PR body, acceptance placeholder, deployment placeholder, architecture doc, command doc, and subagent log README.
2. Update control logs and RunLog to show Stage 03 merged/tagged and Stage 04 planning active.
3. Run planning-only checks: phase check, no extraction implementation path check, no Stage 04 test/fixture path check, forbidden-scope scan, secret scan, and `git diff --check`.
4. Commit, push, open PR, request `@codex review`, wait for CI, and resolve critical findings.
5. Submit the Stage 04 plan packet to GPT Pro through the specified Chrome/GPT Pro page.

Later implementation steps must be written only after GPT Pro plan PASS and a new approved `/goal`.

## Tests

### Local checks

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04`
- `Test-Path apps/api/finsignalhub_api/extraction` must be false during planning.
- `Test-Path apps/api/tests/test_stage04_extraction.py` must be false during planning.
- `Test-Path apps/api/tests/fixtures/stage04_extraction` must be false during planning.
- High-confidence secret scan must find no real secrets.
- Forbidden-scope scan must find no Stage 04 implementation package, external LLM calls, claim graph logic, Research Delta logic, MCP business tools, UI/dashboard behavior, chatbot/RAG, stock prediction, investment advice, Risk Mode, or Replay Engine behavior.
- `git diff --check`

### Unit tests

No Stage 04 unit tests are run during planning because extraction implementation is not authorized. The later implementation goal must add mock-only unit tests before any functionality gate can pass.

### Integration tests

No Stage 04 integration tests are run during planning. A later implementation goal must keep default extraction integration tests fixture-based and must not require live external APIs, real LLM providers, credentials, network calls, or paid services.

### Acceptance checks

Planning acceptance requires Stage 04 plan, tasks, checklist, GPT Pro review packet, PR body, deployment placeholder, architecture note, command note, subagent README, logs, GitHub PR, Codex review, and GPT Pro plan review to exist before implementation may begin.

Future implementation tests to plan:

- Mock extraction adapter returns deterministic candidates.
- Quote spans validate against document text fixtures.
- No-quote rationale is required when a candidate has no exact quote.
- Relation labels are limited to approved enum values.
- Provenance includes source identity, document ref, retrieval time, quote span, transformation notes, confidence, and tool-call lineage.
- Extraction errors use deterministic error shapes.
- No external LLM or network calls occur in default tests.
- Forbidden Stage 05+ claim graph and Research Delta behavior stays absent.

## Docs

Docs must define extraction boundaries, schema intent, relation labels, quote-span validation, no-quote rationale rules, provenance fields, mock LLM adapter constraints, worker skeleton boundaries, deferred implementation paths, and stop conditions.

## GitHub Deployment

Use branch `stage/04-evidence-extraction`.

PR title: `Stage 04: Evidence Extraction Planning`.

PR body source: `reviews/stage_04/PR_BODY.md`.

After PR creation or after any pushed head that needs review, comment:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

Any pushed head must pass CI and current-head Codex before GPT Pro plan review.

## GPT Pro Review

Submit `reviews/stage_04/GPT_PRO_REVIEW_PACKET.md` to the specified GPT Pro page. GPT Pro must answer PASS, CONDITIONAL PASS, or FAIL for planning. Stage 04 implementation cannot begin until GPT Pro plan review passes and a separate `/goal` exists.

## Risks

- Evidence extraction drifts into generic summarization or chat answers.
- Relation classification becomes claim graph computation too early.
- Mock LLM adapter becomes a real provider call or requires API keys.
- Quote-span validation is weakened and candidates cannot be replayed.
- Extraction candidates omit source identity, retrieval time, transformation notes, confidence, or tool-call lineage.
- Stage 04 starts creating implementation paths before GPT Pro plan acceptance.

## Stop Conditions

Stop if:

- Planning would require real API keys, LLM provider credentials, paid services, live network calls, or private documents.
- Work requires claim graph computation, Research Delta computation, Repro Pack export, MCP business tools, UI/dashboard behavior, chatbot/RAG behavior, stock prediction, investment advice, Risk Mode, or Replay Engine behavior.
- Quote-span or provenance requirements cannot be defined without changing Stage 02 or Stage 03 persisted schema behavior.
- A requested extraction feature cannot map to research evidence-stream value.
- Browser/GPT Pro review encounters login, captcha, payment, secret, permission, privacy, or unclear consent prompts.
