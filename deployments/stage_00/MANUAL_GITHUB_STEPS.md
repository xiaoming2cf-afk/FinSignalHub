# Manual GitHub Steps For Stage 00

Use these steps after the user provides a GitHub repository and authenticates GitHub CLI.

```powershell
cd "D:\new work"
git remote add origin <GITHUB_REPO_URL>
git push -u origin main
git push -u origin stage/00-control-system
gh pr create --base main --head stage/00-control-system --title "Stage 00: Control System" --body-file "reviews/stage_00/PR_BODY.md"
gh pr comment --body "@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems"
```

Already completed locally:

- `git init`
- `git checkout -B stage/00-control-system`
- `git add .`
- `git commit -m "stage-00: establish control system"`
- Local `main` baseline branch prepared for PR base

If GitHub CLI remains unavailable, create the repository and PR through GitHub web UI, then paste the PR URL into `deployments/stage_00/GITHUB_PR.md`.

Do not mark Gate 6 passed until the real PR URL, CI result, and Codex review summary are saved.
