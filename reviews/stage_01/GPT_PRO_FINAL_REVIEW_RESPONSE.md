# Stage 01 Repo Scaffold 最终验收结论：**PASS**

基于你提供的 Stage 01 final implementation packet，并结合可见的 GitHub PR、CI、Codex review 证据，Stage 01 可以判定为：

> **PASS — Stage 01 repo scaffold 达标，可以接受。**
> **允许进入 Stage 02 planning only。**
> **不允许直接进入 Stage 02 implementation。**

PR #7 当前是 `stage/01-repo-scaffold` 合并到 `main` 的 Stage 01 PR，公开页面显示该 PR 目标就是 “Stage 01: Repo Scaffold”。([GitHub][1]) CI job 显示 `governance-check` succeeded，仅存在 Node.js 20 deprecation warning；该 warning 不阻断 Stage 01。([GitHub][2]) Codex review 在当前 review 流程中已给出 “Didn't find any major issues”，满足 Stage 01 的 Codex review gate。([GitHub][1])

---

# 1. Stage 01 implementation：PASS

Stage 01 的边界是：

```text
repo scaffold only
```

你提供的实现内容符合该边界：

```text
docker-compose.yml
pyproject.toml
package.json
apps/api health-only FastAPI
apps/mcp_server health/server-info with tools_enabled=false
apps/web_admin inspect-only Next.js page
docs
CI
logs
subagent summaries
```

这属于 Stage 01 允许范围。

同时，review packet 明确说明没有引入以下禁止内容：

```text
ResearchProject
EvidenceItem
ResearchClaim
ClaimEvidenceEdge
ResearchDelta
LiteratureMatrix
MethodCard
DatasetCard
ReproPackExport
ToolCallLog
connectors
LLM adapters
evidence extraction
claim graph
research delta
Repro Pack logic
Risk Mode
Replay Engine
stock prediction
investment advice
chatbot UI
generic RAG
dashboard product behavior
```

因此，Stage 01 没有越界到 Stage 02+。

---

# 2. Must-fix items before Stage 01 acceptance

**无阻断性 must-fix。**

本次审查视角下，Stage 01 可以接受。此前 Stage 01 的关键 gate 已满足：

```text
1. Docker ordering 已解决。
2. Docker daemon / Compose 已恢复。
3. docker compose config 已作为 implementation-preflight 执行。
4. scaffold runtime 已完成。
5. 本地 checks 通过。
6. GitHub CI 通过。
7. @codex review 当前实现 head 无 major issues。
8. 没有越界业务功能。
9. B-0016 本身就是等待 GPT Pro final review；本回复通过后可关闭。
```

Stage 01 acceptance result 中应更新：

```text
B-0016: resolved by GPT Pro final implementation PASS.
Stage 01 final result: PASS / ACCEPTED.
```

---

# 3. Deferrable items

以下事项可以延后，不阻断 Stage 01：

## Deferred 1：Node.js 20 actions deprecation warning

CI 页面显示 GitHub Actions 对 Node.js 20 actions 有 deprecation warning。该 warning 不影响 Stage 01 scaffold acceptance，但应记录为后续维护事项。([GitHub][2])

建议写入：

```text
CONTROL/12_RISK_REGISTER.md
CONTROL/20_BLOCKER_LOG.md 或 maintenance section
Stage 02 / CI hardening backlog
```

## Deferred 2：更强 CI hardening

Stage 01 只需要 scaffold health/build 级别 CI。以下可延后：

```text
coverage gate
strict typing gate
dependency audit blocking gate
security scan hardening
Node 24 migration
matrix build
```

## Deferred 3：Web admin 功能化

Stage 01 只需要 inspect-only scaffold status page。以下应延后：

```text
project list
project detail
evidence review
claim graph view
literature matrix view
export center
```

这些属于 Stage 07。

## Deferred 4：MCP business tools

Stage 01 只允许 health/server-info。以下应延后到 Stage 06：

```text
create_research_project
get_research_delta
map_research_claims
build_literature_matrix
suggest_methods
suggest_data_sources
export_repro_pack
get_ai_capability_delta
```

---

# 4. 是否允许 Stage 01 accepted now

**允许。**

Stage 01 可以标记为：

```text
PASS / ACCEPTED
```

需要立即更新的记录：

```text
reviews/stage_01/STAGE_ACCEPTANCE_RESULT.md
CONTROL/24_CURRENT_STAGE_STATE.md
CONTROL/25_NEXT_ACTION_QUEUE.md
CONTROL/27_CHECKPOINT_LOG.md
RUNLOG/LONG_RUN_CURRENT.md
RUNLOG/LONG_RUN_SUMMARY.md
CONTROL/18_ARTIFACT_REGISTRY.md
CONTROL/19_STAGE_DASHBOARD.md
CONTROL/20_BLOCKER_LOG.md
```

其中 `B-0016` 应改为：

```text
resolved by GPT Pro Stage 01 final implementation PASS.
```

---

# 5. 是否允许进入 Stage 02

**允许进入 Stage 02 planning only。**

不允许直接进入 Stage 02 implementation。

Stage 02 必须先执行：

```text
/plan
```

并创建：

```text
PLANS/STAGE_02_PLAN.md
reviews/stage_02/GPT_PRO_REVIEW_PACKET.md
reviews/stage_02/PR_BODY.md
reviews/stage_02/STAGE_ACCEPTANCE_RESULT.md
deployments/stage_02/GITHUB_PR.md
```

Stage 02 plan 必须先经过 GPT Pro plan review。只有 Stage 02 plan 通过、用户批准、GitHub branch 创建、scope fence 明确之后，才能进入 Stage 02 implementation。

---

# 6. Stage 02 planning requirements

## Stage 02 名称

```text
Stage 02: Research Mode Domain Models
```

## Stage 02 目标

Stage 02 的目标是建立 Research Mode 的最小领域模型和基础 CRUD，为后续 Stage 03 connectors、Stage 04 evidence extraction、Stage 05 claim graph/research delta、Stage 06 MCP tools 提供数据底座。

Stage 02 只做：

```text
domain model schema
database migration
Pydantic schemas
basic CRUD services
basic API routers
tests
docs
logs
```

Stage 02 不做任何外部数据接入、LLM 抽取、业务推理、MCP business tools 或前端功能。

---

## Stage 02 允许创建 / 修改的文件边界

允许：

```text
PLANS/STAGE_02_PLAN.md
TASKS/STAGE_02_TASKS.md
CHECKLISTS/STAGE_02_CHECKLIST.md

apps/api/app/db/
apps/api/app/models/
apps/api/app/schemas/
apps/api/app/services/
apps/api/app/routers/
apps/api/app/core/
apps/api/tests/

apps/api/alembic/
apps/api/alembic.ini
apps/api/alembic/versions/

docs/architecture/stage_02_domain_models.md
docs/codex/stage_02_commands.md

reviews/stage_02/GPT_PRO_REVIEW_PACKET.md
reviews/stage_02/PR_BODY.md
reviews/stage_02/STAGE_ACCEPTANCE_RESULT.md
deployments/stage_02/GITHUB_PR.md

logs/subagents/stage_02/
CONTROL/04_EXECUTION_LOG.md
CONTROL/07_CODEX_GOAL_REGISTRY.md
CONTROL/18_ARTIFACT_REGISTRY.md
CONTROL/19_STAGE_DASHBOARD.md
CONTROL/20_BLOCKER_LOG.md
CONTROL/24_CURRENT_STAGE_STATE.md
CONTROL/25_NEXT_ACTION_QUEUE.md
CONTROL/27_CHECKPOINT_LOG.md
RUNLOG/LONG_RUN_CURRENT.md
RUNLOG/LONG_RUN_SUMMARY.md
```

可修改：

```text
pyproject.toml
docker-compose.yml
.github/workflows/ci.yml
.github/workflows/phase-deploy.yml
.env.example
README.md
AGENTS.md only if stage rules need clarification
```

---

## Stage 02 必须实现的核心模型

Stage 02 的核心模型为：

```text
ResearchProject
Source
Document
EvidenceItem
ResearchClaim
ClaimEvidenceEdge
ResearchDelta
LiteratureMatrixRow
MethodCard
DatasetCard
ReproPackExport
ToolCallLog
```

建议字段级边界：

### ResearchProject

```text
id
title
description
research_area
target_outputs
status
created_at
updated_at
```

### Source

```text
id
source_name
source_type
access_type
base_url
reliability_class
metadata
created_at
```

### Document

```text
id
source_id
title
authors
venue
doi
url
source_type
publication_time
ingestion_time
raw_text
abstract
metadata
content_hash
```

### EvidenceItem

```text
id
project_id
document_id
source_type
source_name
url
release_time
evidence_claim
quote_span
evidence_type
relation_type
validation_status
created_at
```

### ResearchClaim

```text
id
project_id
claim_text
claim_type
state
created_at
updated_at
```

### ClaimEvidenceEdge

```text
id
claim_id
evidence_id
relation
rationale
created_at
```

### ResearchDelta

```text
id
project_id
baseline_time
current_time
summary
new_evidence_ids
updated_claims
new_gaps
created_at
```

### LiteratureMatrixRow

```text
id
project_id
document_id
research_question
method
data
finding
limitations
use_for_project
created_at
```

### MethodCard

```text
id
project_id
method_name
source_document_ids
core_idea
transferable_use
limitations
created_at
```

### DatasetCard

```text
id
project_id
dataset_name
source_url
access_type
coverage
variables
use_case
limitations
created_at
```

### ReproPackExport

```text
id
project_id
export_type
export_status
file_uri
manifest
created_at
```

### ToolCallLog

```text
id
tool_name
input_json
output_json
client_name
latency_ms
created_at
```

---

# 7. Stage 02 必须禁止的内容

Stage 02 严禁实现：

```text
OpenAlex connector
Crossref connector
Semantic Scholar connector
arXiv connector
user upload ingestion
external API calls
LLM adapters
LLM extraction
evidence extraction pipeline
quote_span extraction logic beyond schema field
dedup pipeline
claim graph computation
research delta computation logic beyond model/table
literature matrix generation logic
Repro Pack export logic
MCP business tools
ChatGPT App
Claude Connector
Copilot Connector
Risk Mode
Replay Engine
stock prediction
investment advice
chatbot UI
generic RAG
dashboard product behavior
auth / billing
```

Stage 02 可以创建 routers 和 CRUD，但这些必须是 model-level primitives，不得变成业务 workflow。

---

# 8. Stage 02 subagents

Stage 02 plan 应配置以下 subagents：

## 1. `schema-agent`

职责：

```text
Define SQLAlchemy/SQLModel models.
Ensure table names, relationships, enums, JSON fields, timestamps.
```

允许文件：

```text
apps/api/app/models/
apps/api/app/db/
```

## 2. `migration-agent`

职责：

```text
Create Alembic setup and migration.
Verify migration upgrade/downgrade if feasible.
```

允许文件：

```text
apps/api/alembic/
apps/api/alembic.ini
```

## 3. `api-schema-agent`

职责：

```text
Create Pydantic schemas and CRUD routers.
No business workflows.
```

允许文件：

```text
apps/api/app/schemas/
apps/api/app/routers/
apps/api/app/services/
```

## 4. `test-agent`

职责：

```text
Add tests for models, migrations, CRUD, forbidden scope.
```

允许文件:

```text
apps/api/tests/
```

## 5. `docs-log-agent`

职责：

```text
Update docs, logs, review packet, artifact registry, stage dashboard.
```

允许文件:

```text
docs/
CONTROL/
RUNLOG/
reviews/stage_02/
deployments/stage_02/
logs/subagents/stage_02/
```

---

# 9. Stage 02 测试要求

Stage 02 implementation 必须通过：

```text
pytest apps/api/tests
alembic upgrade head
alembic downgrade -1 or documented if not supported
alembic upgrade head again
python -m compileall apps/api/app
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02
secret scan
forbidden runtime/scope scan
git diff --check
```

CI 应至少覆盖：

```text
Python install
pytest
phase_check --stage 02
migration check if database service available
forbidden scope check
```

Docker 如果继续用于 Postgres 测试，则必须记录：

```text
docker compose up -d postgres
database migration pass
docker compose down
```

---

# 10. Stage 02 验收标准

Stage 02 PASS 条件：

```text
1. Stage 02 plan exists and GPT Pro plan review passes.
2. SQLAlchemy/SQLModel models exist.
3. Alembic migration exists and runs.
4. Pydantic schemas exist.
5. CRUD routers/services exist for model primitives.
6. Tests pass.
7. No external connectors exist.
8. No LLM extraction exists.
9. No MCP business tools exist.
10. No claim graph/research delta computation exists beyond tables/schemas.
11. No Risk Mode / Replay Engine / stock prediction / investment advice.
12. Docs updated.
13. Logs updated.
14. Artifact registry updated.
15. PR opened.
16. @codex review returns no critical issues.
17. CI passes.
18. GPT Pro final implementation review passes.
19. GPT Pro assigns Stage 03.
```

---

# 11. Stage 02 风险

## Risk 1：提前实现 connectors

阻断。Stage 03 才能做 connectors。

## Risk 2：把 ResearchDelta model 变成计算引擎

阻断。Stage 02 只建表和 schema，不实现 delta computation。

## Risk 3：把 EvidenceItem 变成 extraction pipeline

阻断。Stage 04 才能做 extraction。

## Risk 4：MCP business tools 提前实现

阻断。Stage 06 才能做 MCP tools。

## Risk 5：模型关系过度复杂

控制。Stage 02 保持最小关系，先支持后续扩展，不做复杂图数据库。

## Risk 6：数据库迁移不可复现

阻断。Alembic migration 必须可运行并记录命令。

---

# 12. Stage 02 停止条件

Codex 应停止并请求用户/GPT Pro 判断，如果：

```text
1. 需要引入外部数据 API。
2. 需要真实 LLM API key。
3. 模型设计要求超出 Research Mode P0。
4. Alembic migration 无法运行且原因不明。
5. 需要引入 auth/billing。
6. 需要修改 Stage 01 scaffold 结构并产生破坏性变更。
7. 出现投资建议、股票预测、Risk Mode、Replay Engine 相关实现。
8. Docker/Postgres 持续不可用且 migration test 依赖它。
```

---

# 13. 给 Codex 的下一步指令

```text
GPT Pro Stage 01 final implementation review result: PASS.

Stage 01 is accepted.

Before proceeding:
1. Save this GPT Pro response to reviews/stage_01/GPT_PRO_FINAL_REVIEW_RESPONSE.md.
2. Save action items to reviews/stage_01/GPT_PRO_FINAL_ACTION_ITEMS.md.
3. Update reviews/stage_01/STAGE_ACCEPTANCE_RESULT.md to PASS / ACCEPTED.
4. Mark B-0016 resolved.
5. Update CONTROL/24_CURRENT_STAGE_STATE.md.
6. Update CONTROL/25_NEXT_ACTION_QUEUE.md.
7. Append RUNLOG/LONG_RUN_CURRENT.md and RUNLOG/LONG_RUN_SUMMARY.md.
8. Update CONTROL/18_ARTIFACT_REGISTRY.md.
9. Update CONTROL/19_STAGE_DASHBOARD.md.
10. Update CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md with Stage 02 planning instructions.

Next action:
Begin Stage 02 planning only.

Do not implement Stage 02 yet.

Create PLANS/STAGE_02_PLAN.md.

Stage 02 plan must cover:
- Research Mode domain model scope
- file boundaries
- forbidden scope
- subagents
- migrations
- tests
- CI
- docs
- GitHub PR
- GPT Pro plan review
- stop conditions

After Stage 02 plan is created, prepare reviews/stage_02/GPT_PRO_REVIEW_PACKET.md and submit to GPT Pro for plan review.
```

---

# Final verdict

```text
Stage 01 implementation: PASS
Stage 01 may be accepted now: YES
Stage 02 may begin: PLANNING ONLY
Stage 02 implementation: NOT YET AUTHORIZED
Must-fix before Stage 02 implementation: Stage 02 plan + GPT Pro plan review
```

[1]: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/7 "Stage 01: Repo Scaffold by xiaoming2cf-afk · Pull Request #7 · xiaoming2cf-afk/FinSignalHub · GitHub"
[2]: https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26470335307/job/77941753720 "stage-01: add repo scaffold · xiaoming2cf-afk/FinSignalHub@f30a02e · GitHub"

