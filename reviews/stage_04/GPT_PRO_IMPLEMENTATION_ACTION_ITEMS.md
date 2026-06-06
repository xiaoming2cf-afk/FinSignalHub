# Stage 04 GPT Pro Implementation Action Items

Source response: `reviews/stage_04/GPT_PRO_IMPLEMENTATION_REVIEW_RESPONSE.md`

Reviewed PR head: `79ec29a42b9119dbaf5edd1c88b7fb4e52fe1368`

GPT Pro verdict: **PASS**

## Required Closeout Actions

| Item | Status | Evidence / next step |
| --- | --- | --- |
| Save final GPT Pro response | done locally | Full response saved in `reviews/stage_04/GPT_PRO_IMPLEMENTATION_REVIEW_RESPONSE.md`. |
| Save extracted action items | done locally | This file records the required closeout and Stage 05 planning instructions. |
| Preserve reviewed-head evidence | done locally | GPT Pro accepted PR #11 head `79ec29a42b9119dbaf5edd1c88b7fb4e52fe1368`, current-head CI PASS, Codex no-major, unresolved threads = 0, and local verification results. |
| Rerun external gates for the response-saving head | pending after push | If this evidence save creates a new commit, PR #11 must again show CI PASS, current-head Codex no-major, and unresolved review threads = 0 before merge/tag. |
| Track GitHub Actions runtime warning | deferred | GPT Pro noted the Node.js 20 Actions deprecation warning; Stage 05 planning must include a CI runtime review before later stages rely on the current workflow runtime. |

## Stage 04 Final Acceptance Interpretation

Stage 04 implementation is accepted for reviewed head `79ec29a42b9119dbaf5edd1c88b7fb4e52fe1368`.

This file is part of a new evidence-sync patch. The patch must pass the same live external gate after push. Do not merge or tag from stale reviewed-head evidence if this file changes the PR head.

## Stage 05 Planning Instructions From GPT Pro

Next authorized action: **Stage 05 planning only**.

Stage 05 title: **Claim Graph and Research Delta**.

Stage 05 implementation may not begin until:

- A Stage 05 plan is created and reviewed.
- A separate Stage 05 implementation goal is drafted.
- The user approves that implementation goal.
- Stage 05 plan PR has CI PASS, Codex current-head no-major, unresolved review threads = 0, and GPT Pro plan approval.

Allowed Stage 05 planning files:

- `PLANS/STAGE_05_PLAN.md`
- `TASKS/STAGE_05_TASKS.md`
- `CHECKLISTS/STAGE_05_CHECKLIST.md`
- `docs/architecture/stage_05_claim_graph_delta.md`
- `docs/codex/stage_05_commands.md`
- `reviews/stage_05/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_05/PR_BODY.md`
- `reviews/stage_05/STAGE_ACCEPTANCE_RESULT.md`
- `deployments/stage_05/GITHUB_PR.md`
- `logs/subagents/stage_05/README.md`
- Required `CONTROL/`, `RUNLOG/`, and `CHANGELOG.md` updates.

Future Stage 05 implementation may be planned, but not executed yet, as a mock-only, non-persistent, deterministic claim/delta skeleton that consumes Stage 04 candidate evidence payloads and produces candidate payloads for:

- `ResearchClaimCreate`
- `ClaimEvidenceEdgeCreate`
- `ResearchDeltaCreate`
- `LiteratureMatrixRowCreate`
- `MethodCardCreate`
- `DatasetCardCreate`

Forbidden for Stage 05 planning and future implementation unless separately approved:

- Database writes, migrations, persistence routes, frontend/UI behavior, dashboard behavior, MCP business tools, external LLM calls, live network calls, API keys, provider clients, Repro Pack export, Risk Mode, Replay Engine, chatbot/RAG behavior, stock prediction, investment advice, auth, billing, and unreviewed changes to Stage 03 connectors or Stage 04 extraction behavior.

Required Stage 05 plan test coverage to specify:

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

Primary Stage 05 risks:

- Scope explosion.
- Premature graph persistence.
- Treating candidate edges as verified truth.
- Generating unsupported research judgments.
- Turning Research Delta into prediction, investment advice, risk scoring, or trading signal.
- Fabricating method/dataset metadata.
- Losing Stage 04 provenance.
- Letting literature matrix or card generation become a report generator.
