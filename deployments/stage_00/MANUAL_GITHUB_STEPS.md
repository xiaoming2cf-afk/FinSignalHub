# Manual GitHub Steps For Stage 00

These steps are retained as fallback evidence. Stage 00 now has an open PR and passing CI, but persistent `gh` authentication is still not configured.

```powershell
cd "D:\new work"
git remote add origin <GITHUB_REPO_URL>
git push -u origin main
git push -u origin stage/00-control-system
gh pr create --base main --head stage/00-control-system --title "Stage 00: Control System" --body-file "reviews/stage_00/PR_BODY.md"
gh pr comment --body "@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems"
```

Already completed:

- `git init`
- `git checkout -B stage/00-control-system`
- `git add .`
- `git commit -m "stage-00: establish control system"`
- Local `main` baseline branch prepared for PR base
- Remote repository created: `https://github.com/xiaoming2cf-afk/FinSignalHub.git`
- Branches pushed: `main`, `stage/00-control-system`
- PR opened: `https://github.com/xiaoming2cf-afk/FinSignalHub/pull/1`
- Stage Governance CI passed

If GitHub CLI remains unavailable in a later session, continue using GitHub web UI or temporary Git Credential Manager authentication, then write evidence into `deployments/stage_XX/GITHUB_PR.md`.

Do not mark Gate 6 passed until Codex review actually runs and `reviews/stage_00/CODEX_REVIEW_SUMMARY.md` contains findings or a no-finding review result.
