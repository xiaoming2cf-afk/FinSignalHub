# Stage 04 GPT Pro Implementation-Goal Action Items

## Source

- Response file: `reviews/stage_04/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md`
- Reviewed PR head: `e6cb1052572d84f1c0f0fa7041e210e72d64d104`
- GPT Pro verdict: PASS
- Captured at: 2026-06-05T16:18:46-05:00

## Required Closeout Actions

| ID | Action | Status | Evidence |
| --- | --- | --- | --- |
| GP-04-GOAL-001 | Save GPT Pro response | done locally | `reviews/stage_04/GPT_PRO_IMPLEMENTATION_GOAL_REVIEW_RESPONSE.md` |
| GP-04-GOAL-002 | Save GPT Pro action items | done locally | this file |
| GP-04-GOAL-003 | Update implementation-goal draft acceptance to PASS | in progress | `reviews/stage_04/IMPLEMENTATION_GOAL_DRAFT_ACCEPTANCE.md` |
| GP-04-GOAL-004 | Update current-state, action queue, checkpoint log, RunLog, RunLog summary, and artifact registry | in progress | `CONTROL/24`, `CONTROL/25`, `CONTROL/27`, `RUNLOG/`, `CONTROL/18` |
| GP-04-GOAL-005 | Confirm no new commit appeared after reviewed CI/Codex evidence before starting implementation | pending after evidence-sync push | Saving this evidence changes the head, so live CI/Codex must be refreshed before implementation |
| GP-04-GOAL-006 | Start implementation only through the accepted `/goal` | pending | Implementation code has not started |

## Deferred Items

| ID | Deferred item | Earliest stage |
| --- | --- | --- |
| GP-04-DEF-001 | Broader extraction edge cases | Stage 04 follow-up or later |
| GP-04-DEF-002 | Richer fixture corpus | Stage 04 follow-up or later |
| GP-04-DEF-003 | Relation-label expansion | Stage 04 follow-up or later |
| GP-04-DEF-004 | Advanced provenance completeness policy | Stage 04 follow-up or later |
| GP-04-DEF-005 | Extraction observability | Stage 04 follow-up or later |
| GP-04-DEF-006 | Claim graph, Research Delta, Repro Pack, and MCP business-tool work | Stage 05+ only after explicit GPT Pro gate |

## Hard Boundary

Do not create Stage 04 implementation files until the response-saving evidence head passes live PR #11 CI, current-head Codex no-major, unresolved review threads = 0, and implementation starts under the accepted `/goal`.
