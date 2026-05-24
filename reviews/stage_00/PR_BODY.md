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
- GPT Pro review completed with CONDITIONAL PASS and saved in `reviews/stage_00/GPT_PRO_REVIEW_RESPONSE.md`.
- `gh` remains unauthenticated persistently, but PR creation and owner-side `@codex review` comment were completed with a temporary Git Credential Manager token.
- The GitHub plugin also posted the required `@codex review` comment as `lhy18613775`.
- Codex review executed and returned one P1 and two P2 governance findings.
- Codex review fixes update `phase-deploy.yml`, `ci.yml`, and the Stage 00 GPT Pro review packet.
- Docker daemon unavailable or permission required.

## Acceptance checklist

Gate 6 GitHub remains BLOCKED until Codex follow-up review confirms the findings are resolved or only explicitly deferred non-critical items remain. PR URL, CI pass, and Codex review evidence are saved. Gate 7 GPT Pro has CONDITIONAL PASS. Stage 00 must not be marked full PASS before Codex review resolution evidence is complete.
