# Stage 01 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | `PLANS/STAGE_01_PLAN.md`; forbidden-scope scan; product-scope subagent audit | pass locally |
| Functionality | `docker-compose.yml`; API `/health`; MCP `/health` and `/server-info`; web admin inspect-only page | pass locally |
| Tests | phase check, compose config, Python tests, web install/build/audit, compose up, endpoint smoke, browser/Chrome smoke | pass locally; CI pending after push |
| Docs | scaffold docs and package READMEs | pass locally |
| Logs | `CONTROL/04`, `CONTROL/07`, `CONTROL/18`, `CONTROL/19`, `CONTROL/20`, `CONTROL/24`, `CONTROL/25`, `CONTROL/27`, `RUNLOG/` | pass locally |
| GitHub | branch, PR, current-head CI, current-head `@codex review`, PR URL | blocked until implementation commit is pushed and PR #7 current head receives CI PASS and Codex no-major |
| GPT Pro | final implementation packet, response, action items, final result, next-stage instruction | blocked until GitHub current-head gate passes |
| Product governance | no product behavior, no Stage 02+ entities, no forbidden product direction | pass locally |
| Security | no secrets; Chrome/session artifacts removed; `.env.example` placeholders only; `.dockerignore` excludes local generated files | pass locally |
| Next stage | GPT Pro Stage 02 instruction after Stage 01 final PASS | blocked |

Stage 01 current state: local scaffold implementation checks passed. Final acceptance is blocked by the hard GitHub and GPT Pro gates for the new implementation head.
