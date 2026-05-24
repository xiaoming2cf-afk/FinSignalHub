# Stage 00: Control System

## Goal

Create the FinSignalHub project operating system before business implementation.

## Product identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. Stage 00 implements governance only.

## Deliverables

- Control files under `CONTROL/`.
- Approved plan and global plan/goal templates.
- Stage tasks and checklists.
- Local FinSignalHub skills.
- Local Codex plugin draft.
- GitHub deployment and GPT Pro review protocols.
- Stage 00 review packet and phase acceptance result.
- Minimal governance CI workflows.

## Checks

Local file-structure checks must verify required files, control headings, skill sections, plugin manifest fields, and workflows.

## Capability audit status

Current status:

- Local Git repository exists.
- Remote repository exists: `https://github.com/xiaoming2cf-afk/FinSignalHub.git`.
- Branches pushed: `main` and `stage/00-control-system`.
- GPT Pro initial review completed with CONDITIONAL PASS and final confirmation returned PASS for Stage 00 / prompt 1.
- `gh` persistent authentication is now available for active account `xiaoming2cf-afk` with `repo,workflow` scopes.
- A separate GitHub connector/plugin account, `lhy18613775`, posted one retry `@codex review` comment; it is not the active GitHub CLI account.
- Codex review executed, findings were fixed, and latest follow-up on commit `f0c1d70` found no major issues.
- Stage 00 final acceptance is PASS after GPT Pro final confirmation was saved.
- Docker daemon is now available: Docker Server 29.3.1 on context `docker-desktop`.

## Acceptance checklist

Gate 6 GitHub is PASS: branch, PR, CI, and Codex no-major-issues evidence are saved. Gate 7 GPT Pro is PASS: packet, response, action items, final result, and next-stage instruction are saved. Stage 00 is governance-only complete; Stage 01 must still start with a separate approved plan and goal.

## Post-acceptance capability update

This PR records that two deferred local-environment blockers have been resolved after Stage 00 acceptance:

- GitHub CLI persistent login is available.
- Docker Desktop daemon is available.
- Codex review on PR #2 found one provenance clarity issue about account identity; this branch now reconciles the active CLI account evidence.

No product runtime, backend, database, connector, frontend, or MCP business tool is introduced.
