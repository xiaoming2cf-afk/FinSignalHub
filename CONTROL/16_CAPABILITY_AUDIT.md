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
| Chrome extension | degraded / blocked for current Stage 02 final review | GPT Pro page and Codex settings pages with login state | direct extension calls returned `native pipe is closed` on 2026-05-29 even though Chrome is running, extension is installed/enabled in Profile 26, and native host manifest is correct | GPT Pro final review cannot be claimed through Chrome until extension communication is restored or a safe visual route is available | retry only after Chrome/plugin recovery; stop on permission/account prompts | yes |
| Computer Use | unavailable as a standalone tool in current tool surface | last-resort UI operation | official Computer Use MCP surface is not exposed in this session; Chrome tab CUA is unavailable while extension pipe is closed | cannot use Computer Use to recover GPT Pro submission in this run | restore Chrome extension or ask user to repair/reinstall Codex Chrome Extension from plugin UI if communication remains closed | yes |
| GitHub connection | available | repo, PR, review | repo exists and PR is open; GitHub plugin user differs from repo owner but PR workflow is functional | connector can comment/read and `gh` can perform authenticated CLI operations | record owner/account assumptions in stage PR logs | yes for owner-only browser actions |
| GitHub CLI | available | branch, push, PR | none after persistent login | `gh auth status` reports active account `xiaoming2cf-afk` with `repo,workflow` scopes; `lhy18613775` remains a non-active secondary login | none | no |
| GitHub Actions | available | CI gate | none for Stage 00 | governance CI passed on PR | none | no |
| PR `@codex review` | available | Codex review gate | current-head response can lag after comments, requiring bounded retry plus method switch | Stage 01 implementation head `f30a02e7fd891d578e0f6e54f858ed475a6d6881` received no-major response after required trigger, minimal retry, and GitHub plugin route | use CLI comment, minimal retry, GitHub plugin route, then blocker/replacement only if still unresolved | no |
| Subagents | available | independent Stage 00 completeness audit | must be spawned explicitly | improves verification | local self-check if unavailable | no |
| MCP | available as concept/tool ecosystem | primary future product entrypoint | no FinSignalHub MCP server in Stage 00 | runtime not implemented by design | Stage 06 plan | no |
| Local shell | available | checks and audits | none | supports verification | none | no |
| Docker | available for daemon, compose config, and local runtime smoke | Stage 01 scaffold runtime checks | daemon resolved on 2026-05-26: `docker info`, `docker version`, and `docker compose version` pass; `docker compose config` passed after the approved compose file was created; `docker compose up --build -d` and health smoke checks passed locally | Docker no longer blocks local Stage 01 scaffold verification | CI now includes compose config and runtime smoke; keep Docker artifacts out of committed runtime state | no |
| Python | available | future scripts/checks | none | can run verification scripts later | shell checks | no |
| Node.js | available | future admin/tooling | none | available for later stages | none | no |
| Package managers | partial | future JS tooling | `npm.ps1` blocked; `npm.cmd` works; pnpm/yarn unavailable | use `npm.cmd` on Windows | document command form | no |
| GPT Pro page accessibility | available through Chrome visual route; Chrome extension direct pipe degraded | blocking review gate | Chrome extension direct tab control returned `native pipe is closed` on 2026-05-29, but the specified GPT Pro page was accessible in Chrome and Windows UI Automation recovery submitted/captured the Stage 02 final review without secret entry | GPT Pro returned Stage 01 final PASS, Stage 02 plan PASS, and Stage 02 final implementation PASS; Stage 03 planning only is authorized | save response/action items/final result; avoid committing raw browser screenshots or clipboard captures that may include unrelated session context; stop on login/captcha/payment/permission prompts | yes |

## Stage 02 Implementation Addendum

| Capability | Status | Use in project | Blocker | Impact | Fallback | Requires user authorization |
| --- | --- | --- | --- | --- | --- | --- |
| GitHub Actions on PR #8 | available | Stage 02 GitHub gate | none for implementation-reviewed head `09585c58e71eb72b532ea42569d38dce2aa7b648` | CI passed before implementation and after CR-02-036 remediation; final documentation-only evidence commit still needs normal CI after push | rerun or inspect workflow logs if CI fails | no |
| PR `@codex review` on PR #8 | available | Stage 02 Codex gate | none for implementation-reviewed head `09585c58e71eb72b532ea42569d38dce2aa7b648` | Codex no-major received after CR-02-036 remediation at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4579603862 | CLI comment, minimal retry, GitHub route, then blocker if no response on future evidence commits | no |
| Docker/PostgreSQL for Stage 02 | available | Alembic/PostgreSQL migration validation | none observed | `docker compose config`, Postgres Alembic upgrade/downgrade/upgrade, and full Compose build/smoke passed locally on 2026-05-29 | rerun if CI or GPT Pro requests fresh DB evidence | no |
| GPT Pro final implementation page | available through safe visual recovery; direct Chrome extension pipe degraded | final Stage 02 hard gate | Chrome extension communication failed with `native pipe is closed`; Windows UI Automation was used against the already accessible Chrome page and no login/captcha/payment/permission/secret prompt appeared | Stage 02 final GPT Pro PASS saved; future GPT Pro reviews should still prefer Chrome extension first and switch to visual recovery after bounded retries | keep direct Chrome extension as preferred route; use safe visual route only when no secret/permission prompt appears | yes |
