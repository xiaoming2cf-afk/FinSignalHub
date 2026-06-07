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
| Chrome extension | available for Stage 03 GPT Pro follow-up and CR-03-043 re-review through logged-in DOM route | GPT Pro page and Codex settings pages with login state | Earlier extension routes returned `native pipe is closed` or timed out on screenshot/page-state calls, but the logged-in Chrome extension DOM route later submitted Stage 03 follow-up, implementation-goal, final implementation, and CR-03-043 re-review packets without entering secrets or credentials. | Stage 03 GPT Pro review evidence can be claimed from saved response/action files; future reviews still require readable DOM and no login/permission/secret prompt. | Use the successful DOM route when stable; otherwise record a blocker or wait for standalone background Computer Use instead of using foreground automation. | no for saved reviews; yes for future foreground-only fallback |
| Computer Use | unavailable as a standalone background tool in current tool surface | last-resort UI operation | official background Computer Use MCP surface is not exposed in this session; foreground pyautogui-style recovery would interfere with the user's active Chrome work | cannot use Computer Use to recover GPT Pro Stage 03 submission while the user is using foreground Chrome | use Chrome extension/background control only, or wait for user to provide an idle foreground window/background Computer Use surface | yes |
| GitHub connection | available | repo, PR, review | repo exists and PR is open; GitHub plugin user differs from repo owner but PR workflow is functional | connector can comment/read and `gh` can perform authenticated CLI operations | record owner/account assumptions in stage PR logs | yes for owner-only browser actions |
| GitHub CLI | available | branch, push, PR | none after persistent login | `gh auth status` reports active account `xiaoming2cf-afk` with `repo,workflow` scopes; `lhy18613775` remains a non-active secondary login | none | no |
| GitHub Actions | available | CI gate | none for Stage 00 | governance CI passed on PR | none | no |
| PR `@codex review` | available | Codex review gate | current-head response can diverge by PR surface after bounded retry plus method switch | Stage 03 PR #9 reviewed closeout head `14145ffb0b2c4fa6f94530f39efb779edbf3e84c` and returned CR-03-028 on stale current-state wording, while replacement PR #10 reviewed the same head and returned no-major. B-0062 records the active status correction and recheck requirement. | use CLI comment, minimal retry, PR review-event route, replacement PR only when necessary, then record blocker or active method-switch evidence; never claim Gate 6 without current-head evidence for the active route | no |
| Subagents | available | independent Stage 00 completeness audit | must be spawned explicitly | improves verification | local self-check if unavailable | no |
| MCP | available as concept/tool ecosystem | primary future product entrypoint | no FinSignalHub MCP server in Stage 00 | runtime not implemented by design | Stage 06 plan | no |
| Local shell | available | checks and audits | none | supports verification | none | no |
| Docker | available for daemon, compose config, and local runtime smoke | Stage 01 scaffold runtime checks | daemon resolved on 2026-05-26: `docker info`, `docker version`, and `docker compose version` pass; `docker compose config` passed after the approved compose file was created; `docker compose up --build -d` and health smoke checks passed locally | Docker no longer blocks local Stage 01 scaffold verification | CI now includes compose config and runtime smoke; keep Docker artifacts out of committed runtime state | no |
| Python | available | future scripts/checks | none | can run verification scripts later | shell checks | no |
| Node.js | available | future admin/tooling | none | available for later stages | none | no |
| Package managers | partial | future JS tooling | `npm.ps1` blocked; `npm.cmd` works; pnpm/yarn unavailable | use `npm.cmd` on Windows | document command form | no |
| GPT Pro page accessibility | available for Stage 03 through logged-in Chrome extension DOM route | blocking review gate | Earlier routes had limits: Chrome extension direct tab control returned `native pipe is closed` on 2026-05-29, the in-app Browser lacks the user's ChatGPT login state, isolated off-screen Chrome redirected to login, and standalone background Computer Use is not exposed. On 2026-05-30, the logged-in Chrome extension route submitted Stage 03 follow-up, implementation-goal, final implementation, and CR-03-043 re-review packets and captured responses without entering secrets or credentials. Edge/CDP remains historical evidence only and is not an allowed current Stage 03 follow-up route. | GPT Pro returned Stage 01 final PASS, Stage 02 plan PASS, Stage 02 final implementation PASS, Stage 03 plan CONDITIONAL PASS, Stage 03 follow-up PASS, Stage 03 implementation-goal PASS, Stage 03 final implementation PASS, and Stage 03 CR-03-043 re-review PASS. Stage 04 planning-only is authorized after clean evidence closeout; Stage 04 implementation remains unauthorized. | Use the logged-in Chrome extension DOM route only when DOM is readable and no login/captcha/payment/permission prompt appears; otherwise record a blocker or wait for standalone background Computer Use. Avoid committing raw browser screenshots or clipboard captures that may include unrelated session context. | no for completed reviews; yes for future foreground-only fallback |

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
| Chrome CDP off-screen route | unavailable for authenticated GPT Pro review | GPT Pro follow-up without foreground interaction | Chrome was launched off-screen with remote debugging on port `9337` and the specified GPT Pro URL, but the isolated profile redirected to `https://chatgpt.com/auth/login/?next=...`; Codex must not enter credentials, verification codes, payment data, API keys, tokens, or secrets | This isolated-profile method cannot complete GPT Pro review; it is superseded by the logged-in Chrome extension DOM route recorded below | use the authenticated Chrome extension route only when DOM is readable, or wait for a future standalone background Computer Use surface; do not use Edge while the Chrome-only instruction stands | yes |
| Current Stage 03 GitHub/Codex gate | PASS for reviewed CR-03-043 code head; evidence-closeout recheck pending after push | Stage 03 Gate 6 | CR-03-043 remediation head `adb41c36e66a25ddfa943950b7e08a685906560e` passed both governance CI jobs and received current-head Codex no-major evidence. | Stage 03 code acceptance is clean; saving GPT Pro response/action items creates a governance-only head that must pass live CI/Codex before merge. | Push evidence closeout, sync PR #10 body, verify `gh pr checks 10`, and request current-head Codex no-major if the head changes. | no |
| Chrome extension logged-in profile route | available through DOM route for Stage 03 follow-up and CR-03-043 re-review | GPT Pro review using user's logged-in Chrome profile | Earlier selector/screenshot routes timed out, but the later DOM route claimed the existing GPT Pro tab, submitted Stage 03 follow-up and re-review packets, and captured GPT Pro PASS responses without foreground mouse/keyboard use | Stage 03 GPT Pro review gates are satisfied by saved response/action items; future use still requires readable DOM and no login/secret/permission prompt | use the same DOM route only when stable; otherwise record a blocker or wait for standalone background Computer Use | no |
| Chrome extension visible-DOM/clipboard route | superseded | GPT Pro follow-up using a different Chrome-only background method | Earlier visible-DOM plus clipboard probes timed out, but a later Chrome extension DOM CUA route succeeded on the same logged-in GPT Pro conversation | The earlier timeout no longer blocks Stage 03 planning Gate 7 | keep the successful route evidence; do not repeat timeout-prone probes unless needed for a fresh page | no |
| Standalone background Computer Use for Stage 03 | unavailable | user-requested GPT Pro review recovery without disturbing foreground Chrome | tool discovery exposed no standalone background Computer Use API; available routes are Chrome extension/browser-control and unrelated app tools | Cannot satisfy the requested background Computer Use route or claim GPT Pro review completion through it | wait for a background Computer Use tool surface or an idle foreground window; do not substitute foreground automation or Edge while Chrome-only instruction stands | yes |

## Stage 03 Chrome Follow-Up Resolution

| Capability | status | use in project | blocker | impact | fallback | requires user authorization |
| --- | --- | --- | --- | --- | --- | --- |
| Chrome extension logged-in background tab route | available for Stage 03 follow-up | GPT Pro review submission and response capture without foreground interaction | Earlier selector/screenshot routes timed out, but a later route successfully listed tabs, claimed the existing GPT Pro background tab, read DOM, submitted via DOM CUA, and captured GPT Pro PASS | Stage 03 planning Gate 7 is satisfied for the saved follow-up response | Use this route for future GPT Pro pages only when DOM is readable and no login/secret/permission prompt appears | no |
| Standalone background Computer Use | unavailable / not needed for this completed follow-up | Requested fallback for browser recovery | No standalone API is exposed; this remains a capability limitation | Does not block the saved Stage 03 follow-up because Chrome extension route succeeded | Continue to avoid foreground automation while the user is active | yes for foreground-only fallback |

## Stage 05 GPT Pro Browser Addendum

| Capability | status | use in project | blocker | impact | fallback | requires user authorization |
| --- | --- | --- | --- | --- | --- | --- |
| GPT Pro target page for Stage 05 | requires user action | Stage 05 blocking plan review | Chrome opened the specified GPT Pro page at 2026-06-07T02:02:53-05:00, but the visible page showed a Pro subscription renewal/payment-related prompt. Browser policy requires stopping on payment prompts. | Stage 05 Gate 7 cannot complete; no packet was submitted and no GPT Pro response was captured. Stage 05 implementation remains unauthorized. | User resolves the payment/renewal prompt, then Codex can resubmit the Stage 05 planning packet with live PR #12 evidence. | yes |
| Computer Use for Stage 05 | unavailable as a named standalone tool in this session | visual recovery route requested by user | Tool discovery exposed `node_repl` for Chrome/browser control but no separate Computer Use namespace. Foreground screenshot inspection was used only to detect the stop condition. | Codex cannot claim a dedicated Computer Use submission path for Stage 05; GPT Pro review remains blocked by the payment prompt. | Use Chrome only when the page is safely submittable and no login/captcha/payment/permission/privacy/secret prompt appears. | yes if foreground interaction is required |
