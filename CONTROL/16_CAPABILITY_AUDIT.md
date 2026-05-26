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
| Chrome extension | available | GPT Pro page and Codex settings pages with login state | none for GPT Pro after successful final confirmation | GPT Pro review and final confirmation completed | use only with user approval and stop on permission/account prompts | yes |
| Computer Use | unknown | last-resort UI operation | standalone availability not confirmed | cannot rely on it | Browser or manual user action | yes |
| GitHub connection | available | repo, PR, review | repo exists and PR is open; GitHub plugin user differs from repo owner but PR workflow is functional | connector can comment/read and `gh` can perform authenticated CLI operations | record owner/account assumptions in stage PR logs | yes for owner-only browser actions |
| GitHub CLI | available | branch, push, PR | none after persistent login | `gh auth status` reports active account `xiaoming2cf-afk` with `repo,workflow` scopes; `lhy18613775` remains a non-active secondary login | none | no |
| GitHub Actions | available | CI gate | none for Stage 00 | governance CI passed on PR | none | no |
| PR `@codex review` | available | Codex review gate | Stage 00 and Stage 00.1 findings were fixed; latest PR #6 follow-up found no major issues | Gate 6 satisfied for Stage 00.1 on commit `43c570a1291b262faba32f288b29b0dfbf396029` | none | no |
| Subagents | available | independent Stage 00 completeness audit | must be spawned explicitly | improves verification | local self-check if unavailable | no |
| MCP | available as concept/tool ecosystem | primary future product entrypoint | no FinSignalHub MCP server in Stage 00 | runtime not implemented by design | Stage 06 plan | no |
| Local shell | available | checks and audits | none | supports verification | none | no |
| Docker | requires user action | future Stage 01 compose | Docker CLI exists, but daemon is not reachable at `npipe:////./pipe/dockerDesktopLinuxEngine` | Stage 01 implementation is blocked until Docker Desktop is running and revalidated; Stage 00.1 is not blocked | rerun Docker-specific tests before Stage 01 implementation | yes |
| Python | available | future scripts/checks | none | can run verification scripts later | shell checks | no |
| Node.js | available | future admin/tooling | none | available for later stages | none | no |
| Package managers | partial | future JS tooling | `npm.ps1` blocked; `npm.cmd` works; pnpm/yarn unavailable | use `npm.cmd` on Windows | document command form | no |
| GPT Pro page accessibility | available after user instruction | blocking review gate | none for Stage 00.1 after Chrome submission | GPT Pro returned Stage 00.1 PASS and authorized Stage 01 planning only | saved response, action items, final acceptance, and next-stage instruction | yes |
