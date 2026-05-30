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
| Chrome extension | degraded / blocked for current Stage 03 GPT Pro plan review | GPT Pro page and Codex settings pages with login state | direct extension calls previously returned `native pipe is closed`; later backend selection and tab creation worked, but ChatGPT tab DOM/screenshot/page-evaluate/control timed out before safe background submission | GPT Pro Stage 03 plan review cannot be claimed through Chrome until page-state/control works and response can be saved | retry only with a materially different background route; stop on permission/account/login prompts | yes |
| Computer Use | unavailable as a standalone background tool in current tool surface | last-resort UI operation | official background Computer Use MCP surface is not exposed in this session; foreground pyautogui-style recovery would interfere with the user's active Chrome work | cannot use Computer Use to recover GPT Pro Stage 03 submission while the user is using foreground Chrome | use Chrome extension/background control only, or wait for user to provide an idle foreground window/background Computer Use surface | yes |
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
| GPT Pro page accessibility | available through off-screen Edge/CDP route; Chrome extension direct pipe degraded | blocking review gate | Chrome extension direct tab control returned `native pipe is closed` on 2026-05-29 and later timed out on ChatGPT page-state reads; the in-app Browser lacks the user's ChatGPT login state; standalone background Computer Use is not exposed. On 2026-05-30 an off-screen Microsoft Edge Default profile controlled through CDP opened the logged-in GPT Pro page and submitted the Stage 03 plan packet without entering secrets. | GPT Pro returned Stage 01 final PASS, Stage 02 plan PASS, Stage 02 final implementation PASS, and Stage 03 plan CONDITIONAL PASS. Stage 03 implementation remains blocked by B-0040. | Prefer safe background browser routes; use off-screen Edge/CDP for Stage 03 follow-up if still available; save response/action items/final result; avoid committing raw browser screenshots or clipboard captures that may include unrelated session context; stop on login/captcha/payment/permission prompts | yes |

## Stage 02 Implementation Addendum

| Capability | Status | Use in project | Blocker | Impact | Fallback | Requires user authorization |
| --- | --- | --- | --- | --- | --- | --- |
| GitHub Actions on PR #8 | available | Stage 02 GitHub gate | none for implementation-reviewed head `09585c58e71eb72b532ea42569d38dce2aa7b648` | CI passed before implementation and after CR-02-036 remediation; final documentation-only evidence commit still needs normal CI after push | rerun or inspect workflow logs if CI fails | no |
| PR `@codex review` on PR #8 | available | Stage 02 Codex gate | none for implementation-reviewed head `09585c58e71eb72b532ea42569d38dce2aa7b648` | Codex no-major received after CR-02-036 remediation at https://github.com/xiaoming2cf-afk/FinSignalHub/pull/8#issuecomment-4579603862 | CLI comment, minimal retry, GitHub route, then blocker if no response on future evidence commits | no |
| Docker/PostgreSQL for Stage 02 | available | Alembic/PostgreSQL migration validation | none observed | `docker compose config`, Postgres Alembic upgrade/downgrade/upgrade, and full Compose build/smoke passed locally on 2026-05-29 | rerun if CI or GPT Pro requests fresh DB evidence | no |
| GPT Pro final implementation page | available through safe visual recovery; direct Chrome extension pipe degraded | final Stage 02 hard gate | Chrome extension communication failed with `native pipe is closed`; Windows UI Automation was used against the already accessible Chrome page and no login/captcha/payment/permission/secret prompt appeared | Stage 02 final GPT Pro PASS saved; future GPT Pro reviews should still prefer Chrome extension first and switch to visual recovery after bounded retries | keep direct Chrome extension as preferred route; use safe visual route only when no secret/permission prompt appears | yes |

## Stage 02 CR-02-043 Background Operation Addendum

| Capability | status | use in project | blocker | impact | fallback | requires user authorization |
| --- | --- | --- | --- | --- | --- | --- |
| Chrome extension background tab route | degraded; usable for tab listing/fresh-tab open only | GPT Pro review without foreground Chrome control | Stage 03 GPT Pro tabs can be listed/created, but page-state reads, screenshots, page evaluation, and safe composer detection time out | cannot submit/capture GPT Pro Stage 03 response safely in the background | bounded retry only after a new signal, then record blocker or wait for a clean background route | no unless permission/login prompt appears |
| Standalone background Computer Use | unavailable in current tool surface | user-requested background visual recovery | tool discovery exposes browser-control APIs but no standalone background Computer Use; foreground screenshot/click tools would interfere with the user's active Chrome work | cannot satisfy a background-only Computer Use requirement through foreground UI automation | use Chrome extension/background control only, or wait for user to provide an idle foreground window/background Computer Use surface | yes for any foreground-only fallback |

## Stage 03 Chrome-Only Follow-Up Addendum

| Capability | status | use in project | blocker | impact | fallback | requires user authorization |
| --- | --- | --- | --- | --- | --- | --- |
| Chrome CDP off-screen route | requires user action | GPT Pro follow-up without foreground interaction | Chrome was launched off-screen with remote debugging on port `9337` and the specified GPT Pro URL, but the isolated profile redirected to `https://chatgpt.com/auth/login/?next=...`; Codex must not enter credentials, verification codes, payment data, API keys, tokens, or secrets | GPT Pro follow-up for Stage 03 cannot be completed through the Chrome-only background route; B-0040 remains open despite current-head GitHub/Codex PASS | use an authenticated background Chrome profile, a future standalone background Computer Use surface, or an idle foreground Chrome window; do not use Edge unless the latest Chrome-only instruction changes | yes |
| Current PR #9 GitHub/Codex gate | blocked by CR-03-010/011 | Stage 03 Gate 6 | blocker-evidence head `f9b2e3067d123dc915ffe2977cb448f3008b0294` passed CI, but Codex review `4395247885` returned P2 findings on Stage 03 subagent protocol clarity and stale GPT Pro follow-up packet evidence | Gate 6 cannot pass until the remediation is pushed, the new head passes CI, and Codex rechecks | run governance checks, push remediation, run CI, request Codex review, and record live-head evidence | no |
| Chrome extension logged-in profile route | degraded / unsafe for current task | GPT Pro follow-up using user's logged-in Chrome profile | Extension connects to logged-in `hengyuan` profile and can list/create/claim tabs, but ChatGPT page screenshot, DOM snapshot, locator, and evaluate calls timed out; a coordinate/keyboard CUA attempt was indeterminate and could not safely capture the response | GPT Pro follow-up cannot be completed or verified through this route without risking foreground interference or blind submission | stop CUA/keyboard attempts; wait for stable DOM route, standalone background Computer Use, or idle foreground approval | yes for foreground-only recovery |
| Chrome extension visible-DOM/clipboard route | blocked | GPT Pro follow-up using a different Chrome-only background method | Visible-DOM plus clipboard probe on the logged-in target tab timed out, and read-only port probes found no usable Chrome CDP listener on common local ports | This confirms the current blocker is not limited to Playwright selectors; GPT Pro follow-up still cannot be safely submitted or captured in background Chrome | do not repeat the same Chrome page-control class without a new signal; wait for stable Chrome background control or idle foreground window | yes for foreground-only recovery |
| Standalone background Computer Use for Stage 03 | unavailable | user-requested GPT Pro review recovery without disturbing foreground Chrome | tool discovery exposed no standalone background Computer Use API; available routes are Chrome extension/browser-control and unrelated app tools | Cannot satisfy the requested background Computer Use route or claim GPT Pro review completion through it | wait for a background Computer Use tool surface or an idle foreground window; do not substitute foreground automation or Edge while Chrome-only instruction stands | yes |
