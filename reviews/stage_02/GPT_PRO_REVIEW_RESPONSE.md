# Stage 02 Plan Gate Review：**PASS**

本次只审查 **Stage 02 planning**，不审查也不授权任何 Stage 02 implementation code。基于你提供的 live preface，以及 PR #8 当前页面可见信息，Stage 02 计划可以判定为：

> **PASS — Stage 02 plan gate 达标。**
> **允许进入 Stage 02 implementation 的前提：用户显式 `/goal` 批准 + 保存本次 GPT Pro plan review response + 继续保持 Stage 02 禁止项边界。**
> **不授权 Stage 03。**

PR #8 当前定位明确是 “Stage 02: Research Mode Domain Models”，PR 说明写明该 PR 是 planning-only，直到 GPT Pro plan review 和用户 `/goal` approval 才能授权 implementation；其 scope 也限定为 domain model boundaries、migration plan、Pydantic schema plan、CRUD/router plan、tests、docs、CI、review、risks 和 stop conditions，不包含实现代码。([GitHub][1])

---

# 1. Stage 02 plan result

```text
Stage 02 plan result: PASS
```

理由如下：

1. **阶段定位正确**
   Stage 02 被限定为 Research Mode Domain Models，且 review packet 明确说明 Stage 02 implementation 尚未开始，没有 domain models、migrations、CRUD、connectors、MCP business tools、evidence extraction、claim graph、Research Delta、Repro Pack、chatbot UI、dashboard、stock prediction 或 investment advice。

2. **Planning-only 边界清楚**
   PR #8 描述明确写明该 PR 不实现 domain model runtime code、migrations、CRUD routers、connectors、extraction、claim graph computation、research delta computation、Repro Pack export、MCP business tools、admin UI product features、Risk Mode、Replay Engine、stock prediction、investment advice、chatbot UI、generic RAG 或 dashboard product behavior。([GitHub][1])

3. **GitHub/Codex gate 已从历史 pending 状态更新为 live PASS 状态**
   committed packet 内部保留历史 pending / remediation 记录是合理的，因为 live preface 已明确覆盖历史状态。PR 页面显示 current head 为 `857696e`，并且 Codex review 对该 head 返回 “Didn't find any major issues”。([GitHub][1])

4. **CI 已通过**
   两个 Stage 02 相关 GitHub Actions job 均显示 `governance-check succeeded`，耗时分别为 1m25s 和 1m21s；存在 Node.js 20 deprecation warning，但不阻断 plan gate。([GitHub][2])

5. **此前 Codex review 发现的问题已被计划吸收**
   PR 页面记录此前 Codex 指出过 mandatory provenance fields 不够具体、路径使用错误等问题；当前 review packet 已明确把 provenance 细化为 source identity、source type、retrieval time、quoted evidence span/no-quote rationale、transformation notes、confidence、tool-call lineage，并且纠正了实现路径应使用现有 `apps/api/finsignalhub_api` 包的问题。([GitHub][1])

---

# 2. Must-fix items before Stage 02 implementation may begin

这里区分 **plan 内容 must-fix** 与 **implementation 启动前流程 must-fix**。

## 2.1 Plan 内容 must-fix

```text
None blocking.
```

从当前 packet 看，Stage 02 plan 已满足进入 implementation 前的计划审查要求。没有需要重新修 plan 的阻断项。

## 2.2 Implementation 启动前 must-fix

Stage 02 implementation 开始前必须完成以下动作：

### Must-fix 1：保存本次 GPT Pro plan review response

必须创建或更新：

```text
reviews/stage_02/GPT_PRO_PLAN_REVIEW_RESPONSE.md
reviews/stage_02/GPT_PRO_PLAN_REVIEW_ACTION_ITEMS.md
reviews/stage_02/STAGE_ACCEPTANCE_RESULT.md
```

并写明：

```text
Stage 02 plan gate: PASS
Implementation authorization: requires user /goal approval
Stage 03: not authorized
```

---

### Must-fix 2：更新状态与运行日志

必须更新：

```text
CONTROL/24_CURRENT_STAGE_STATE.md
CONTROL/25_NEXT_ACTION_QUEUE.md
CONTROL/27_CHECKPOINT_LOG.md
RUNLOG/LONG_RUN_CURRENT.md
RUNLOG/LONG_RUN_SUMMARY.md
CONTROL/18_ARTIFACT_REGISTRY.md
CONTROL/19_STAGE_DASHBOARD.md
```

状态应写为：

```text
Stage 02 plan: PASS
Stage 02 implementation: pending user /goal approval
Stage 03: not authorized
```

---

### Must-fix 3：用户必须显式 `/goal` 批准

Stage 02 plan PASS 不等于自动进入 implementation。Implementation 必须由用户明确发送 `/goal` 或同等明确批准后开始。

---

### Must-fix 4：Stage 02 implementation 必须沿用现有 API package 路径

此前 Codex 指出过计划里误用不存在的 `apps/api/app` 路径，而当前 scaffold 实际运行的是 `apps/api/finsignalhub_api`。Stage 02 implementation 必须使用现有包路径：

```text
apps/api/finsignalhub_api/
```

不得重新引入：

```text
apps/api/app/
```

除非单独发起架构变更 ADR 并重新审查。PR 页面记录该路径问题曾被 Codex 指出并已在计划中修正。([GitHub][1])

---

### Must-fix 5：provenance 字段必须作为显式字段建模

Stage 02 implementation 中，EvidenceItem / Source / Document / ToolCallLog 相关模型不能把关键 provenance 隐藏进无校验 blob。至少必须显式支持：

```text
source_identity
source_type
retrieval_time 或 ingestion_time
publication_time / release_time
url / doi / locator
quote_span 或 explicit no_quote_reason
transformation_notes
confidence
tool_call_lineage
validation_status
```

PR 页面中 Codex 曾明确指出 provenance 不能只高层描述，必须枚举 source identity/type、retrieval time、quoted span、transformation notes、confidence、tool-call lineage；当前 packet 已将这些列为 mandatory coverage，implementation 必须落实。([GitHub][1])

---

# 3. Deferrable items

以下事项可以延后，不阻断 Stage 02 implementation：

## Deferred 1：Node.js 20 deprecation warning

CI job 中出现 Node.js 20 deprecation warning，但 governance-check 已成功。该项可以作为 maintenance item 放入 Stage 03 或 CI hardening backlog，不阻断 Stage 02 plan 或 implementation。([GitHub][2])

## Deferred 2：完整业务计算逻辑

以下均应延后：

```text
research delta computation engine
claim graph computation engine
literature matrix generation logic
Repro Pack export logic
evidence extraction pipeline
LLM extraction adapter
connector execution
MCP business tools
```

Stage 02 只建立模型、schema、CRUD 和迁移基础。

## Deferred 3：高级数据完整性约束

可以在 Stage 02 先实现基础字段、关系、enum、nullable 约束和测试。更复杂的约束，如 provenance completeness policy、graph edge validation policy、tool-call lineage strict validator，可以在 Stage 04/05/06 分阶段增强。但 Stage 02 至少要预留字段和基础校验。

## Deferred 4：管理员 UI 呈现

Stage 02 不需要 Web admin UI 展示这些模型。前端视图属于 Stage 07。

---

# 4. Whether Stage 02 implementation may begin after user `/goal` approval

**可以。**

准确表述：

```text
Stage 02 implementation may begin after:
1. this GPT Pro plan review response is saved;
2. action items are recorded;
3. current stage state/action queue/runlog are updated;
4. user explicitly issues /goal approval;
5. implementation remains within Stage 02 model/schema/CRUD/migration/test/docs boundary.
```

Stage 02 plan PASS 不自动授权 implementation。用户必须显式给 Codex：

```text
/goal
Implement Stage 02 Research Mode Domain Models...
```

---

# 5. Required file boundaries for Stage 02 implementation

## 5.1 Allowed files / directories

Stage 02 implementation 允许创建或修改：

```text
apps/api/finsignalhub_api/db/
apps/api/finsignalhub_api/models/
apps/api/finsignalhub_api/schemas/
apps/api/finsignalhub_api/services/
apps/api/finsignalhub_api/routers/
apps/api/finsignalhub_api/core/

apps/api/alembic.ini
apps/api/alembic/
apps/api/alembic/env.py
apps/api/alembic/versions/

apps/api/tests/

docs/architecture/stage_02_domain_models.md
docs/codex/stage_02_commands.md

reviews/stage_02/
deployments/stage_02/
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

可有限修改：

```text
pyproject.toml
docker-compose.yml
.github/workflows/ci.yml
.github/workflows/phase-deploy.yml
.env.example
README.md
AGENTS.md only if governance wording needs clarification
```

---

## 5.2 Forbidden files / behaviors

Stage 02 implementation 禁止创建或实现：

```text
workers/ingestion_worker/
workers/extraction_worker/
workers/delta_worker/

OpenAlex connector
Crossref connector
Semantic Scholar connector
arXiv connector
user upload ingestion connector

LLM adapters
external API clients
evidence extraction pipeline
dedup pipeline
claim graph computation
research delta computation
literature matrix generation logic
Repro Pack export logic

MCP business tools:
create_research_project
get_research_delta
map_research_claims
build_literature_matrix
suggest_methods
suggest_data_sources
export_repro_pack
get_ai_capability_delta

Risk Mode
Replay Engine
stock prediction
investment advice
chatbot UI
generic RAG
dashboard product behavior
auth/billing
```

---

# 6. Required tests and CI checks

Stage 02 implementation 必须至少包含以下测试。

## 6.1 Local tests

```text
pytest apps/api/tests
alembic upgrade head
alembic downgrade -1 or documented blocker
alembic upgrade head
python -m compileall apps/api/finsignalhub_api
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02
secret scan
forbidden scope scan
git diff --check
```

## 6.2 Database tests

若 Docker/Postgres 可用：

```text
docker compose up -d postgres
alembic upgrade head
run model/CRUD tests against test database
docker compose down
```

若 Docker/Postgres 不可用：

```text
record blocker
run SQLite-compatible unit tests if supported
do not claim full DB acceptance
```

## 6.3 Model-level tests

必须覆盖：

```text
ResearchProject create/list/get/update
Source create/list/get/update
Document create/list/get/update
EvidenceItem create/list/get/update
ResearchClaim create/list/get/update
ClaimEvidenceEdge create/list/get/update
ResearchDelta create/list/get/update
LiteratureMatrixRow create/list/get/update
MethodCard create/list/get/update
DatasetCard create/list/get/update
ReproPackExport create/list/get/update
ToolCallLog create/list/get/update
```

如果全部 CRUD 在 Stage 02 过重，可采用统一 generic CRUD test pattern，但必须覆盖模型注册、schema validation 和 route availability。

## 6.4 Scope tests

必须增加禁止项扫描，确认没有：

```text
connectors
LLM adapter
extraction worker
claim graph engine
delta engine
Repro Pack exporter
MCP business tools
Risk Mode
Replay Engine
stock/investment behavior
chatbot UI
```

---

# 7. Required subagents

Stage 02 implementation 建议使用以下 subagents，并要求每个 subagent 输出日志到：

```text
logs/subagents/stage_02/<agent-name>.md
```

## 7.1 `schema-agent`

职责：

```text
Implement SQLAlchemy/SQLModel model definitions.
Define relationships, enums, timestamp fields, JSON fields, provenance fields.
```

文件边界：

```text
apps/api/finsignalhub_api/models/
apps/api/finsignalhub_api/db/
```

## 7.2 `migration-agent`

职责：

```text
Set up Alembic env.
Create initial migration.
Validate upgrade/downgrade where possible.
```

文件边界：

```text
apps/api/alembic/
apps/api/alembic.ini
```

## 7.3 `api-schema-agent`

职责：

```text
Create Pydantic schemas and basic CRUD routers/services.
No business workflow.
No extraction logic.
No connector logic.
```

文件边界：

```text
apps/api/finsignalhub_api/schemas/
apps/api/finsignalhub_api/services/
apps/api/finsignalhub_api/routers/
```

## 7.4 `test-agent`

职责：

```text
Add model/schema/router/migration/scope tests.
```

文件边界：

```text
apps/api/tests/
```

## 7.5 `docs-log-agent`

职责：

```text
Update docs, review packets, acceptance result, artifact registry, RunLog, dashboard.
```

文件边界：

```text
docs/
CONTROL/
RUNLOG/
reviews/stage_02/
deployments/stage_02/
logs/subagents/stage_02/
```

---

# 8. Required stop conditions

Codex 必须停止并记录 blocker，如果出现：

```text
1. 需要真实外部 API key。
2. 需要真实 LLM API key。
3. 需要实现 connectors。
4. 需要实现 extraction pipeline。
5. 需要实现 claim graph computation。
6. 需要实现 research delta computation。
7. 需要实现 MCP business tools。
8. 需要实现 Repro Pack export logic。
9. 需要实现 Risk Mode or Replay Engine。
10. 需要 auth/billing。
11. 需要改变 product identity。
12. 需要创建 apps/api/app 而不是使用 apps/api/finsignalhub_api。
13. Alembic migration 无法运行且原因不明。
14. Docker/Postgres 不可用且 Stage 02 DB acceptance 依赖它。
15. 出现 stock prediction、investment advice、chatbot UI、generic RAG 或 dashboard behavior。
```

---

# 9. Product-alignment risks before implementation

## Risk 1：过度实现

Stage 02 最容易越界到 Stage 05/06。必须保持：

```text
models and CRUD only
```

## Risk 2：provenance 被弱化成 metadata blob

必须避免。关键 provenance 要有显式字段或明确 schema，不应全部塞进无校验 JSON。

## Risk 3：ResearchDelta 被实现为 computation engine

禁止。Stage 02 只定义表与 CRUD。

## Risk 4：EvidenceItem 被实现成 extraction pipeline

禁止。Stage 04 才能做 extraction。

## Risk 5：MCP tools 提前暴露业务行为

禁止。Stage 06 才能做 business MCP tools。

## Risk 6：路径不一致

Stage 02 必须基于 Stage 01 scaffold 的实际 package：

```text
apps/api/finsignalhub_api
```

不得使用旧计划中的：

```text
apps/api/app
```

---

# 10. Exact Stage 02 `/goal` requirements

下面是可以给 Codex 的 Stage 02 `/goal`：

```text
/goal

Implement Stage 02: Research Mode Domain Models.

Use the approved PLANS/STAGE_02_PLAN.md and the GPT Pro Stage 02 plan review response.

Product identity:
FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. Stage 02 is domain models only.

Scope:
Implement Research Mode domain model schema, Alembic migration, Pydantic schemas, model-level CRUD services/routers, tests, docs, logs, and acceptance artifacts.

Allowed models:
- ResearchProject
- Source
- Document
- EvidenceItem
- ResearchClaim
- ClaimEvidenceEdge
- ResearchDelta
- LiteratureMatrixRow
- MethodCard
- DatasetCard
- ReproPackExport
- ToolCallLog

Required provenance fields:
- source identity
- source type
- retrieval or ingestion time
- publication or release time where applicable
- URL / DOI / locator where applicable
- quoted evidence span or explicit no-quote rationale
- transformation notes
- confidence
- tool-call lineage where applicable
- validation status

Allowed files:
- apps/api/finsignalhub_api/db/
- apps/api/finsignalhub_api/models/
- apps/api/finsignalhub_api/schemas/
- apps/api/finsignalhub_api/services/
- apps/api/finsignalhub_api/routers/
- apps/api/finsignalhub_api/core/
- apps/api/alembic/
- apps/api/alembic.ini
- apps/api/tests/
- docs/architecture/stage_02_domain_models.md
- docs/codex/stage_02_commands.md
- reviews/stage_02/
- deployments/stage_02/
- logs/subagents/stage_02/
- CONTROL and RUNLOG files needed for logs/artifacts/status

Forbidden:
No connectors, external API calls, LLM adapters, evidence extraction pipeline, dedup pipeline, claim graph computation, research delta computation, literature matrix generation, Repro Pack export, MCP business tools, ChatGPT App, Claude Connector, Copilot Connector, Gemini Connector, Risk Mode, Replay Engine, stock prediction, investment advice, chatbot UI, generic RAG, dashboard behavior, auth, or billing.

Subagents:
Use schema-agent, migration-agent, api-schema-agent, test-agent, docs-log-agent. Each subagent must write logs under logs/subagents/stage_02/.

Tests:
Run:
- pytest apps/api/tests
- alembic upgrade head
- alembic downgrade -1 or documented blocker
- alembic upgrade head
- python -m compileall apps/api/finsignalhub_api
- python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02
- secret scan
- forbidden scope scan
- git diff --check

If Docker/Postgres is required, run docker compose up -d postgres and migration checks. If Docker/Postgres is unavailable, record blocker and do not claim full DB acceptance.

Done when:
1. All approved models exist.
2. Alembic migration exists and runs.
3. Pydantic schemas exist.
4. CRUD services/routers exist for model primitives.
5. Tests pass.
6. No forbidden Stage 03+ logic exists.
7. Docs updated.
8. Logs updated.
9. Artifact registry updated.
10. PR updated.
11. @codex review requested and critical findings resolved.
12. CI passes.
13. GPT Pro final implementation review passes.
14. GPT Pro assigns Stage 03.

Stop if:
- external API key is needed
- LLM API key is needed
- connector/extraction/claim graph/delta/MCP business logic is requested
- product scope drifts
- database migration cannot run and no safe fallback is available
```

---

# Final Verdict

```text
Stage 02 plan result: PASS

Stage 02 implementation may begin:
YES, but only after user /goal approval and after this GPT Pro plan review response/action items are saved.

Stage 03:
NOT authorized.

Implementation boundary:
Domain models + migrations + schemas + CRUD primitives + tests + docs/logs only.

Main must-fix before implementation:
Save this review response and update current stage state/action queue/runlog/artifact registry. Then proceed only via explicit /goal.
```

[1]: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8 "Stage 02: Research Mode Domain Models by xiaoming2cf-afk · Pull Request #8 · xiaoming2cf-afk/FinSignalHub · GitHub"
[2]: https://github.com/xiaoming2cf-afk/FinSignalHub/actions/runs/26641127042/job/78514186780 "stage-02: keep changelog user visible · xiaoming2cf-afk/FinSignalHub@857696e · GitHub"
