# GPT Pro Review Packet: Stage 04 Evidence Extraction Planning

Please review FinSignalHub Stage 04 planning only. Do not review this as implementation code.

## Project Identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. It serves researchers, PhD students, labs, research teams, research-oriented product teams, and innovation teams.

Core outputs remain research delta, claim graph, evidence card, literature matrix, method card, dataset card, Repro Pack, and tool call log.

Forbidden directions remain chatbot, generic RAG, stock prediction, investment advice, ordinary report generator, standalone dashboard behavior, model leaderboard, Risk Mode, and Replay Engine.

## Stage 03 Closure Evidence

- Stage 03 PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10
- Stage 03 merge commit: `13ee0a0bc497578b235662ea60c9aa225c62e53f`
- Stage 03 tag: `stage-03-source-connectors`
- Final Stage 03 evidence head: `92970f32f0b22754dad02c661e2b1b9a5d313fec`
- CI PASS: https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26701084288/job/78693930282
- CI PASS: https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26701083605/job/78693928721
- Codex no-major: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/10#issuecomment-4585499255
- GPT Pro CR-03-043 re-review PASS: `reviews/stage_03/GPT_PRO_CR_03_043_REREVIEW_RESPONSE.md`

## Stage 04 Goal

Plan an evidence extraction skeleton that can later transform Stage 03 normalized documents into provenance-preserving evidence candidates.

This Stage 04 planning PR must define extraction schemas, relation type enum, quote-span validation, no-quote rationale validation, provenance validation, mock LLM extraction adapter plan, extraction worker skeleton plan, mock-only tests, subagent boundaries, GitHub/Codex/GPT Pro gates, and stop conditions.

## Actual Work In This Planning Packet

Files created or updated:

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
- required `CONTROL/` and `RUNLOG/` updates

## Explicit Non-Implementation

Stage 04 planning does not create:

- `apps/api/finsignalhub_api/extraction/`
- `apps/api/tests/test_stage04_extraction.py`
- `apps/api/tests/fixtures/stage04_extraction/`

It also does not implement production extraction, external LLM calls, real API keys, external network calls, claim graph logic, Research Delta logic, Repro Pack logic, MCP business tools, UI/dashboard behavior, chatbot/RAG behavior, stock prediction, investment advice, Risk Mode, Replay Engine, auth, billing, or destructive repository restructuring.

## Required Checks Before GPT Pro Submission

Codex must insert current evidence after PR creation:

- Branch head
- CI job URLs
- Codex review result
- Local planning check outputs
- PR URL

Required local checks:

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04`
- No extraction implementation directory
- No Stage 04 test file
- No Stage 04 fixture directory
- Secret scan
- Forbidden-scope scan
- `git diff --check`

## Known Limitations

- This is planning only. It deliberately does not prove runtime extraction behavior.
- The mock LLM adapter is a plan, not an implementation.
- Relation labels are planned for future extraction candidates only and must not be treated as claim graph edges in Stage 04 planning.
- Stage 04 implementation will need a separate `/goal` after GPT Pro plan PASS.

## Questions For GPT Pro

Please answer:

1. PASS / CONDITIONAL PASS / FAIL for Stage 04 planning.
2. Must-fix issues before Stage 04 implementation planning can proceed.
3. Deferrable items.
4. Whether this plan preserves Research Mode-first, MCP-first, evidence-stream product direction.
5. Whether quote-span, no-quote rationale, relation enum, provenance validation, and mock LLM boundaries are sufficient for a later implementation goal.
6. Whether any forbidden Stage 05+ claim graph, Research Delta, Repro Pack, MCP business tool, UI, chatbot/RAG, stock/investment, Risk Mode, or Replay Engine behavior leaked into Stage 04 planning.
7. If PASS, provide exact Stage 04 implementation `/goal` requirements, files, tests, risks, subagents, and stop conditions.

Do not authorize implementation directly from this packet. If PASS, authorize drafting a separate Stage 04 implementation `/goal` only.
