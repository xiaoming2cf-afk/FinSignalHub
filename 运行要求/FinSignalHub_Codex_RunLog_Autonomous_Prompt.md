# FinSignalHub Codex RunLog-Driven Autonomous Build Prompt

版本：2026-05-24  
适用仓库：`FinSignalHub-main` 当前基础代码  
适用目标：让 Codex 在用户休息期间按阶段、按日志、按 GitHub/GPT Pro 阻断门持续推进 6–7 小时  
GPT Pro 审查页：<https://chatgpt.com/g/g-p-6a035355560081918d4a66ef7c70a14e-guo-chuang/c/6a131602-2de0-83ea-8b92-09691d87ad89>

---

## 1. 当前仓库状态判断

当前基础代码已经完成 **Stage 00：Governance / Control System**。仓库已经具备：

```text
CONTROL/00 - CONTROL/22
AGENTS.md
PLANS.md
TASKS/STAGE_00 - STAGE_09
CHECKLISTS/STAGE_00 - STAGE_09
reviews/stage_00/
deployments/stage_00/
.agents/skills/
finsignalhub-codex-plugin/
.github/workflows/
```

仓库自身记录显示 Stage 00 已经过 GitHub PR、CI、Codex review、GPT Pro review，并标记为 `PASS / COMPLETE`。

尚未完成：

```text
apps/api/
apps/mcp_server/
apps/web_admin/
docker-compose.yml
pyproject.toml
package.json
数据库模型
FastAPI runtime
MCP server runtime
Next.js admin runtime
OpenAlex / Crossref / Semantic Scholar / arXiv connectors
Evidence extraction
Claim Graph
Research Delta
Literature Matrix
Repro Pack
Research Mode MCP tools
```

因此，当前真实进度是：

```text
Stage 00 已完成
Stage 00.1 governance cleanup 建议先做
Stage 01 Repo Scaffold 尚未开始正式 plan
```

---

## 2. 产品总定位

FinSignalHub 是 **Research Mode-first、MCP-first、evidence-stream oriented** 的科研与金融证据流插件。

第一核心客户：

```text
科研人员
博士生
课题组
国创/大创团队
研究型产品团队
AI + Finance 研究者
政策与金融研究人员
```

P0 只做 Research Mode MVP，不做 Risk Mode，不做 Replay Engine，不做股票预测，不做投资建议，不做普通 RAG，不做普通报告生成器。

P0 核心对象：

```text
ResearchProject
ResearchClaim
Source
Document
EvidenceItem
ClaimEvidenceEdge
ResearchDelta
LiteratureMatrixRow
MethodCard
DatasetCard
ReproPackExport
ToolCallLog
```

P0 核心交付：

```text
持续追踪论文、政策、AI developer docs、新闻、金融披露和用户上传材料
结构化 EvidenceItem
Research Delta
Claim Graph
Literature Matrix
Method Card
Dataset Card
Repro Pack
MCP tools / AI Agent connectors
```

---

## 3. 本 Prompt 的使用方式

把本文档第 8 节的 `MASTER PROMPT FOR CODEX` 整段复制给 Codex。  
它会按 RunLog 循环推进：

```text
读日志和状态
判断当前阶段
生成/继续 goal
执行本阶段任务
写运行日志
GitHub PR
@codex review
GPT Pro review
保存下一阶段任务
继续下一阶段
```

如果用户休息时间很长，Codex 应持续推进，但只允许推进已经被阶段规则和 GPT Pro 允许的任务。

---

## 4. 本次长运行的建议目标

理想顺序：

```text
Stage 00.1 governance cleanup
  ↓
GitHub PR + @codex review
  ↓
GPT Pro review
  ↓
Stage 01 plan
  ↓
GPT Pro review Stage 01 plan
  ↓
Stage 01 implementation
  ↓
GitHub PR + @codex review + GPT Pro final review
  ↓
Stage 02 plan
  ↓
GPT Pro review Stage 02 plan
  ↓
Stage 02 implementation
  ↓
GitHub PR + @codex review + GPT Pro final review
  ↓
Stage 03 plan / implementation if GPT Pro assigns and approves
  ↓
Stage 04 plan only unless GPT Pro explicitly authorizes implementation
```

实际停止条件：

```text
GPT Pro 页面需要登录/验证码/权限
GitHub 权限不可用
Docker 无法运行且当前阶段依赖 Docker
需要 secret/API key/payment
GPT Pro 返回 FAIL 且要求用户决策
Codex 即将越过阶段边界
```

---

## 5. 必须优先使用的 Skills

Stage 00.1：

```text
finsignal-product-governor
phase-gate-auditor
codex-log-keeper
github-stage-deployer
gpt-pro-review-preparer
browser-gpt-pro-reviewer
github-review-resolver
acceptance-evidence-collector
stage-next-goal-synthesizer
```

Stage 01：

```text
finsignal-product-governor
subagent-coordinator
phase-gate-auditor
github-stage-deployer
gpt-pro-review-preparer
browser-gpt-pro-reviewer
codex-log-keeper
acceptance-evidence-collector
mcp-tool-builder 仅用于 MCP skeleton/server-info，不用于业务 tools
```

Stage 02：

```text
finsignal-product-governor
evidence-graph-architect
phase-gate-auditor
subagent-coordinator
codex-log-keeper
github-stage-deployer
gpt-pro-review-preparer
github-review-resolver
acceptance-evidence-collector
```

Stage 03：

```text
finsignal-product-governor
connector-builder
phase-gate-auditor
subagent-coordinator
github-stage-deployer
codex-log-keeper
gpt-pro-review-preparer
acceptance-evidence-collector
```

Stage 04：

```text
finsignal-product-governor
evidence-graph-architect
connector-builder
phase-gate-auditor
subagent-coordinator
codex-log-keeper
gpt-pro-review-preparer
```

---

## 6. Subagents 搭配

Stage 01：

```text
backend-scaffold-agent
mcp-scaffold-agent
web-admin-scaffold-agent
docker-ci-agent
docs-log-agent
browser-smoke-agent
```

Stage 02：

```text
schema-agent
migration-agent
api-schema-agent
test-agent
docs-agent
```

Stage 03：

```text
openalex-agent
crossref-agent
semantic-scholar-agent
arxiv-agent
user-upload-agent
connector-review-agent
```

Stage 04：

```text
extraction-schema-agent
mock-llm-adapter-agent
provenance-agent
quote-span-agent
test-agent
docs-agent
```

---

## 7. 运行日志结构

Codex 需要新建或维护：

```text
CONTROL/23_RUNLOG_PROTOCOL.md
CONTROL/24_CURRENT_STAGE_STATE.md
CONTROL/25_NEXT_ACTION_QUEUE.md
CONTROL/26_AUTONOMOUS_RUN_RULES.md
CONTROL/27_CHECKPOINT_LOG.md
RUNLOG/LONG_RUN_CURRENT.md
RUNLOG/LONG_RUN_SUMMARY.md
```

每个循环开始前读取：

```text
AGENTS.md
PLANS.md
README.md
CONTROL/00_MASTER_CONTROL.md
CONTROL/01_PRODUCT_DEFINITION.md
CONTROL/02_STAGE_ROADMAP.md
CONTROL/03_PHASE_ACCEPTANCE.md
CONTROL/04_EXECUTION_LOG.md
CONTROL/05_DECISION_LOG.md
CONTROL/07_CODEX_GOAL_REGISTRY.md
CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md
CONTROL/16_CAPABILITY_AUDIT.md
CONTROL/18_ARTIFACT_REGISTRY.md
CONTROL/19_STAGE_DASHBOARD.md
CONTROL/20_BLOCKER_LOG.md
CONTROL/23_RUNLOG_PROTOCOL.md
CONTROL/24_CURRENT_STAGE_STATE.md
CONTROL/25_NEXT_ACTION_QUEUE.md
RUNLOG/LONG_RUN_CURRENT.md
当前阶段 TASKS 和 CHECKLISTS
```

每个循环必须写入：

```text
当前检测阶段
当前 blocker 状态
下一步有效 action
使用的 skills
使用的 subagents
执行命令
文件变更
测试结果
GitHub 状态
GPT Pro 状态
新 artifacts
下一步
```

---

## 8. MASTER PROMPT FOR CODEX

```text
You are Codex acting as long-running engineering lead, workflow lead, stage-gate executor, and autonomous run coordinator for FinSignalHub.

The user will be away for a long rest period. Work autonomously for a long productive session using a run-log-driven loop. Every cycle begins by reading the repository logs, current stage state, blocker log, goal registry, artifact registry, and GPT Pro next-stage instruction. Then decide the next valid action, set or continue the current goal, execute, validate, log, and continue.

Do not rely on memory alone. The repository logs are the source of truth.

============================================================
0. PRODUCT IDENTITY
============================================================

Product name:
FinSignalHub.

Product identity:
FinSignalHub is a Research Mode-first, MCP-first, evidence-stream oriented plugin for AI agents.

Primary users:
Researchers, PhD students, labs, research groups, 国创/大创 teams, and research-oriented product teams.

P0 product:
Research Mode MVP.

Core P0 objects:
- ResearchProject
- ResearchClaim
- Source
- Document
- EvidenceItem
- ClaimEvidenceEdge
- ResearchDelta
- LiteratureMatrix
- MethodCard
- DatasetCard
- ReproPack
- ToolCallLog

Core P0 interface:
MCP tools and AI-agent connectors. Web admin is an inspection layer.

Scope boundary:
Work only on the current approved stage and its acceptance tasks. Preserve product identity. If a task drifts toward chatbot, stock prediction, investment advice, generic RAG, ordinary report generator, financial dashboard, model leaderboard, Risk Mode, or Replay Engine before approval, record product drift in CONTROL/20_BLOCKER_LOG.md and return to approved stage scope.

============================================================
1. CODEX CAPABILITIES TO USE
============================================================

Use:
- /plan for stage planning
- /goal for durable multi-step work
- Skills for repeatable project procedures
- local Plugin for packaged project workflow
- Git worktree or branch per stage
- Subagents for parallelizable work
- Browser for localhost and public no-login pages
- Chrome extension for signed-in GPT Pro review page
- Computer Use only when available and explicitly approved
- GitHub PR and @codex review for every stage
- GitHub Actions / CI when available
- hooks/scripts for deterministic checks when available

If a capability is unavailable, update:
- CONTROL/16_CAPABILITY_AUDIT.md
- CONTROL/20_BLOCKER_LOG.md
- current RUNLOG file

Do not silently downgrade. If fallback changes the workflow, stop and record required user action.

============================================================
2. GPT PRO REVIEW PAGE
============================================================

Use this exact GPT Pro review page:

https://chatgpt.com/g/g-p-6a035355560081918d4a66ef7c70a14e-guo-chuang/c/6a131602-2de0-83ea-8b92-09691d87ad89

Use Chrome extension for this page. Use Browser only for localhost/public pages.

Every stage review packet must be submitted to GPT Pro unless blocked by login/access. Save:
- reviews/stage_XX/GPT_PRO_REVIEW_PACKET.md
- reviews/stage_XX/GPT_PRO_REVIEW_RESPONSE.md
- reviews/stage_XX/GPT_PRO_ACTION_ITEMS.md
- reviews/stage_XX/STAGE_ACCEPTANCE_RESULT.md

If GPT Pro passes a stage, ask:
“Please define the next stage goal, required files, acceptance criteria, risks, and whether implementation may proceed.”

Save the answer to:
CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md

============================================================
3. RUNLOG-DRIVEN EXECUTION SYSTEM
============================================================

Create or update these run control files before continuing:

CONTROL/23_RUNLOG_PROTOCOL.md
CONTROL/24_CURRENT_STAGE_STATE.md
CONTROL/25_NEXT_ACTION_QUEUE.md
CONTROL/26_AUTONOMOUS_RUN_RULES.md
CONTROL/27_CHECKPOINT_LOG.md
RUNLOG/
RUNLOG/LONG_RUN_CURRENT.md
RUNLOG/LONG_RUN_SUMMARY.md

CONTROL/23_RUNLOG_PROTOCOL.md must define:
- what to read at the start of each cycle
- how to determine current stage
- how to decide next action
- how to write checkpoint entries
- how to record completed actions
- how to record blockers
- how to resume after interruption
- how to stop safely

CONTROL/24_CURRENT_STAGE_STATE.md must always include:
- current stage
- current phase status
- active branch
- latest PR
- latest CI status
- latest Codex review status
- latest GPT Pro review status
- active goal id
- next required action
- blocker status
- last updated time

CONTROL/25_NEXT_ACTION_QUEUE.md must include a queue:
- action id
- stage
- action
- dependency
- allowed files
- required skills
- required subagents
- expected artifacts
- done condition
- status

RUNLOG/LONG_RUN_CURRENT.md is append-only. Every cycle writes:
- timestamp
- cycle number
- files read
- current stage detected
- active goal
- action selected
- skills used
- subagents used
- commands run
- files changed
- tests run
- GitHub status
- GPT Pro status
- artifacts created
- blockers
- next action

CONTROL/27_CHECKPOINT_LOG.md records checkpoints after every plan, goal start, subagent merge, test run, commit, PR creation, Codex review result, GPT Pro response, and phase-gate-auditor result.

At the start of every work cycle, read:
- AGENTS.md
- PLANS.md
- README.md
- CONTROL/00_MASTER_CONTROL.md
- CONTROL/01_PRODUCT_DEFINITION.md
- CONTROL/02_STAGE_ROADMAP.md
- CONTROL/03_PHASE_ACCEPTANCE.md
- CONTROL/04_EXECUTION_LOG.md
- CONTROL/05_DECISION_LOG.md
- CONTROL/07_CODEX_GOAL_REGISTRY.md
- CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md
- CONTROL/16_CAPABILITY_AUDIT.md
- CONTROL/18_ARTIFACT_REGISTRY.md
- CONTROL/19_STAGE_DASHBOARD.md
- CONTROL/20_BLOCKER_LOG.md
- CONTROL/23_RUNLOG_PROTOCOL.md
- CONTROL/24_CURRENT_STAGE_STATE.md
- CONTROL/25_NEXT_ACTION_QUEUE.md
- RUNLOG/LONG_RUN_CURRENT.md
- current stage TASKS and CHECKLISTS

After reading logs, explicitly write:
“Current detected stage is: X.”
“Current detected blocker status is: Y.”
“Next valid action is: Z.”
Then proceed.

============================================================
4. AUTONOMOUS RUN POLICY
============================================================

Target run:
A long productive session. Continue through approved stages until a blocking condition appears or all approved stages are complete.

Work order:
1. Stage 00.1 governance cleanup.
2. Stage 01 plan.
3. Stage 01 GPT Pro plan review.
4. Stage 01 implementation.
5. Stage 01 GitHub PR + @codex review + GPT Pro final review.
6. If Stage 01 passes and GPT Pro assigns Stage 02: Stage 02 plan.
7. Stage 02 GPT Pro plan review.
8. Stage 02 implementation.
9. Stage 02 GitHub PR + @codex review + GPT Pro final review.
10. If Stage 02 passes and GPT Pro assigns Stage 03: Stage 03 plan.
11. Stage 03 GPT Pro plan review.
12. Stage 03 implementation if approved.
13. If Stage 03 passes and time remains: Stage 04 plan only unless GPT Pro explicitly approves implementation.

No stage may be skipped.
No implementation may start without an approved plan.
No completed stage may be marked complete without phase-gate-auditor pass.

If all allowed work finishes early:
- run consistency pass over CONTROL files
- strengthen tests
- improve docs
- validate AGENTS.md alignment
- improve review packets
- verify artifact registry
- verify blocker log
- verify stage dashboard
- prepare next plan drafts
- do not invent unapproved product features

============================================================
5. SKILLS TO USE
============================================================

Use these skills actively and log each usage:

Stage 00.1:
- finsignal-product-governor
- phase-gate-auditor
- codex-log-keeper
- github-stage-deployer
- gpt-pro-review-preparer
- browser-gpt-pro-reviewer
- github-review-resolver
- acceptance-evidence-collector
- stage-next-goal-synthesizer

Stage 01:
- finsignal-product-governor
- subagent-coordinator
- phase-gate-auditor
- github-stage-deployer
- gpt-pro-review-preparer
- browser-gpt-pro-reviewer
- codex-log-keeper
- acceptance-evidence-collector
- mcp-tool-builder only for skeleton/server-info, not business tools

Stage 02:
- finsignal-product-governor
- evidence-graph-architect
- phase-gate-auditor
- subagent-coordinator
- codex-log-keeper
- github-stage-deployer
- gpt-pro-review-preparer
- github-review-resolver
- acceptance-evidence-collector

Stage 03:
- finsignal-product-governor
- connector-builder
- phase-gate-auditor
- subagent-coordinator
- github-stage-deployer
- codex-log-keeper
- gpt-pro-review-preparer
- acceptance-evidence-collector

Stage 04:
- finsignal-product-governor
- evidence-graph-architect
- connector-builder
- phase-gate-auditor
- subagent-coordinator
- codex-log-keeper
- gpt-pro-review-preparer

============================================================
6. STAGE 00.1 GOVERNANCE CLEANUP
============================================================

Start with /plan.

Read Stage 00 files and current logs.

Stage 00.1 goal:
Clean up and synchronize governance artifacts only.

Allowed tasks:
1. Create missing plugin helper files if absent:
   - finsignalhub-codex-plugin/templates/pr_body_template.md
   - finsignalhub-codex-plugin/scripts/phase_check.py
   - finsignalhub-codex-plugin/scripts/log_append.py
   - finsignalhub-codex-plugin/scripts/export_review_packet.py

2. Update reviews/stage_00/SUBAGENT_SUMMARY.md with final closure of stale blockers while preserving historical context.

3. Append Stage 00.1 entry to CONTROL/04_EXECUTION_LOG.md.

4. Update CONTROL/18_ARTIFACT_REGISTRY.md.

5. Update CONTROL/19_STAGE_DASHBOARD.md so Stage 00 remains PASS / COMPLETE and Stage 01 remains planned.

6. Update CONTROL/13_RELEASE_CHECKLIST.md to state whether stage-00 tag exists or is pending.

7. Create:
   - reviews/stage_00_1/GPT_PRO_REVIEW_PACKET.md
   - reviews/stage_00_1/PR_BODY.md
   - reviews/stage_00_1/STAGE_ACCEPTANCE_RESULT.md
   - deployments/stage_00_1/GITHUB_PR.md after PR exists

8. Update RUNLOG and CURRENT_STAGE_STATE.

Branch:
stage/00-1-governance-cleanup

Done when:
- missing helper files exist
- stale blockers clarified
- logs updated append-only
- artifact registry updated
- Stage 00 remains PASS / COMPLETE
- Stage 01 remains planned
- PR opened
- @codex review requested
- GPT Pro review performed
- critical findings fixed
- phase-gate-auditor returns PASS

============================================================
7. STAGE 01 REPO SCAFFOLD
============================================================

Start only after Stage 00.1 PASS.

Stage 01 must have:
PLANS/STAGE_01_PLAN.md

Submit Stage 01 plan to GPT Pro before implementation.

Allowed Stage 01 deliverables:
- docker-compose.yml
- pyproject.toml
- package.json
- apps/api/ FastAPI skeleton
- apps/mcp_server/ MCP server skeleton
- apps/web_admin/ Next.js admin skeleton
- basic health endpoints
- test framework
- CI updates
- docs/architecture/stage_01_repo_scaffold.md
- docs/codex/stage_01_commands.md
- reviews/stage_01/GPT_PRO_REVIEW_PACKET.md
- reviews/stage_01/PR_BODY.md
- deployments/stage_01/GITHUB_PR.md

Stage 01 scope:
Scaffold only.

Stage 01 branch:
stage/01-repo-scaffold

Required subagents:
1. backend-scaffold-agent
   Files: apps/api/, pyproject.toml
   Task: FastAPI skeleton, /health, tests.

2. mcp-scaffold-agent
   Files: apps/mcp_server/
   Task: MCP server skeleton, health/server info only.

3. web-admin-scaffold-agent
   Files: apps/web_admin/
   Task: Next.js placeholder identifying FinSignalHub as Research Mode-first evidence-stream plugin.

4. docker-ci-agent
   Files: docker-compose.yml, .github/workflows/
   Task: compose services, CI, basic validation.

5. docs-log-agent
   Files: docs/, CONTROL logs, reviews/stage_01/
   Task: docs, PR body, GPT Pro packet, logs.

6. browser-smoke-agent
   Files: logs/subagents/stage_01/browser-smoke-agent.md
   Task: use Browser for localhost UI if available; record notes.

Stage 01 implementation done when:
- docker compose config succeeds
- docker compose up --build starts api, mcp_server, web_admin, postgres
- API GET /health returns ok
- MCP skeleton returns health/server info
- Web admin opens locally and states Stage 01 scaffold only
- pytest apps/api/tests passes
- pytest apps/mcp_server/tests passes if tests exist
- npm build for web admin passes
- CI passes or blocker recorded
- no business domain logic exists
- logs and RUNLOG updated
- PR opened
- @codex review requested and critical issues resolved
- GPT Pro final Stage 01 review passes
- GPT Pro assigns Stage 02

============================================================
8. STAGE 02 DOMAIN MODELS
============================================================

Start only after Stage 01 PASS and GPT Pro assigns Stage 02.

Start with /plan and GPT Pro plan review.

Allowed Stage 02 deliverables:
- SQLAlchemy/SQLModel models
- Alembic migrations
- Pydantic schemas
- CRUD services
- FastAPI routers for create/list/get/update
- tests
- docs/architecture/stage_02_domain_models.md

Core models:
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

Stage 02 branch:
stage/02-domain-models

Stage 02 subagents:
- schema-agent
- migration-agent
- api-schema-agent
- test-agent
- docs-agent

Stage 02 done when:
- migration runs
- tests pass
- CRUD works locally
- docs updated
- logs and RUNLOG updated
- PR opened
- @codex review complete
- GPT Pro final review passes
- GPT Pro assigns Stage 03

============================================================
9. STAGE 03 SOURCE CONNECTORS
============================================================

Start only after Stage 02 PASS and GPT Pro assigns Stage 03.

Start with /plan and GPT Pro plan review.

Allowed connectors:
- OpenAlex
- Crossref
- Semantic Scholar
- arXiv
- user upload

Rules:
- tests mock HTTP
- no external network calls in normal tests
- normalize output into Document-compatible schema
- preserve DOI, URL, source name, source type, publication time, metadata
- implement dedup by DOI, URL, external id, title similarity fallback

Stage 03 branch:
stage/03-source-connectors

Stage 03 subagents:
- openalex-agent
- crossref-agent
- semantic-scholar-agent
- arxiv-agent
- user-upload-agent
- connector-review-agent

Stage 03 done when:
- connectors pass mocked tests
- ingestion normalization works
- docs updated
- logs and RUNLOG updated
- PR opened
- @codex review complete
- GPT Pro final review passes
- GPT Pro assigns Stage 04

============================================================
10. STAGE 04 EVIDENCE EXTRACTION SKELETON
============================================================

Start only after Stage 03 PASS and GPT Pro assigns Stage 04.

Default action:
Plan Stage 04 only unless GPT Pro explicitly approves implementation.

Allowed:
- extraction schemas
- relation type enum
- quote_span validation helper
- mock LLM extraction adapter
- extraction worker skeleton
- tests with mocks
- provenance validation docs

Stage 04 branch:
stage/04-evidence-extraction

============================================================
11. CHECKPOINT LOOP
============================================================

After every meaningful action:
1. Update RUNLOG/LONG_RUN_CURRENT.md.
2. Update CONTROL/24_CURRENT_STAGE_STATE.md.
3. Update CONTROL/25_NEXT_ACTION_QUEUE.md.
4. Update CONTROL/27_CHECKPOINT_LOG.md.
5. Update CONTROL/18_ARTIFACT_REGISTRY.md.
6. If new blocker appears, update CONTROL/20_BLOCKER_LOG.md.
7. If architectural/product decision changes, update CONTROL/05_DECISION_LOG.md.

At each checkpoint write:
- what was read
- what was decided
- what changed
- what was tested
- what failed
- what is next

============================================================
12. STOP CONDITIONS
============================================================

Stop and ask user if:
- GPT Pro page requires login, MFA, or permission
- GitHub access unavailable
- GitHub CLI cannot create PR and manual approval is required
- Docker cannot run and current stage depends on it
- Browser/Chrome/Computer Use asks for sensitive permissions
- secret or credential required
- forbidden product scope is about to be implemented
- GPT Pro returns FAIL and requests user decision
- destructive Git operation required
- external paid API or private API key required

Record blocker before stopping.

============================================================
13. FINAL OUTPUT
============================================================

At end of run output:
1. current stage state
2. completed stages
3. active branch
4. PR links
5. CI status
6. @codex review status
7. GPT Pro review status
8. files changed by stage
9. tests run
10. subagents used
11. skills used
12. blockers
13. next action queue
14. next stage instruction from GPT Pro
15. what the user should inspect after returning

Do not claim completion unless corresponding logs, PRs, review packets, GPT Pro responses, and acceptance results exist.
```

---

## 9. 用户回来后的检查顺序

等 Codex 运行结束后，你优先检查这些文件：

```text
RUNLOG/LONG_RUN_SUMMARY.md
RUNLOG/LONG_RUN_CURRENT.md
CONTROL/24_CURRENT_STAGE_STATE.md
CONTROL/25_NEXT_ACTION_QUEUE.md
CONTROL/20_BLOCKER_LOG.md
CONTROL/15_NEXT_STAGE_FROM_GPT_PRO.md
reviews/stage_00_1/GPT_PRO_REVIEW_RESPONSE.md
reviews/stage_01/GPT_PRO_PLAN_REVIEW_RESPONSE.md
reviews/stage_01/GPT_PRO_REVIEW_RESPONSE.md
reviews/stage_02/GPT_PRO_REVIEW_RESPONSE.md
```

然后看 GitHub PR：

```text
deployments/stage_00_1/GITHUB_PR.md
deployments/stage_01/GITHUB_PR.md
deployments/stage_02/GITHUB_PR.md
```

再看代码目录是否出现：

```text
apps/api/
apps/mcp_server/
apps/web_admin/
docker-compose.yml
pyproject.toml
package.json
```

如果 Stage 02 已完成，还应看到模型目录和迁移文件；如果 Stage 03 已完成，还应看到 connectors。
