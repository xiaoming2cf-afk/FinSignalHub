# 10 Computer Browser Protocol

## Purpose

Defines safe use of Browser, Chrome extension, and Computer Use for FinSignalHub reviews.

## Owner

Browser workflow lead.

## When to update

Update when browser tooling, target GPT Pro page, login handling, or consent rules change.

## Required fields

- Tool
- Allowed use
- Forbidden actions
- Stop condition
- Log path
- Evidence path

## Example format

`Chrome extension | GPT Pro review | stop on login | log to CONTROL/04_EXECUTION_LOG.md`

## Current state

Routing:

- Public docs and local web checks: Browser.
- GPT Pro target page: Chrome extension first.
- Computer Use: only when available in the active tool surface and explicitly allowed by the current user instruction or stage protocol.
- Computer Use recovery must use `.agents/skills/computer-use-gpt-pro-reviewer/SKILL.md` and `finsignalhub-computer-use-plugin/` when Chrome extension or background browser control fails.

Forbidden:

- Passwords, verification codes, payment details, API keys, tokens, or secrets.
- Continuing through login, captcha, permission, payment, privacy, or unclear consent.
- Blind input into a browser whose page state has not been inspected.
- Foreground keyboard or mouse automation while the user is actively using Chrome.
- Committing screenshots or page captures that expose private browser context, account data, conversation URLs, tabs, or payment prompts.

Every browser action must be logged in `CONTROL/04_EXECUTION_LOG.md` with page, purpose, result, and saved evidence path.

Current Stage 05 note: creating a local Computer Use plugin draft does not prove Computer Use is callable. A stage may not mark GPT Pro Gate 7 complete unless GPT Pro response evidence is saved.
