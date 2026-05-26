# MCP Server Package

This package contains the Stage 01 MCP server-info scaffold.

Allowed in Stage 01:

- `/health` for service readiness;
- `/server-info` for scaffold metadata;
- explicit `tools_enabled: false` and empty allowed output declarations.

Forbidden until Stage 06 or another approved stage:

- MCP business tools;
- tool schemas for research workflows;
- evidence extraction;
- claim graph, Research Delta, Repro Pack, connector, chatbot, RAG, dashboard, prediction, or investment behavior.
