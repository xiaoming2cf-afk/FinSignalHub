# Stage 05 Commands

## Planning Checks

```powershell
python finsignalhub-codex-plugin\scripts\phase_check.py --stage 05
python finsignalhub-codex-plugin\scripts\phase_check.py --stage 05 --final
python -m compileall apps\api\finsignalhub_api
Test-Path apps\api\finsignalhub_api\claim_graph
Test-Path apps\api\finsignalhub_api\research_delta
Test-Path apps\api\tests\test_stage05_claim_graph.py
Test-Path apps\api\tests\test_stage05_research_delta.py
Test-Path apps\api\tests\fixtures\stage05_claim_graph
rg -n "(sk-[A-Za-z0-9]{20,}|OPENAI_API_KEY\s*=\s*[^<\s]|GITHUB_TOKEN\s*=\s*[^<\s]|password\s*=\s*[^<\s]|secret\s*=\s*[^<\s]|token\s*=\s*[^<\s])" PLANS TASKS CHECKLISTS reviews\stage_05 deployments\stage_05 docs\architecture\stage_05_claim_graph_research_delta.md docs\codex\stage_05_commands.md logs\subagents\stage_05 CONTROL\24_CURRENT_STAGE_STATE.md CONTROL\19_STAGE_DASHBOARD.md CONTROL\20_BLOCKER_LOG.md CHANGELOG.md
rg -n "chatbot|generic RAG|stock prediction|investment advice|Risk Mode|Replay Engine|dashboard behavior|Repro Pack export logic|MCP business tools|real LLM calls|live external" PLANS\STAGE_05_PLAN.md TASKS\STAGE_05_TASKS.md CHECKLISTS\STAGE_05_CHECKLIST.md reviews\stage_05 docs\architecture\stage_05_claim_graph_research_delta.md logs\subagents\stage_05
$artifactIds = Select-String -Path CONTROL\18_ARTIFACT_REGISTRY.md -Pattern '^\| A-\d{4} \|' | ForEach-Object { if ($_.Line -match '^\| (A-\d{4}) \|') { $Matches[1] } }; $artifactIds | Group-Object | Where-Object { $_.Count -gt 1 }
$checkpointIds = Select-String -Path CONTROL\27_CHECKPOINT_LOG.md -Pattern '^\| CP-\d{4} \|' | ForEach-Object { if ($_.Line -match '^\| (CP-\d{4}) \|') { $Matches[1] } }; $checkpointIds | Group-Object | Where-Object { $_.Count -gt 1 }
$blockerIds = Select-String -Path CONTROL\20_BLOCKER_LOG.md -Pattern '^\| B-\d{4} \|' | ForEach-Object { if ($_.Line -match '^\| (B-\d{4}) \|') { $Matches[1] } }; $blockerIds | Group-Object | Where-Object { $_.Count -gt 1 }
git diff --check
```

All `Test-Path` checks for Stage 05 implementation paths must return `False` during planning. Secret scan must return no matches. Forbidden-scope scan may return only negative or stop-condition references, never implementation. Row-ID uniqueness commands must return no duplicate groups.

## GitHub

```powershell
git status --short --branch
git add .
git commit -m "stage-05: plan claim graph and research delta"
git push -u origin stage/05-claim-graph-delta
gh pr create --title "Stage 05: Claim Graph and Research Delta Planning" --body-file reviews/stage_05/PR_BODY.md --base main --head stage/05-claim-graph-delta
gh pr comment <PR> --body "@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems"
```

## GPT Pro

Submit `reviews/stage_05/GPT_PRO_REVIEW_PACKET.md` to the approved GPT Pro page after GitHub CI and current-head Codex review pass. Stop on login, captcha, payment, permission, secret, privacy, or unclear consent prompts.
