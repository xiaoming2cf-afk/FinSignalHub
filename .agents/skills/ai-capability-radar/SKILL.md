---
name: ai-capability-radar
description: Audit local Codex, plugin, runtime, browser, GitHub, MCP, and GPT Pro capabilities.
---

# AI Capability Radar

## When to use

Use at the start of every stage and when a tool fallback may alter workflow.

## Procedure

1. Check required capabilities listed in `CONTROL/16_CAPABILITY_AUDIT.md`.
2. Record status, use, blocker, impact, fallback, and user authorization need.
3. Do not silently downgrade a required tool.
4. If fallback changes workflow, pause and ask the user.

## Required outputs

- Updated capability audit table.
- Blocker entries for unavailable or user-action capabilities.

## Failure conditions

- A missing capability is ignored.
- A fallback changes workflow without user awareness.
