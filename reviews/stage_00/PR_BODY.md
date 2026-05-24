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
- `gh` remains unauthenticated persistently, but PR creation and owner-side `@codex review` comment were completed with a temporary Git Credential Manager token.
- The GitHub plugin also posted the required `@codex review` comment as `lhy18613775`.
- Codex review executed, findings were fixed, and latest follow-up on commit `f0c1d70` found no major issues.
- Stage 00 final acceptance is PASS after GPT Pro final confirmation was saved.
- Docker daemon unavailable or permission required.

## Acceptance checklist

Gate 6 GitHub is PASS: branch, PR, CI, and Codex no-major-issues evidence are saved. Gate 7 GPT Pro is PASS: packet, response, action items, final result, and next-stage instruction are saved. Stage 00 is governance-only complete; Stage 01 must still start with a separate approved plan and goal.
