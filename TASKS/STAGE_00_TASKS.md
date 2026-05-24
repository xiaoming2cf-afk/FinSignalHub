# Stage 00 Tasks: Control System And Capability Audit

## Stage goal

Create FinSignalHub governance, capability audit, local skills, local plugin draft, review packets, workflows, logs, and acceptance gates.

## User needs

Researchers need a controlled project system before product implementation so later evidence-stream work does not drift into chatbot, generic RAG, stock recommendation, dashboard, or report generation behavior.

## Files allowed

`CONTROL/`, `PLANS/`, `TASKS/`, `CHECKLISTS/`, `reviews/stage_00/`, `deployments/stage_00/`, `logs/`, `artifacts/`, `docs/`, `.agents/skills/`, `finsignalhub-codex-plugin/`, `.github/workflows/`, root governance files.

## Files forbidden

Backend, database, MCP server runtime, connectors, frontend app, admin UI, demo code, product models, and production scripts.

## Skills required

`ai-capability-radar`, `codex-log-keeper`, `phase-gate-auditor`, `finsignal-product-governor`, `gpt-pro-review-preparer`, `github-stage-deployer`, `browser-gpt-pro-reviewer`, `subagent-coordinator`.

## Subagents required

Use a bounded verification subagent when available. It may inspect files and report gaps but must not own broad repository changes.

## Implementation tasks

- Create required directories and purpose docs.
- Create root governance files.
- Create all `CONTROL` files with required sections.
- Create all skills and plugin draft files.
- Create Stage 00 review and deployment artifacts.
- Create CI and phase deploy workflow placeholders.

## Test tasks

- Check required files exist.
- Check `CONTROL` sections.
- Check skill sections and YAML frontmatter.
- Check plugin manifest fields.
- Check review artifacts and workflow files.

## Docs tasks

- Record Stage 00 status, roadmap, risks, protocols, and blockers.
- Ensure no blank placeholder file exists.

## GitHub deployment tasks

- If repo and auth exist, create branch, commit, push, PR, comment `@codex review`, wait for CI, summarize review.
- If blocked, write `deployments/stage_00/MANUAL_GITHUB_STEPS.md` and blocker entries.

## GPT Pro review tasks

- Generate copy-ready packet.
- Submit only through user-approved Chrome extension workflow.
- Save response, action items, final result, and next-stage instruction when available.
- If blocked, record blocker and leave Stage 00 not complete.

## Stop conditions

Stop on business implementation, product drift, secret entry, unsafe browser prompt, missing logs, missing GitHub evidence, or missing GPT Pro evidence.
