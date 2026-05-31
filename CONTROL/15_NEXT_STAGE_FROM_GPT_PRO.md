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
