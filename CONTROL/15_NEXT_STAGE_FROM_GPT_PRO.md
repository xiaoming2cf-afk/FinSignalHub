# 15 Next Stage From GPT Pro

## Purpose

Stores GPT Pro instructions for the next authorized work unit.

## Owner

Stage next-goal synthesizer.

## When to update

Update only after GPT Pro passes or conditionally passes a stage or plan gate and gives next-step instructions.

## Required fields

- Source stage
- GPT Pro result
- Next stage id
- Next stage goal
- Required files
- Acceptance criteria
- Risks
- Constraints
- Raw GPT Pro instruction

## Example format

`Source Stage 02 implementation gate | PASS | Next Stage 03 planning | source connectors planning only | raw instruction pasted below`

## Current state

Source stage: Stage 02 implementation final gate.

GPT Pro result: PASS.

Important condition: Stage 03 is authorized for planning only. Stage 03 implementation is not authorized.

## Next Stage ID

Stage 03 planning: Source Connectors.

## Next Stage Goal

Create `PLANS/STAGE_03_PLAN.md` for Research Mode source connector planning only.

The Stage 03 plan must define connector framework scope, file boundaries, subagents, normalized `Document` mapping, provenance fields, mocked test strategy, no-network test rule, CI checks, stop conditions, and a GPT Pro plan review packet.

## Allowed Planning Targets

- OpenAlex connector.
- Crossref connector.
- Semantic Scholar connector.
- arXiv connector.
- User upload connector.
- Connector base interface.
- Normalized `Document` output.
- Mocked tests.
- Docs.
- Logs.
- GPT Pro plan review packet.

## Required Stage 03 Planning Files

- `PLANS/STAGE_03_PLAN.md`
- `TASKS/STAGE_03_TASKS.md`
- `CHECKLISTS/STAGE_03_CHECKLIST.md`
- `reviews/stage_03/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_03/PR_BODY.md`
- `reviews/stage_03/STAGE_ACCEPTANCE_RESULT.md`
- `deployments/stage_03/GITHUB_PR.md`
- `docs/architecture/stage_03_source_connectors.md`
- `docs/codex/stage_03_commands.md`
- `logs/subagents/stage_03/`
- Required `CONTROL/` and `RUNLOG/` status updates.

## Required Subagents

Stage 03 plan should declare:

- `openalex-agent`
- `crossref-agent`
- `semantic-scholar-agent`
- `arxiv-agent`
- `user-upload-agent`
- `connector-review-agent`

Each subagent must have bounded file authority and must write logs under `logs/subagents/stage_03/`.

## Required Tests To Plan

- `pytest apps/api/tests/test_stage03_connectors.py`
- Mocked HTTP tests only.
- No external network calls in normal tests.
- Fixture-based OpenAlex sample response.
- Fixture-based Crossref sample response.
- Fixture-based Semantic Scholar sample response.
- Fixture-based arXiv sample response.
- User-upload sample fixture.
- Normalized `Document` schema validation.
- `publication_time` / `release_time` mapping tests.
- `source_identity` mapping tests.
- URL / DOI / external id mapping tests.
- Rate-limit and retry behavior tests with mocks.
- Forbidden-scope scan.
- Secret scan.
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03`
- `git diff --check`

CI must not require real API keys.

## Forbidden Scope

Do not implement in Stage 03 planning or implementation:

- Evidence extraction.
- LLM adapters.
- Claim graph computation.
- Research delta computation.
- Repro Pack export logic.
- MCP business tools.
- Risk Mode.
- Replay Engine.
- Stock prediction.
- Investment advice.
- Chatbot UI.
- Generic RAG.
- Dashboard behavior.

## Risks

- External API dependency creep.
- Connector work becoming ingestion or extraction workflow.
- Connector output bypassing provenance requirements.
- Stage 03 drifting into evidence extraction.
- User upload becoming a full document parser.

## Stop Conditions

Codex must stop and ask for user or GPT Pro guidance if:

1. A connector requires paid API keys or private credentials.
2. A source endpoint is inaccessible and no public fixture can be used.
3. Implementation requires real network tests.
4. Connector work requires evidence extraction.
5. Connector work requires an LLM adapter.
6. Connector work requires claim graph or research delta computation.
7. Connector work requires MCP business tool exposure.
8. Repository package layout requires destructive restructuring.
9. Stage 03 plan cannot preserve Stage 02 model boundaries.
10. External source terms create licensing ambiguity requiring user decision.

## Raw GPT Pro Instruction Source

Full final response is saved at:

- `reviews/stage_02/GPT_PRO_REVIEW_RESPONSE.md`
- `reviews/stage_02/GPT_PRO_FINAL_REVIEW_RESPONSE.md`

## Raw GPT Pro Instruction

```text
Stage 02 implementation result: PASS.
Stage 02 may be accepted now after saving this response/action items locally.
ADR-0002 support-file exception: acceptable.
Provenance modeling and validation: sufficient for Stage 02.
Forbidden Stage 03+ behavior: none indicated.
Live GitHub CI + Codex no-major evidence: sufficient despite committed historical pending wording.
Stage 03: planning only, not implementation.
Final verdict: PASS.

Begin Stage 03 planning only.
Do not implement Stage 03.
```

## Stage 03 Closeout Addendum From GPT Pro

Timestamp: 2026-05-30T13:45:00-05:00

Source files:

- `reviews/stage_03/GPT_PRO_CLOSEOUT_RESPONSE.md`
- `reviews/stage_03/GPT_PRO_CLOSEOUT_ACTION_ITEMS.md`

GPT Pro reviewed PR #10 closeout evidence and returned:

```text
Stage 03 planning closeout: PASS.
PR #10 may continue as the valid closeout PR.
Only Stage 03 implementation /goal artifacts may be drafted next.
Connector implementation is not authorized by this closeout review.
```

Next-stage instruction remains bounded to Stage 03 implementation `/goal` drafting only. The draft must include allowed files, forbidden files, mocked connector tests, no-network CI, provenance mapping, subagents, stop conditions, GitHub/Codex/GPT Pro final gates, and an explicit prohibition on connector code until the separate implementation `/goal` begins.

## Stage 03 Implementation Goal PASS From GPT Pro

Timestamp: 2026-05-30T15:51:25-05:00

Source files:

- `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md`
- `reviews/stage_03/GPT_PRO_IMPLEMENTATION_GOAL_ACTION_ITEMS.md`

GPT Pro reviewed the Stage 03 implementation `/goal` draft, PR #10 head `8f10f95c69c3eaf7d6ada7b878e017b917929e33`, CI PASS links, and Codex no-major evidence, then returned:

```text
VERDICT: PASS.
Begin Stage 03 implementation only under the accepted goal scope.
Implement connector primitives with mocked fixtures and normalized output only.
Run required local checks, CI, current-head Codex review, and final GPT Pro Stage 03 implementation review before accepting Stage 03.
```

Next instruction: after this evidence-sync update is saved and the resulting implementation branch head has live CI PASS plus current-head Codex no-major, start Stage 03 source connector implementation only for OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata. Outputs must normalize into existing Stage 02-compatible `SourceCreate`, `DocumentCreate`, and `ToolCallLog` payloads. Stage 04+ extraction, claim graph, delta, Repro Pack, MCP business tools, UI/dashboard behavior, chatbot/RAG, stock prediction, investment advice, Risk Mode, Replay Engine, auth, billing, live external API tests in CI, API keys, paid credentials, and full document parsing remain forbidden.

## Stage 03 Final Implementation PASS And Stage 04 Planning Instruction From GPT Pro

Timestamp: 2026-05-30T18:28:03-05:00

Source files:

- `reviews/stage_03/GPT_PRO_FINAL_REVIEW_RESPONSE.md`
- `reviews/stage_03/GPT_PRO_FINAL_ACTION_ITEMS.md`

GPT Pro reviewed PR #10, implementation remediation head `039e3d087c84f6ec61a6107b6f55b628d8a79ee6`, CI PASS links, current-head Codex no-major evidence, and CR-03-041 remediation, then returned:

```text
VERDICT: PASS.
Stage 03 final implementation: PASS.
Stage 03 may close after evidence closeout.
Next allowed action: Stage 04 planning only.
Stage 04 implementation is not authorized.
```

Stage 04 planning objective: plan evidence extraction skeleton only. The plan must define extraction schemas, relation type enums, quote-span validation, provenance validation, mock LLM extraction adapter, extraction worker skeleton, tests with mocks, and stop conditions. The plan may prepare the bridge from `Document` / connector-normalized metadata to future `EvidenceItem` candidates, but must not implement production extraction, external LLM calls, claim graph computation, Research Delta, Repro Pack, MCP business tools, Risk Mode, Replay Engine, chatbot/RAG/dashboard, stock prediction, investment advice, auth, billing, or live external network calls.

Allowed Stage 04 planning files: `PLANS/STAGE_04_PLAN.md`, `TASKS/STAGE_04_TASKS.md`, `CHECKLISTS/STAGE_04_CHECKLIST.md`, `reviews/stage_04/GPT_PRO_REVIEW_PACKET.md`, `reviews/stage_04/PR_BODY.md`, `reviews/stage_04/STAGE_ACCEPTANCE_RESULT.md`, `deployments/stage_04/GITHUB_PR.md`, `docs/architecture/stage_04_evidence_extraction.md`, `docs/codex/stage_04_commands.md`, `logs/subagents/stage_04/`, and required `CONTROL/` / `RUNLOG/` updates. Do not create `apps/api/finsignalhub_api/extraction/`, `apps/api/tests/test_stage04_extraction.py`, or `apps/api/tests/fixtures/stage04_extraction/` until Stage 04 implementation is separately approved.

## Stage 03 CR-03-042 Interlock

Timestamp: 2026-05-30T18:58:31-05:00

GPT Pro authorized Stage 04 planning only after Stage 03 evidence closeout, but PR #10 evidence-closeout head `bd33c4f1147c48dcf9573cee2c8546bbdfd5daf0` later received Codex CR-03-042 on arXiv stable identity normalization. Stage 04 planning must not start until the CR-03-042 remediation head passes live PR #10 CI and current-head Codex. If the remediation changes implementation behavior materially, submit the updated Stage 03 packet to GPT Pro again before closing Stage 03.

## Stage 03 CR-03-043 Re-review PASS And Stage 04 Planning Instruction From GPT Pro

Timestamp: 2026-05-30T21:11:44-05:00

Source files:

- `reviews/stage_03/GPT_PRO_CR_03_043_REREVIEW_RESPONSE.md`
- `reviews/stage_03/GPT_PRO_CR_03_043_REREVIEW_ACTION_ITEMS.md`

GPT Pro reviewed PR #10, CR-03-043 remediation head `adb41c36e66a25ddfa943950b7e08a685906560e`, current CI PASS links, current-head Codex no-major evidence, and the old-style arXiv id remediation, then returned:

```text
Verdict: PASS for Stage 03 PR #10 current head adb41c36e66a25ddfa943950b7e08a685906560e.
Is CR-03-043 resolved? yes.
Is PR #10 allowed to merge after current CI and Codex evidence? yes.
Is Stage 04 planning-only allowed next? yes.
Stage 04 implementation is not authorized.
```

Stage 04 planning objective: plan an evidence extraction skeleton only. The plan may define extraction schemas, relation type enum, quote-span validation plan, no-quote rationale plan, provenance validation plan, mock LLM extraction adapter plan, extraction worker skeleton plan, mock-only tests, and stop conditions.

Allowed Stage 04 planning files:

- `PLANS/STAGE_04_PLAN.md`
- `TASKS/STAGE_04_TASKS.md`
- `CHECKLISTS/STAGE_04_CHECKLIST.md`
- `reviews/stage_04/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_04/PR_BODY.md`
- `reviews/stage_04/STAGE_ACCEPTANCE_RESULT.md`
- `deployments/stage_04/GITHUB_PR.md`
- `docs/architecture/stage_04_evidence_extraction.md`
- `docs/codex/stage_04_commands.md`
- `logs/subagents/stage_04/`
- required `CONTROL/` and `RUNLOG/` updates.

The Stage 04 plan may reference future implementation paths such as `apps/api/finsignalhub_api/extraction/` and `apps/api/tests/test_stage04_extraction.py`, but must not create extraction implementation code until Stage 04 implementation is separately approved.

Forbidden until separately approved: production extraction, external LLM calls, real API keys, external network calls, claim graph logic, Research Delta logic, Repro Pack logic, MCP business tools, UI/dashboard behavior, chatbot/RAG behavior, stock prediction, investment advice, Risk Mode, Replay Engine, auth, billing, or destructive repository restructuring.

## Stage 03 Merge Closeout And Active Stage 04 Planning State

Timestamp: 2026-05-30T21:46:24-05:00

Stage 03 final evidence head `92970f32f0b22754dad02c661e2b1b9a5d313fec` passed PR #10 CI and Codex no-major after the CR-03-043 GPT Pro re-review PASS was saved. PR #10 was squash-merged into `main` at `13ee0a0bc497578b235662ea60c9aa225c62e53f`, and tag `stage-03-source-connectors` was pushed.

The active next-stage instruction is still Stage 04 planning only. Stage 04 implementation remains unauthorized until the Stage 04 planning PR passes CI/Codex, GPT Pro returns PASS or accepted CONDITIONAL PASS for the plan, and a separate implementation `/goal` is created.

## Stage 04 Planning PASS And Implementation Goal Draft Instruction From GPT Pro

Timestamp: 2026-05-31T01:58:00-05:00

Source files:

- `reviews/stage_04/GPT_PRO_PLAN_REVIEW_RESPONSE.md`
- `reviews/stage_04/GPT_PRO_PLAN_ACTION_ITEMS.md`
- `reviews/stage_04/GPT_PRO_REVIEW_RESPONSE.md`
- `reviews/stage_04/GPT_PRO_ACTION_ITEMS.md`

GPT Pro reviewed PR #11, Stage 04 planning head `d62d8d8eafb73eb207ba401e12f9d073dff61223`, CI PASS links, current-head Codex no-major evidence, and the Stage 04 planning review packet, then returned:

```text
Final gate result: PASS.
Stage 04 planning accepted; separate implementation /goal drafting allowed; Stage 04 implementation not yet authorized.
```

Authorized next action: draft a separate Stage 04 implementation `/goal` only after the response/action-item evidence closeout head is pushed and passes live PR #11 CI plus current-head Codex review.

Future implementation `/goal` objective: implement a mock-only evidence extraction skeleton that can later transform Stage 03 normalized `Document` records into provenance-preserving `EvidenceItem` candidate payloads.

Allowed future implementation goal paths:

- `apps/api/finsignalhub_api/extraction/`
- `apps/api/finsignalhub_api/extraction/schemas.py`
- `apps/api/finsignalhub_api/extraction/relations.py`
- `apps/api/finsignalhub_api/extraction/quote_span.py`
- `apps/api/finsignalhub_api/extraction/provenance.py`
- `apps/api/finsignalhub_api/extraction/mock_llm.py`
- `apps/api/finsignalhub_api/extraction/worker.py`
- `apps/api/tests/test_stage04_extraction.py`
- `apps/api/tests/fixtures/stage04_extraction/`
- Stage 04 docs, reviews, deployments, logs, `CONTROL/`, `RUNLOG/`, `TASKS/`, and `CHECKLISTS/` records required by the stage gate.

Required future implementation scope:

- Evidence candidate schema.
- Relation type enum.
- Quote-span validator.
- No-quote rationale validator.
- Provenance preservation validator.
- Deterministic mock LLM adapter.
- Mock-only worker skeleton.

Required future tests:

- Mock-only extraction tests.
- No-network enforcement.
- Quote-span valid and invalid cases.
- No-quote rationale requirement.
- Relation validation.
- Provenance preservation.
- Candidate schema validation.
- Deterministic mock adapter output.
- Worker fixture test.
- High-confidence secret scan.
- Forbidden-scope scan.
- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04`.
- `python -m compileall apps/api/finsignalhub_api`.
- `git diff --check`.
- CI PASS.
- Current-head Codex no-major.
- Final GPT Pro implementation review.

Required future subagents:

- `extraction-schema-agent`
- `relation-enum-agent`
- `quote-span-agent`
- `provenance-agent`
- `mock-llm-adapter-agent`
- `worker-skeleton-agent`
- `test-agent`
- `docs-log-agent`
- `scope-review-agent`

Forbidden until the separate implementation goal is accepted:

- External LLM API calls.
- Real network calls.
- Production extraction pipeline.
- Claim graph computation.
- Research Delta computation.
- Repro Pack export logic.
- MCP business tools.
- UI/dashboard behavior.
- Chatbot/RAG behavior.
- Stock prediction or investment advice.
- Risk Mode or Replay Engine.
- Auth or billing.
- Unreviewed Stage 03 connector changes.

Stop if any future Stage 04 implementation draft or work requires a real LLM API key, external network access, claim graph work, Research Delta work, Repro Pack output, MCP business tools, UI/dashboard behavior, auth/billing, stock/investment behavior, chatbot/RAG behavior, Risk Mode, Replay Engine, unresolved CI/Codex gate, or unreviewed Stage 03 connector modification.

## Stage 04 Implementation Goal Accepted By GPT Pro

Timestamp: 2026-06-05T16:18:46-05:00

Source files:

- `reviews/stage_04/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md`
- `reviews/stage_04/GPT_PRO_IMPLEMENTATION_GOAL_ACTION_ITEMS.md`
- `reviews/stage_04/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md`

GPT Pro reviewed PR #11 head `e6cb1052572d84f1c0f0fa7041e210e72d64d104`, CI PASS links, Codex no-major evidence, unresolved review threads = 0, and `reviews/stage_04/GPT_PRO_IMPLEMENTATION_GOAL_PACKET.md`, then returned:

```text
VERDICT: PASS.
The Stage 04 implementation-goal draft is complete enough to start a later Stage 04 implementation run, provided a separate /goal starts implementation, current-head CI/Codex evidence remains valid, and no new commit resets the gate.
```

Accepted next `/goal`:

```text
/goal

Implement Stage 04: Evidence Extraction Skeleton.

Use the approved Stage 04 implementation-goal draft and GPT Pro implementation-goal review response.

Product identity:
FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. Stage 04 is evidence extraction skeleton only.

Objective:
Implement a mock-only evidence extraction skeleton that can transform Stage 03 normalized Document records into provenance-preserving EvidenceItem candidate payloads. This stage must not perform production extraction, external LLM calls, claim graph computation, Research Delta computation, Repro Pack generation, MCP business-tool exposure, UI/dashboard behavior, chatbot/RAG behavior, stock prediction, investment advice, Risk Mode, or Replay Engine.

Allowed files:
- apps/api/finsignalhub_api/extraction/__init__.py
- apps/api/finsignalhub_api/extraction/schemas.py
- apps/api/finsignalhub_api/extraction/relations.py
- apps/api/finsignalhub_api/extraction/provenance.py
- apps/api/finsignalhub_api/extraction/quote_span.py
- apps/api/finsignalhub_api/extraction/mock_llm.py
- apps/api/finsignalhub_api/extraction/worker.py
- apps/api/tests/test_stage04_extraction.py
- apps/api/tests/fixtures/stage04_extraction/README.md
- apps/api/tests/fixtures/stage04_extraction/*.json
- docs/architecture/stage_04_evidence_extraction.md
- docs/codex/stage_04_commands.md
- logs/subagents/stage_04/*.md
- reviews/stage_04/
- deployments/stage_04/
- required CONTROL/, RUNLOG/, TASKS/, CHECKLISTS/, and CHANGELOG records
```

Implementation may start only after this response-saving evidence head passes live PR #11 CI, current-head Codex no-major, and unresolved review threads = 0.

## Stage 04 Final Closeout Recheck PASS And Implementation-Goal Draft Instruction From GPT Pro

Timestamp: 2026-06-05T14:41:54-05:00

Source files:

- `reviews/stage_04/GPT_PRO_FINAL_CLOSEOUT_RECHECK_RESPONSE.md`
- `reviews/stage_04/GPT_PRO_FINAL_CLOSEOUT_RECHECK_ACTION_ITEMS.md`

GPT Pro reviewed PR #11, Stage 04 closeout head `3864181e1dfcbdf522884e7f78e4cb0815b96966`, CI PASS links, Codex no-major links, unresolved review-thread count of 0, and the stale README P2 verification comment, then returned:

```text
VERDICT: PASS.
Is Stage 04 planning closeout complete now? yes.
Does current PR #11 GitHub gate now pass given CI PASS, Codex no-major, and unresolved review threads = 0? yes.
No blocking must-fix remains.
Drafting a separate Stage 04 implementation /goal is allowed.
Stage 04 implementation itself remains separate and not authorized.
```

Next authorized work: after the final response/action-item evidence-sync head is pushed and passes live PR #11 CI plus current-head Codex no-major, draft Stage 04 implementation `/goal` artifacts only.

Required implementation-goal draft files:

- `PLANS/STAGE_04_IMPLEMENTATION_GOAL.md`
- `reviews/stage_04/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md`
- `reviews/stage_04/GPT_PRO_IMPLEMENTATION_GOAL_PACKET.md`

The implementation-goal draft must define allowed files, forbidden files, subagents, tests, risks, stop conditions, CI/Codex/GPT Pro gates, and explicit implementation boundaries.

Allowed future implementation scope for the draft:

- Extraction schemas.
- Relation enum.
- Quote-span validation.
- No-quote rationale validation.
- Provenance validation.
- Deterministic mock LLM adapter.
- Extraction worker skeleton.
- Mock-only tests.

Still forbidden until the separate implementation goal is accepted:

- `apps/api/finsignalhub_api/extraction/`
- `apps/api/tests/test_stage04_extraction.py`
- `apps/api/tests/fixtures/stage04_extraction/`
- Runtime extraction schemas.
- Mock LLM adapter code.
- Worker code.
- Real LLM calls.
- External network calls.
- Production extraction.
- Claim graph computation.
- Research Delta computation.
- Repro Pack logic.
- MCP business tools.
- UI/dashboard behavior.
- Chatbot/RAG behavior.
- Stock prediction.
- Investment advice.
- Risk Mode.
- Replay Engine.
- Auth.
- Billing.

## Stage 04 Final Implementation PASS And Stage 05 Planning Instruction From GPT Pro

Timestamp: 2026-06-05T18:18:39-05:00

Source files:

- `reviews/stage_04/GPT_PRO_IMPLEMENTATION_REVIEW_RESPONSE.md`
- `reviews/stage_04/GPT_PRO_IMPLEMENTATION_ACTION_ITEMS.md`

GPT Pro reviewed PR #11 implementation head `79ec29a42b9119dbaf5edd1c88b7fb4e52fe1368`, CI PASS evidence, Codex current-head no-major evidence, unresolved review threads = 0, CR-04-029 remediation, local verification results, and the Stage 04 implementation review packet, then returned:

```text
VERDICT: PASS.
Stage 04 implementation final acceptance allowed for reviewed head 79ec29a.
No blocking must-fix items remain.
Final response/action-item save is evidence-only; if it creates a new commit, rerun CI and current-head Codex before merge/tag.
Next authorized action: Stage 05 planning only.
Stage 05 implementation may not start until the Stage 05 plan is reviewed, a separate Stage 05 implementation goal is drafted, and the user approves that goal.
```

## Next Stage ID

Stage 05 planning: Claim Graph and Research Delta.

## Next Stage Goal

Create a reviewable Stage 05 planning package for a future mock-only, non-persistent, deterministic claim graph and research delta skeleton. Planning may define boundaries, files, tests, subagents, risks, and acceptance evidence. It must not create claim graph implementation code, Stage 05 test code, persistence, UI, MCP business tools, or business logic.

## Required Stage 05 Planning Files

- `PLANS/STAGE_05_PLAN.md`
- `TASKS/STAGE_05_TASKS.md`
- `CHECKLISTS/STAGE_05_CHECKLIST.md`
- `docs/architecture/stage_05_claim_graph_delta.md`
- `docs/codex/stage_05_commands.md`
- `reviews/stage_05/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_05/CODEX_REVIEW_SUMMARY.md`
- `reviews/stage_05/PR_BODY.md`
- `reviews/stage_05/STAGE_ACCEPTANCE_RESULT.md`
- `deployments/stage_05/GITHUB_PR.md`
- `logs/subagents/stage_05/README.md`
- Required `CONTROL/`, `RUNLOG/`, and `CHANGELOG.md` updates.

## Future Implementation Objects To Plan, Not Execute

- `ResearchClaimCreate`
- `ClaimEvidenceEdgeCreate`
- `ResearchDeltaCreate`
- `LiteratureMatrixRowCreate`
- `MethodCardCreate`
- `DatasetCardCreate`

## Stage 05 Planning Constraints

- Stage 05 planning only; implementation is not authorized.
- Outputs must remain candidate-level and mock-only until later approval.
- No persistence, migrations, database writes, routers, frontend/UI behavior, dashboard behavior, MCP business tools, external LLM calls, live network calls, API keys, provider clients, Repro Pack export, Risk Mode, Replay Engine, chatbot/RAG behavior, stock prediction, investment advice, auth, billing, or unreviewed changes to Stage 03 connectors or Stage 04 extraction behavior.
- Preserve Stage 04 provenance fields: source, quote/no-quote rationale, document reference, candidate id, tool lineage, and deterministic fixture trace.

## Required Stage 05 Tests To Plan

- Deterministic claim candidate generation.
- Bounded edge relation types.
- Evidence-to-claim provenance preservation.
- No claim edge without evidence reference.
- No delta without old/new evidence snapshots.
- Literature matrix row payload validation.
- Method card and dataset card payload validation.
- Duplicate/cycle handling.
- Unsupported-claim rejection.
- No prediction/recommendation wording in research deltas.
- No network/provider imports.
- Deterministic fixture output.
- Full regression coverage across Stage 02 through Stage 05.

## Stage 05 Main Risks

- Scope explosion.
- Premature graph persistence.
- Treating candidate edges as verified truth.
- Unsupported research judgments.
- Research Delta becoming prediction, investment advice, risk scoring, or trading signal.
- Fabricated method/dataset metadata.
- Loss of Stage 04 provenance.
- Literature matrix/card work drifting into report generation.

## Stage 04 Current-Head Final PASS And Updated Stage 05 Planning Instruction

Timestamp: 2026-06-06T10:47:06-05:00

Source files:

- `reviews/stage_04/GPT_PRO_CURRENT_HEAD_FINAL_REVIEW_RESPONSE.md`
- `reviews/stage_04/GPT_PRO_CURRENT_HEAD_FINAL_ACTION_ITEMS.md`

GPT Pro reviewed PR #11 head `cd3c1cfeef0dc075f5fd35cfd4d6451c712e75df`, CI PASS evidence, current-head Codex no-major evidence, unresolved review threads = 0, and CR-04-039 remediation, then returned:

```text
Stage 04 current head: PASS.
Merge/tag Stage 04: allowed after live gate refresh if the response-saving evidence commit creates a new head.
Next allowed action: Stage 05 planning only.
Stage 05 implementation: not authorized.
```

Current blocker before Stage 05 planning handoff:

- B-0102: this response/action save creates a new PR #11 head.
- The new head must pass CI, current-head Codex no-major, and unresolved review threads = 0 before merge/tag or Stage 05 planning starts.

## Updated Stage 05 Planning Requirements

Stage 05 name:

```text
Stage 05: Claim Graph and Research Delta Planning
```

Stage 05 objective:

Plan the Claim Graph and Research Delta implementation boundaries. The plan must define how Stage 02 domain models and Stage 04 evidence candidates connect into future claim graph, claim-evidence relation logic, research delta calculation, project-boundary validation, relation-state updates, mock-only tests, docs, logs, and gates.

Allowed Stage 05 planning files:

- `PLANS/STAGE_05_PLAN.md`
- `TASKS/STAGE_05_TASKS.md`
- `CHECKLISTS/STAGE_05_CHECKLIST.md`
- `reviews/stage_05/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_05/CODEX_REVIEW_SUMMARY.md`
- `reviews/stage_05/PR_BODY.md`
- `reviews/stage_05/STAGE_ACCEPTANCE_RESULT.md`
- `deployments/stage_05/GITHUB_PR.md`
- `docs/architecture/stage_05_claim_graph_research_delta.md`
- `docs/codex/stage_05_commands.md`
- `logs/subagents/stage_05/`
- Required `CONTROL/`, `RUNLOG/`, and `CHANGELOG.md` updates.

Future Stage 05 implementation files may be planned but not created during planning:

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

Forbidden during Stage 05 planning:

- MCP business tools.
- Repro Pack export logic.
- Frontend UI behavior or dashboard behavior.
- Chatbot behavior or generic RAG.
- Stock prediction, investment advice, Risk Mode, or Replay Engine.
- Auth, billing, live external API calls, real LLM calls, new connectors, or production extraction pipeline.
- New database domain model redesign.
- Destructive Stage 02 schema changes.
- Destructive Stage 03 connector changes.
- Destructive Stage 04 extraction changes.

Required Stage 05 planning subagents:

- `claim-graph-architecture-agent`
- `relation-rule-agent`
- `research-delta-agent`
- `project-boundary-validator-agent`
- `test-plan-agent`
- `docs-log-agent`
- `scope-review-agent`

Stage 05 plan must cover Claim Graph planning, Research Delta planning, same-project guards, provenance requirements, relation rationale, delta baseline/current time, mock-only tests, forbidden-scope scan, secret scan, `phase_check.py --stage 05`, compileall, `git diff --check`, CI PASS, current-head Codex no-major, unresolved review threads = 0, and final GPT Pro review for the later implementation stage.
