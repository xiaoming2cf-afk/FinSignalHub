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
