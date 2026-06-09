# FinSignalHub Computer Use Plugin Draft

This local-only plugin draft documents how FinSignalHub may use a callable Computer Use surface as a recovery route for GPT Pro stage reviews.

It is not a marketplace plugin, does not install a desktop automation runtime, and does not make Computer Use available in the current Codex session. Availability must still be verified through the active tool surface and recorded in `CONTROL/16_CAPABILITY_AUDIT.md`.

## Scope

- Govern GPT Pro review recovery after Chrome extension or background browser control fails.
- Preserve FinSignalHub's Research Mode-first, MCP-first, evidence-stream product boundaries.
- Prevent foreground interference while the user is working.
- Stop on login, MFA, captcha, permission, privacy, payment, subscription renewal, secret, or unclear consent prompts.
- Record response/action-item evidence only after GPT Pro actually answers.

## Non-Scope

- No business code.
- No FastAPI, database, frontend, connector, MCP tool, Claim Graph, Research Delta, Repro Pack, dashboard, chatbot, RAG, prediction, or investment feature.
- No password, token, API key, payment, or private browser-context capture.

## Files

- `.codex-plugin/plugin.json`: local plugin manifest.
- `.mcp.json`: intentionally empty MCP server declaration; Computer Use is a host capability, not a FinSignalHub MCP server.
- `templates/computer_use_review_runbook.md`: copy-ready runbook for safe GPT Pro review recovery.
- `scripts/README.md`: script policy; no automation script may send blind input to a browser.

## Use In Later Runs

Before using this plugin draft, a future Codex run must:

1. Confirm a callable Computer Use tool exists in the current session.
2. Confirm the active stage review packet is current.
3. Confirm GitHub Gate 6 has live PR head, CI, Codex, and review-thread evidence.
4. Use `computer-use-gpt-pro-reviewer` and stop on any unsafe page state.
5. Save GPT Pro response and action items before marking Gate 7 complete.
