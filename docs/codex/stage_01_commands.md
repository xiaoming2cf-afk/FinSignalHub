# Stage 01 Commands

## Local Checks

```powershell
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 01
docker compose config
python -m pip install -e ".[test]"
python -m pytest apps/api/tests apps/mcp_server/tests
npm --prefix apps/web_admin --workspaces=false ci
npm run web:build
npm run web:audit
```

## Runtime Checks

After dependencies are installed and Docker is available:

```powershell
docker compose up --build
```

Health endpoints:

```powershell
curl.exe http://localhost:8000/health
curl.exe http://localhost:8001/health
curl.exe http://localhost:8001/server-info
```

## Stage Boundary

Do not add product endpoints, database models, connectors, extraction, claim graph, Research Delta, MCP business tools, Repro Pack logic, chatbot UI, stock recommendation, investment advice, generic RAG, or dashboard product behavior in Stage 01.
