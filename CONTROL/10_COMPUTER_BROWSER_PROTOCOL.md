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
- Computer Use: only when available and explicitly approved.

Forbidden:

- Passwords, verification codes, payment details, API keys, tokens, or secrets.
- Continuing through login, captcha, permission, payment, privacy, or unclear consent.

Every browser action must be logged in `CONTROL/04_EXECUTION_LOG.md` with page, purpose, result, and saved evidence path.
