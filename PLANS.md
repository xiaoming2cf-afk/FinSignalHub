# FinSignalHub Plan And Goal Templates

## Required `/plan` Template

Each stage plan must include:

- Context read: control files, `AGENTS.md`, `PLANS.md`, previous GPT Pro instruction.
- Capability check: tools, plugins, browser, GitHub, MCP, shell, runtimes.
- Product alignment check: mapping to Research Mode-first, MCP-first, evidence-stream value.
- Scope: stage goal and explicit non-goals.
- Files to create or modify.
- Files not to touch.
- Skills.
- Subagents.
- Implementation steps.
- Tests.
- Docs.
- GitHub deployment.
- GPT Pro review.
- Risks.
- Stop conditions.

## Required `/goal` Template

Each stage goal must include:

- Stage id.
- Approved plan path.
- Done-when.
- Commands to run.
- Logs to update.
- Review artifacts to create.
- GitHub deployment actions.
- GPT Pro review actions.
- Phase gate requirements.

## Enforcement

If a future stage does not use these templates, `phase-gate-auditor` must return FAIL or BLOCKED.
