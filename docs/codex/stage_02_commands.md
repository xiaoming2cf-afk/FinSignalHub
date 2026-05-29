# Stage 02 Commands

Use these commands for Stage 02 implementation verification.

## Latest Verified Results

Verified on 2026-05-29 after CR-02-030/031 local remediation.

| Check | Result |
| --- | --- |
| `python -m pytest apps/api/tests` | PASS, 42 tests |
| `python -m pytest apps/api/tests/test_stage02_crud_routes.py -q` | PASS, 28 targeted route tests after CR-02-030/031 |
| `python -m pytest apps/api/tests/test_stage02_models.py -q` | PASS, 5 model tests after CR-02-030 |
| `python -m pytest apps/mcp_server/tests` | PASS, 2 tests |
| `python -m compileall apps/api/finsignalhub_api` | PASS |
| `python -m compileall apps/mcp_server/finsignalhub_mcp_server` | PASS |
| `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02` | PASS |
| `npm.cmd run web:build` | PASS |
| `npm.cmd run web:audit` | PASS, 0 vulnerabilities |
| `docker compose config` | PASS |
| `docker compose up -d postgres` plus Alembic upgrade/downgrade/upgrade | PASS |
| `docker compose up --build -d` plus API/MCP/web smoke | PASS |
| likely-secret scan | PASS, no matches |
| runtime forbidden-scope scan | PASS; only expected guard-test strings in `apps/api/tests/test_stage02_forbidden_scope.py` |
| artifact ID uniqueness check | PASS |
| `git diff --check` | PASS; only line-ending warnings from Git on Windows |

## Local Python Checks

```powershell
python -m pip install -e ".[test]"
python -m pytest apps/api/tests
python -m pytest apps/mcp_server/tests
python -m compileall apps/api/finsignalhub_api
python -m compileall apps/mcp_server/finsignalhub_mcp_server
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 02
git diff --check
```

## Docker And Migration Checks

```powershell
docker compose config
docker compose up -d postgres
$env:FINSIGNALHUB_DATABASE_URL="postgresql+psycopg://finsignalhub:finsignalhub_dev_password_placeholder@localhost:5432/finsignalhub_dev"
python -m alembic -c apps/api/alembic.ini upgrade head
python -m alembic -c apps/api/alembic.ini downgrade -1
python -m alembic -c apps/api/alembic.ini upgrade head
docker compose down
```

## Scope Checks

Stage 02 must not add:

- connectors;
- external API clients;
- LLM adapters;
- evidence extraction pipelines;
- claim graph computation;
- research delta computation engines;
- Repro Pack export logic;
- MCP business tools;
- chatbot, generic RAG, stock prediction, investment advice, dashboard behavior, Risk Mode, or Replay Engine.

The runtime forbidden-scope test lives in `apps/api/tests/test_stage02_forbidden_scope.py`.
