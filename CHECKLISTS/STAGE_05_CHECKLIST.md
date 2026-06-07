# Stage 05 Checklist

| Gate | Required evidence | Status |
| --- | --- | --- |
| Scope | Stage 05 planning files only; no runtime Claim Graph, Research Delta, MCP business tool, Repro Pack, UI/dashboard, chatbot/RAG, stock/investment, Risk Mode, Replay Engine, auth, billing, external provider, or real LLM behavior | PASS locally |
| Functionality | Planning defines future Claim Graph architecture, relation rules, same-project guards, Research Delta semantics, and mock-only test plan without implementation | PASS locally |
| Tests | `phase_check.py --stage 05`, `phase_check.py --stage 05 --final`, forbidden implementation path absence, forbidden-scope scan, secret scan, compileall, row-ID uniqueness, and `git diff --check` | PASS locally; GitHub CI pending |
| Docs | Stage 05 plan, tasks, architecture doc, command doc, review/deployment READMEs, and subagent logs exist | PASS locally |
| Logs | CONTROL and RUNLOG entries updated for Stage 04 complete and Stage 05 planning active | PASS locally |
| GitHub | Branch, PR, CI, Codex review, PR URL, unresolved-thread check | BLOCKED until PR is created and current head passes CI/Codex |
| GPT Pro | Review packet, response, action items, final result, next-stage instruction | BLOCKED until GitHub/Codex gate passes and GPT Pro review is submitted |
| Product governance | Stage 05 remains Research Mode evidence-stream planning only | PASS locally |
| Security | No secrets, no provider credentials, no real LLM calls, no live external calls | PASS locally |
| Next stage | GPT Pro must approve Stage 05 planning and provide implementation-goal requirements before any implementation begins | BLOCKED until GPT Pro plan review |

Current Stage 05 status: local planning checks passed on `stage/05-claim-graph-delta`. Stage 05 implementation remains unauthorized.
