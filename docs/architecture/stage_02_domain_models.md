# Stage 02 Research Mode Domain Models

Stage 02 implements model-level primitives for FinSignalHub's Research Mode MVP. The scope is domain schema, Alembic migration, Pydantic schemas, CRUD services, primitive API routers, tests, docs, and logs.

This stage does not implement connectors, external API calls, LLM adapters, evidence extraction, claim graph computation, research delta computation, literature matrix generation, Repro Pack export logic, MCP business tools, ChatGPT App, Claude Connector, Copilot Connector, Gemini Connector, Risk Mode, Replay Engine, stock prediction, investment advice, chatbot UI, generic RAG, dashboard behavior, auth, or billing.

## Product Mapping

| Model | Research need | Later output supported |
| --- | --- | --- |
| `ResearchProject` | Track one research question and its evidence corpus | research delta, literature matrix, repro pack |
| `Source` | Preserve source identity before connector replay exists | evidence card, dataset card |
| `Document` | Store normalized document metadata without extraction | evidence card, literature matrix |
| `EvidenceItem` | Store provenance-backed evidence spans or no-quote rationale | evidence card, claim graph edge |
| `ResearchClaim` | Store research claims without computing graph state | claim graph |
| `ClaimEvidenceEdge` | Link claims to evidence with relation, rationale, confidence, lineage | claim graph |
| `ResearchDelta` | Store delta artifacts only, not compute them | research delta |
| `LiteratureMatrixRow` | Store matrix rows only, not generate them | literature matrix |
| `MethodCard` | Store method metadata and limitations | method card |
| `DatasetCard` | Store dataset metadata and source identity | dataset card |
| `ReproPackExport` | Store export manifest metadata only | repro pack |
| `ToolCallLog` | Preserve safe tool-call lineage and deterministic errors | replayable evidence stream |

## Provenance Fields

Evidence-bearing and generated artifact models expose explicit fields instead of hiding all provenance in a generic blob:

- `source_identity`
- `source_type`
- `retrieval_time`
- `publication_time` where applicable
- `url`, `doi`, or `locator` where applicable
- `quoted_evidence_span` as structured JSON, or `no_quote_reason`
- `transformation_notes`
- `confidence`
- `tool_call_id` and/or `tool_call_lineage`
- `validation_status`

`ToolCallLog.safe_arguments` must be sanitized and must not contain API keys, tokens, cookies, or secrets.

## Relationships

`ResearchProject` owns all Stage 02 artifacts. `Source` owns normalized `Document` records and may link to `EvidenceItem`. `ResearchClaim` connects to `EvidenceItem` through `ClaimEvidenceEdge`. `ToolCallLog` can link to generated or transformed artifacts, but Stage 02 does not execute business tools.

## Project Scope Guards

Stage 02 CRUD routes must not create orphan project-scoped records. The default SQLite engine enables foreign-key checks, and project-scoped create hooks validate that submitted `project_id` values already exist.

Generated artifact `source_artifact_refs` are Stage 02 provenance references, not generation instructions. They may point to known project-scoped Stage 02 artifacts, including `Source`, `Document`, `EvidenceItem`, `ResearchClaim`, `ResearchDelta`, `LiteratureMatrixRow`, `MethodCard`, `DatasetCard`, `ReproPackExport`, `ToolCallLog`, and `ClaimEvidenceEdge`. Unknown refs are rejected. `ClaimEvidenceEdge` refs derive project scope from their linked claim and evidence item and are rejected if those records are inconsistent or belong to another project.

## Migration

The initial Alembic revision is `0001_research_mode_domain_models`. It creates only the approved Stage 02 tables and supports downgrade to the empty schema for this initial migration.

Use `FINSIGNALHUB_DATABASE_URL` for migration checks. `DATABASE_URL` is accepted only as a fallback.

## Root Config Exception

Stage 02 required `pyproject.toml`, `.env.example`, and `docker-compose.yml` updates to make SQLAlchemy, Alembic, PostgreSQL migration checks, and container database routing verifiable. This is recorded as a Stage 02 implementation exception because the approved Stage 02 done-when requires migration and CRUD tests.
