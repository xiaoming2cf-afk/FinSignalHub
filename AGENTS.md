# AGENTS.md

## Product Identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. It exists to help AI Agents call structured evidence workflows for researchers and later financial research users.

Primary users are researchers, PhD students, research groups, research-oriented product teams, and innovation project teams. The product must support continuous evidence tracking, updated research judgment, literature matrices, method cards, dataset cards, reproducible export packs, plugin call logs, and later replayable research.

## Non-Goals

Do not implement FinSignalHub as any of these:

- Chatbot or chat-first product.
- Stock recommendation, investment advice, trading signal, or financial prediction tool.
- Generic RAG system.
- Generic literature summarizer.
- Ordinary report generator.
- Standalone financial dashboard.
- Model leaderboard.

If a task drifts toward those directions, stop, invoke the `finsignal-product-governor` skill, and log the reason in `CONTROL/20_BLOCKER_LOG.md`.

## Engineering Rules

- Follow the active stage plan and goal. No implementation may start without a plan and a verifiable goal.
- Keep changes inside the current stage file boundary unless a blocker and ADR justify the exception.
- Prefer small, reviewable changes that leave clear acceptance evidence.
- Use ASCII unless a file already requires another character set.
- Do not scaffold backend, database, frontend, connectors, or MCP tools before their approved stages.

## Test Rules

- Stage 00 only runs governance structure checks.
- Later stages must define local checks, unit tests, integration tests, and acceptance checks in the stage plan.
- A stage cannot pass if tests are skipped without a documented blocker or explicit deferred rationale.

## Documentation Rules

- Every directory must explain its purpose.
- Every `CONTROL` file must include Purpose, Owner, When to update, Required fields, Example format, and Current state.
- Docs must be searchable and project-specific. Avoid generic engineering templates.
- `CHANGELOG.md` records user-visible changes only.

## Security Rules

- Never enter passwords, verification codes, payment details, API keys, tokens, or secrets.
- Stop on login, permission, payment, privacy, captcha, or unclear consent prompts.
- Record security-sensitive blockers in `CONTROL/20_BLOCKER_LOG.md`.
- `.env.example` may contain placeholder variable names only.

## Evidence Provenance Requirements

Every future research artifact must preserve source identity, source type, retrieval time, quoted evidence span when applicable, transformation notes, confidence, and tool-call lineage. Evidence without provenance cannot support a claim graph edge, research delta, literature matrix, method card, dataset card, or repro pack.

## MCP Tool Rules

- MCP tools are the primary product interface, but Stage 00 must not implement them.
- Future MCP tools must have explicit schemas, deterministic error shapes, provenance fields, tests, and call logging.
- Tool output must map to research delta, claim graph, evidence card, literature matrix, method card, dataset card, or repro pack value.

## GitHub Review Rules

- Each stage uses a branch or worktree named `stage/XX-short-name`.
- Commit format: `stage-XX: summary`.
- PR title: `Stage XX: Name`.
- PR body must come from `reviews/stage_XX/PR_BODY.md`.
- After PR creation, comment: `@codex review for product alignment, missing tests, security regressions, architecture risks, missing provenance, missing docs, and phase acceptance problems`.
- Codex review findings are summarized in `reviews/stage_XX/CODEX_REVIEW_SUMMARY.md`.
- Critical findings must be fixed or explicitly deferred with reason.

## GPT Pro Review Rules

- GPT Pro review is a blocking gate.
- Each stage must generate `reviews/stage_XX/GPT_PRO_REVIEW_PACKET.md`.
- Save response, action items, final result, and next-stage instruction.
- A stage cannot complete without GPT Pro PASS or an explicit BLOCKED result.

## Stage Acceptance Rules

Ten gates apply to every stage: scope, functionality, tests, docs, logs, GitHub, GPT Pro, product governance, security, and next stage. Missing GitHub PR or missing GPT Pro review means the stage is FAIL or BLOCKED, never passed.

If `AGENTS.md` conflicts with the latest user instruction, follow the latest user instruction and record the reason in `CONTROL/05_DECISION_LOG.md`.
