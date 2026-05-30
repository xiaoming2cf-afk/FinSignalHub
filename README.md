# FinSignalHub

FinSignalHub is a Research Mode-first, MCP-first, evidence-stream oriented plugin for scientific and financial research workflows.

The primary users are researchers, PhD students, labs, research project teams, innovation project teams, and research-oriented product teams. The main entrypoints are MCP tools, ChatGPT Apps, Claude/Copilot/Gemini connectors, and other AI Agent workflows. The core outputs are research delta, claim graph, evidence card, literature matrix, method card, dataset card, and repro pack.

Stage 00 status: governance/control system complete after GitHub PR, CI, Codex review, and GPT Pro final PASS confirmation.

Stage 01 status: scaffold-only implementation is accepted by GPT Pro after PR #7 current-head CI/Codex evidence. The repository now contains health-only API and MCP server scaffolds, an inspect-only web admin shell, and Docker Compose wiring. It still does not implement product runtime behavior, domain models, connectors, evidence extraction, claim graph, research delta, MCP business tools, dashboard behavior, report generation, stock recommendation, investment advice, or RAG features.

Stage 02 status: implementation is in progress after Stage 02 plan PASS, PR #8 current-head CI/Codex no-major evidence, and the user's direct approval to continue without repeated confirmation. The local implementation is limited to Research Mode domain model primitives, Alembic migration, Pydantic schemas, CRUD primitives, tests, and acceptance evidence. It still does not implement connectors, evidence extraction, claim graph computation, research delta computation engines, MCP business tools, product UI behavior, reports, stock recommendation, investment advice, or generic RAG.

See `AGENTS.md` before any future change.
