# 16 Capability Audit

## Purpose

Records Codex, plugin, browser, GitHub, runtime, MCP, and GPT Pro capability status.

## Owner

AI capability radar.

## When to update

Update at the start of every stage, after tool discovery, and whenever a fallback changes the workflow.

## Required fields

- Capability
- Status
- Use in project
- Blocker
- Impact
- Fallback
- Requires user authorization

## Example format

`GitHub CLI | requires user action | push PR | gh not logged in | Gate 6 blocked | manual steps | yes`

## Current state

| Capability | Status | Use in project | Blocker | Impact | Fallback | Requires user authorization |
| --- | --- | --- | --- | --- | --- | --- |
| Plan mode | available | create approved plans | none | enables stage protocol | none | no |
| Goal mode | available | execute approved goals | current mode supports execution | enables implementation | none | no |
| Skills | available | local governance skills | project skills not loaded until created | must create Stage 00 skills | create `.agents/skills` | no |
| Plugins | available | Browser, Chrome, GitHub, OpenAI Developers, Codex Security, Render audit context | Render deployment not in Stage 00 scope | external deployment not used | record as not applicable | no |
| Local plugin install/share | unknown | package local skills | no install performed | local-only draft cannot be assumed shared | document manual local use | yes if sharing |
| In-app Browser | available | public/local web checks | none observed | can inspect non-login pages | Chrome extension for login pages | no for public pages |
| Chrome extension | available | GPT Pro page and Codex settings pages with login state | none for GPT Pro after successful submission; Codex settings showed no environment creation action safe for automation | GPT Pro review completed; Codex environment remains user-action blocker | use only with user approval and stop on permission/account prompts | yes |
| Computer Use | unknown | last-resort UI operation | standalone availability not confirmed | cannot rely on it | Browser or manual user action | yes |
| GitHub connection | partial | repo, PR, review | repo exists and PR is open, but GitHub plugin user differs from repo owner | connector can comment/read, but cannot fully administer repo | use repo owner browser/GCM session for owner actions; plugin for audit/comment | yes for owner-only actions |
| GitHub CLI | requires user action | branch, push, PR | `gh` not persistently authenticated; temporary Git Credential Manager token worked for PR actions | future CLI actions may fail after credential expiry | user completes `gh auth login`; keep manual steps | yes |
| GitHub Actions | available | CI gate | none for Stage 00 | governance CI passed on PR | none | no |
| PR `@codex review` | requires user action | Codex review gate | required comments posted, but Codex connector requires a Codex environment for this repo; settings are connected to `lhy18613775` while repo owner is `xiaoming2cf-afk` | Gate 6 remains blocked until actual findings are produced | repo owner or authorized connected user creates Codex environment, then rerun `@codex review` | yes |
| Subagents | available | independent Stage 00 completeness audit | must be spawned explicitly | improves verification | local self-check if unavailable | no |
| MCP | available as concept/tool ecosystem | primary future product entrypoint | no FinSignalHub MCP server in Stage 00 | runtime not implemented by design | Stage 06 plan | no |
| Local shell | available | checks and audits | none | supports verification | none | no |
| Docker | requires user action | future Stage 01 compose | daemon unavailable | cannot verify Docker runtime | record blocker; retry after Docker starts | yes |
| Python | available | future scripts/checks | none | can run verification scripts later | shell checks | no |
| Node.js | available | future admin/tooling | none | available for later stages | none | no |
| Package managers | partial | future JS tooling | `npm.ps1` blocked; `npm.cmd` works; pnpm/yarn unavailable | use `npm.cmd` on Windows | document command form | no |
| GPT Pro page accessibility | available after user instruction | blocking review gate | GitHub still blocks full stage pass | GPT Pro returned CONDITIONAL PASS | saved response and action items | yes |
