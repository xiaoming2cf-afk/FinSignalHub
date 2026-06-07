# Stage 05 Commands

## Planning Checks

```powershell
python finsignalhub-codex-plugin\scripts\phase_check.py --stage 05
Test-Path apps\api\finsignalhub_api\claim_graph
Test-Path apps\api\finsignalhub_api\research_delta
Test-Path apps\api\tests\test_stage05_claim_graph.py
Test-Path apps\api\tests\test_stage05_research_delta.py
Test-Path apps\api\tests\fixtures\stage05_claim_graph
git diff --check
```

All `Test-Path` checks for Stage 05 implementation paths must return `False` during planning.

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
