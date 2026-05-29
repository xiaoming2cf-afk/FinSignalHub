# Stage 02 Plan: Research Mode Domain Models

## Context Read

Required context for this plan:

- `AGENTS.md`
- `PLANS.md`
- `CONTROL/01_PRODUCT_DEFINITION.md`
- `CONTROL/02_STAGE_ROADMAP.md`
- `CONTROL/03_PHASE_ACCEPTANCE.md`
- `CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md`
- `CONTROL/16_CAPABILITY_AUDIT.md`
- `CONTROL/19_STAGE_DASHBOARD.md`
- `CONTROL/20_BLOCKER_LOG.md`
- `RUNLOG/LONG_RUN_SUMMARY.md`
- `reviews/stage_01/STAGE_ACCEPTANCE_RESULT.md`
- `reviews/stage_01/GPT_PRO_REVIEW_RESPONSE.md`

Stage 01 is accepted. GPT Pro authorized **Stage 02 planning only** and did not authorize Stage 02 implementation.

## Capability Check

Known current capabilities:

- Local shell: available.
- GitHub CLI and GitHub plugin: available.
- GitHub Actions: available.
- Codex PR review: available, but responses can lag; use bounded retry and method switch.
- Chrome/GPT Pro route: available through visible Chrome and local visual recovery; stop on login, captcha, payment, permission, secrets, or unclear consent.
- Docker: available for Stage 01 checks; must be revalidated before any Stage 02 implementation goal.
- Python and Node.js: available.
- MCP: product target, but Stage 02 must not implement MCP business tools.

## Product Alignment Check

FinSignalHub remains Research Mode-first, MCP-first, and evidence-stream oriented.

Stage 02 exists to create a minimum model layer that can later support:

- Research projects.
- Evidence items with mandatory provenance fields.
- Research claims and evidence edges.
- Research delta records as stored artifacts, not computation engines.
- Literature matrix rows.
- Method cards and dataset cards.
- Repro Pack export records as metadata only.
- Tool call logs.

This stage must not become a chatbot, generic RAG, stock prediction system, investment advice feature, ordinary report generator, financial dashboard, model leaderboard, Risk Mode, Replay Engine, connector runtime, evidence extraction pipeline, or MCP business tool layer.

### Mandatory Provenance Fields For Later Implementation

The later Stage 02 implementation goal must explicitly model and validate provenance. The plan is not satisfied by a generic `provenance` blob alone.

Required provenance attributes, where applicable:

- `source_identity`: stable source identifier, URL, citation key, uploaded document id, or dataset id.
- `source_type`: controlled value such as literature, preprint, dataset, method note, user upload metadata, or tool output.
- `retrieval_time`: timezone-aware timestamp for when the source or derived artifact was retrieved or generated.
- `quoted_evidence_span`: exact quoted text plus span offsets or page/section locator when a claim relies on a quote; nullable only with an explicit `no_quote_reason` for non-text artifacts.
- `transformation_notes`: concise record of normalization, parsing, manual correction, or model-assisted transformation.
- `confidence`: bounded confidence value or enum with documented meaning.
- `tool_call_lineage`: reference to the `ToolCallLog` record or equivalent tool-call lineage fields that produced or transformed the artifact.

Entity-level provenance requirements:

- `Source` and `Document` must preserve `source_identity`, `source_type`, retrieval or upload time, bibliographic or dataset locator fields, and enough metadata to support later connector replay without implementing connectors in Stage 02.
- `EvidenceItem` must carry all mandatory provenance attributes and cannot support a claim edge unless source identity, source type, retrieval time, transformation notes, confidence, and tool-call lineage are present.
- `ResearchClaim` must keep claim text, project linkage, derivation notes, confidence, and references to supporting or originating evidence artifacts.
- `ClaimEvidenceEdge` must keep `claim_id`, `evidence_item_id`, relation type, rationale, confidence, and the tool-call lineage that created or revised the edge.
- `ResearchDelta`, `LiteratureMatrixRow`, `MethodCard`, `DatasetCard`, and `ReproPackExport` must store source artifact references, generation time, transformation notes, confidence or review status, and tool-call lineage so later stages can export reproducible evidence.
- `ToolCallLog` must capture tool name, tool version or schema version, called-at time, argument hash or safe serialized arguments, input artifact ids, output artifact ids, status, and deterministic error shape without storing secrets.

## Scope

Stage 02 plan scope:

- Define minimum Research Mode domain model boundaries.
- Define database migration plan.
- Define Pydantic schema plan.
- Define model-level CRUD service/router plan.
- Define tests, CI checks, docs, logs, GitHub PR, Codex review, and GPT Pro plan review requirements.

Stage 02 implementation scope is **not authorized in this plan commit**. A later `/goal` must be approved after GPT Pro plan review.

## Files To Create Or Modify

Planning-only files in this branch:

- `PLANS/STAGE_02_PLAN.md`
- `TASKS/STAGE_02_TASKS.md`
- `CHECKLISTS/STAGE_02_CHECKLIST.md`
- `reviews/stage_02/GPT_PRO_REVIEW_PACKET.md`
- `reviews/stage_02/PR_BODY.md`
- `reviews/stage_02/STAGE_ACCEPTANCE_RESULT.md`
- `deployments/stage_02/GITHUB_PR.md`
- `logs/subagents/stage_02/`
- Control, artifact, dashboard, checkpoint, and RunLog records required by the stage process.

Implementation files proposed for a later approved Stage 02 goal:

- `apps/api/finsignalhub_api/db/`
- `apps/api/finsignalhub_api/models/`
- `apps/api/finsignalhub_api/schemas/`
- `apps/api/finsignalhub_api/services/`
- `apps/api/finsignalhub_api/routers/`
- `apps/api/finsignalhub_api/core/`
- `apps/api/tests/`
- `apps/api/alembic/`
- `apps/api/alembic.ini`
- `apps/api/alembic/versions/`
- `docs/architecture/stage_02_domain_models.md`
- `docs/codex/stage_02_commands.md`
- `pyproject.toml`
- `docker-compose.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/phase-deploy.yml`
- `.env.example`
- `README.md`
- `AGENTS.md` only if stage rules need clarification.

## Files Not To Touch

Until Stage 02 plan review and goal approval pass, do not create or modify:

- `apps/api/finsignalhub_api/models/`
- `apps/api/finsignalhub_api/schemas/`
- `apps/api/finsignalhub_api/services/`
- `apps/api/finsignalhub_api/routers/`
- `apps/api/alembic/`
- Any migration files.
- Any product table or model runtime code.

Always forbidden in Stage 02:

- External connectors: OpenAlex, Crossref, Semantic Scholar, arXiv, user upload ingestion.
- External API calls.
- LLM adapters or extraction.
- Evidence extraction pipeline.
- Quote-span extraction logic beyond a schema field.
- Dedup pipeline.
- Claim graph computation.
- Research delta computation beyond model/table fields.
- Literature matrix generation logic.
- Repro Pack export logic.
- MCP business tools.
- ChatGPT App or third-party connector implementation.
- Risk Mode, Replay Engine, stock prediction, investment advice, chatbot UI, generic RAG, dashboard product behavior, auth, or billing.

## Skills

Required skills:

- `finsignal-product-governor`
- `evidence-graph-architect`
- `phase-gate-auditor`
- `codex-log-keeper`
- `gpt-pro-review-preparer`
- `browser-gpt-pro-reviewer`
- `github-stage-deployer`
- `github-review-resolver`
- `subagent-coordinator`
- `acceptance-evidence-collector`

## Subagents

Stage 02 implementation plan must declare bounded subagents:

- `schema-agent`: `apps/api/finsignalhub_api/models/`, `apps/api/finsignalhub_api/db/`
- `migration-agent`: `apps/api/alembic/`, `apps/api/alembic.ini`
- `api-schema-agent`: `apps/api/finsignalhub_api/schemas/`, `apps/api/finsignalhub_api/routers/`, `apps/api/finsignalhub_api/services/`
- `test-agent`: `apps/api/tests/`
- `docs-log-agent`: docs, `CONTROL/`, `RUNLOG/`, `reviews/stage_02/`, `deployments/stage_02/`, `logs/subagents/stage_02/`

Each subagent must write a log under `logs/subagents/stage_02/<agent_name>.md` with files touched, summary, risks, tests, and unresolved issues. No subagent may modify the full repository.

## Implementation Steps For Later Goal

These steps are not authorized until GPT Pro plan review and user `/goal` approval pass:

1. Revalidate Docker, Python, GitHub, and current branch status.
2. Create minimum SQLAlchemy/SQLModel domain models.
3. Create Alembic setup and migration.
4. Create Pydantic schemas for model primitives.
5. Create CRUD services and basic API routers for model-level primitives only.
6. Add tests for models, migrations, schemas, CRUD, and forbidden scope.
7. Update docs, logs, review packet, PR body, acceptance result, and artifact registry.
8. Run local checks.
9. Commit, push, open/update PR, request Codex review, wait for CI, handle critical findings.
10. Submit Stage 02 final implementation packet to GPT Pro only after CI and Codex pass.

## Tests

### Local checks

Planning branch local checks:

- `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02`
- No Stage 02 implementation file check against the branch diff.
- Secret scan for placeholder-only configuration.
- Forbidden scope scan for connectors, LLM adapters, MCP business tools, extraction, claim graph computation, research delta computation, UI product behavior, Risk Mode, Replay Engine, stock prediction, and investment advice.
- `git diff --check`

Later implementation local checks must rerun after every meaningful code change.

### Unit tests

Planning branch unit tests are not applicable because no Stage 02 implementation files are authorized.

Later implementation unit tests must cover model constructors or factories, Pydantic schema validation, CRUD service behavior, deterministic error shapes, provenance field validation, and forbidden-null constraints for evidence lineage.

### Integration tests

Planning branch integration tests are not applicable because no model runtime, migration, database, connector, MCP tool, or API router implementation is authorized.

Later implementation integration tests must cover Alembic upgrade/downgrade behavior, database persistence for the approved Research Mode entities, and basic API route behavior for model-level CRUD only.

### Acceptance checks

Planning acceptance requires:

- Stage 02 plan, task, checklist, review packet, PR body, acceptance placeholder, deployment placeholder, and logs exist.
- No Stage 02 implementation/model/migration/CRUD files are created.
- GitHub PR, CI, Codex review, and GPT Pro plan review evidence are recorded.
- GPT Pro returns PASS or accepted CONDITIONAL PASS before any Stage 02 implementation goal begins.

Later implementation acceptance must use the ten phase gates and cannot request Stage 03 until Stage 02 implementation receives final GPT Pro PASS.

The Stage 02 goal must include:

```powershell
python -m pytest apps/api/tests
python -m compileall apps/api/finsignalhub_api
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02
git diff --check
```

Migration checks:

```powershell
alembic upgrade head
alembic downgrade -1
alembic upgrade head
```

If downgrade is not supported, the exception must be documented with rationale and GPT Pro must decide whether it blocks.

If Postgres is used through Docker:

```powershell
docker compose up -d postgres
alembic upgrade head
docker compose down
```

Additional checks:

- Secret scan.
- Forbidden scope scan.
- No connector files.
- No LLM adapter files.
- No MCP business tool files.
- No front-end product behavior.

## Docs

Required docs for implementation goal:

- `docs/architecture/stage_02_domain_models.md`
- `docs/codex/stage_02_commands.md`
- Updated README only if it clarifies stage status and does not claim product runtime completion.

Docs must describe provenance-bearing fields, relationships, migration commands, and what Stage 02 intentionally does not implement.

## GitHub Deployment

Branch: `stage/02-domain-models`.

Commit format: `stage-02: summary`.

PR title: `Stage 02: Research Mode Domain Models`.

PR body source: `reviews/stage_02/PR_BODY.md`.

Required PR comment after creation:

```text
@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems
```

Critical Codex findings must be fixed or explicitly deferred with reason before GPT Pro final implementation review.

## GPT Pro Review

This planning branch must submit `reviews/stage_02/GPT_PRO_REVIEW_PACKET.md` to GPT Pro for plan review.

GPT Pro must answer:

- PASS / CONDITIONAL PASS / FAIL for the Stage 02 plan.
- Must-fix plan items.
- Deferrable items.
- Whether Stage 02 implementation may begin after user `/goal` approval.
- Required implementation boundaries and stop conditions.

Stage 02 implementation cannot begin without GPT Pro plan PASS or accepted CONDITIONAL PASS and user goal approval.

## Risks

- Premature connector implementation.
- Turning `ResearchDelta` into a computation engine.
- Turning `EvidenceItem` into an extraction pipeline.
- Implementing MCP business tools before Stage 06.
- Over-complex model relationships.
- Irreproducible migrations.
- Weak provenance fields that cannot support evidence-stream outputs later.
- Treating model-level CRUD as research workflow behavior.

## Stop Conditions

Stop and ask user/GPT Pro if:

- External data APIs are required.
- A real LLM API key is required.
- Model design exceeds Research Mode P0.
- Alembic migration cannot run and the cause is unclear.
- Auth or billing is requested.
- Stage 01 scaffold requires destructive changes.
- Investment advice, stock prediction, Risk Mode, or Replay Engine implementation appears.
- Docker/Postgres remains unavailable and migration tests depend on it.

## Done When

This planning step is done when:

- Stage 02 plan, task, checklist, PR body, review packet, acceptance placeholder, and deployment placeholder exist.
- Logs and artifact registry record the Stage 02 planning artifacts.
- No Stage 02 runtime/model/migration/CRUD files are created.
- Local planning checks pass.
- PR is opened and Codex review is requested.
- GPT Pro plan review is submitted and saved.
