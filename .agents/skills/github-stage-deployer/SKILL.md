---
name: github-stage-deployer
description: Deploy a FinSignalHub stage branch to GitHub PR and request Codex review.
---

# GitHub Stage Deployer

## When to use

Use after local checks pass or are explicitly blocked and before stage acceptance.

## Procedure

1. Check current repository, branch, remotes, and `gh auth status`.
2. Create or switch to `stage/XX-short-name`.
3. Run approved checks.
4. Commit using `stage-XX: concise summary`.
5. Push the branch.
6. Create PR titled `Stage XX: Stage Name` using `reviews/stage_XX/PR_BODY.md`.
7. Comment the required `@codex review` request.
8. Wait for CI or record CI status.
9. Save PR URL to `deployments/stage_XX/GITHUB_PR.md`.
10. After acceptance, create stage tag or release note.
11. If any step fails, write `CONTROL/20_BLOCKER_LOG.md`.

## Required outputs

- Branch, commit, PR URL, CI status, Codex review status, and blocker entries as needed.
- `deployments/stage_XX/GITHUB_PR.md`.

## Failure conditions

- GitHub deployment is claimed without branch, PR, CI, and Codex review evidence.
- Manual fallback is used without recording commands and blockers.
