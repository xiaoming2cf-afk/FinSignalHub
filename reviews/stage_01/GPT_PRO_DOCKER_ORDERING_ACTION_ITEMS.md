# Stage 01 GPT Pro Docker Ordering Action Items

## Must Fix Before Implementation

| ID | Action | Owner | Status |
| --- | --- | --- | --- |
| GPT-DOCKER-001 | Split Docker readiness into environment, implementation-preflight, and full runtime gates | codex-log-keeper | done locally; current head needs CI/Codex after push |
| GPT-DOCKER-002 | Treat `docker compose config` as implementation-preflight, not pre-implementation | phase-gate-auditor | done locally; current head needs CI/Codex after push |
| GPT-DOCKER-003 | Do not create `docker-compose.yml` until explicit Stage 01 implementation approval exists | Codex | active rule |
| GPT-DOCKER-004 | First Stage 01 implementation step must create minimal `docker-compose.yml` and immediately run `docker compose config` | docker-ci-agent | pending implementation approval |
| GPT-DOCKER-005 | If `docker compose config` fails, stop implementation, record blocker, and do not create further scaffold | docker-ci-agent | pending implementation approval |
| GPT-DOCKER-006 | Resolve or log PR #6 baseline dependency before implementation | github-stage-deployer | pending |
| GPT-DOCKER-007 | Obtain explicit user approval for Stage 01 implementation | user/Codex | pending |

## Deferred

| ID | Item | Deferred to |
| --- | --- | --- |
| GPT-DOCKER-D001 | `docker compose up --build` | Stage 01 final runtime validation after compose config passes |
| GPT-DOCKER-D002 | API `/health`, MCP health/server-info, web admin smoke | Stage 01 final runtime validation |
| GPT-DOCKER-D003 | Deeper coverage, type, and security gates | Stage 02 or Stage 03 unless Stage 01 plan is amended |

## Stop Condition

Stage 01 implementation remains `BLOCKED` until user implementation approval, PR #6 baseline handling, Docker environment readiness, and the Docker gate wording update are complete. After approval, if the implementation-preflight `docker compose config` fails, stop immediately and log a blocker.
