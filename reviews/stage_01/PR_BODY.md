# Stage 01: Repo Scaffold

## Goal

Create the minimal scaffold-only monorepo foundation for FinSignalHub after Stage 01 plan, GitHub/Codex, user approval, Docker, and GPT Pro implementation-start gates.

## Product boundary

Stage 01 is not a business implementation stage. It does not implement Research Mode domain models, connectors, extraction, claim graph, research delta, MCP business tools, Repro Pack, Risk Mode, Replay Engine, stock prediction, investment advice, chatbot UI, generic RAG, or dashboard product behavior.

## Delivered

- `docker-compose.yml` with `postgres`, `api`, `mcp_server`, and `web_admin` scaffold services.
- `pyproject.toml` for health-only API/MCP Python scaffold and tests.
- `package.json` root command wrapper for web checks.
- `apps/api/` FastAPI `/health` only.
- `apps/mcp_server/` FastAPI `/health` and `/server-info` only, with `tools_enabled: false`.
- `apps/web_admin/` Next.js inspect-only status page.
- `.dockerignore`, `.gitignore`, package READMEs, Stage 01 architecture and command docs.
- CI expanded to run phase check, Python tests, web install/build/audit, compose config, and compose runtime smoke.
- Subagent audit summary and logs under `reviews/stage_01/SUBAGENT_SUMMARY.md` and `logs/subagents/stage_01/`.

## Local checks

Passed locally:

```powershell
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 01
docker compose config
python -m pip install -e ".[test]"
python -m pytest apps/api/tests apps/mcp_server/tests
npm --prefix apps/web_admin --workspaces=false ci
npm run web:build
npm run web:audit
docker compose up --build -d
curl.exe --fail --silent --show-error http://localhost:8000/health
curl.exe --fail --silent --show-error http://localhost:8001/health
curl.exe --fail --silent --show-error http://localhost:8001/server-info
curl.exe --fail --silent --show-error http://localhost:3000
```

## Review status

- Previous planning/current-head evidence: PR head `5bc977b398aaad007f06df3d895289249713830d` had CI PASS and Codex no-major response.
- This implementation update requires new current-head CI and Codex review.
- GPT Pro final implementation review is pending until current-head CI/Codex pass.

Required review comment:

`@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems`

## Blockers

- B-0015: current-head GitHub/Codex gate pending after push.
- B-0016: GPT Pro final implementation review pending after current-head GitHub/Codex pass.
