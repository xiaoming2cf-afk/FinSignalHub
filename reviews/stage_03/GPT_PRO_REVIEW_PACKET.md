# GPT Pro Review Packet: Stage 03 Source Connectors Plan

Please review the FinSignalHub Stage 03 plan. This is a planning review only. Do not authorize implementation unless the plan passes and you explicitly provide implementation gate requirements for a later `/goal`.

## Project Identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. It serves researchers, PhD students, labs, research teams, research-oriented product teams, and innovation teams.

Core outputs remain research delta, claim graph, evidence card, literature matrix, method card, dataset card, Repro Pack, and tool call log.

Forbidden directions remain chatbot, generic RAG, stock prediction, investment advice, ordinary report generator, standalone dashboard behavior, model leaderboard, Risk Mode, and Replay Engine.

## Prior Gate Evidence

- Stage 02 merged through PR #8.
- Stage 02 final implementation and CR-02-043 delta/final review passed GPT Pro.
- GPT Pro authorized Stage 03 planning only.

## Stage 03 Planning Goal

Create a source connector plan for:

- OpenAlex
- Crossref
- Semantic Scholar
- arXiv
- user upload metadata
- connector base interface
- normalized `SourceCreate` and `DocumentCreate` output using the existing Stage 02 schemas
- mocked tests and no-network CI

## Planned Boundaries

The Stage 03 plan must not implement connectors yet. It must define:

- connector contracts;
- normalized `SourceCreate` and `DocumentCreate` field mapping without Stage 02 schema or migration changes;
- provenance requirements;
- fixture strategy;
- no-network tests;
- subagent boundaries;
- file boundaries;
- GitHub/Codex/GPT Pro gates;
- risks and stop conditions.

## Questions For GPT Pro

## Current External Gate Blockers

- GitHub PR: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/9
- PR #9 remains the source of truth; verify the live head with `gh pr view 9 --json headRefOid` before accepting Gate 6.
- This base packet is historical planning context and must not be reused as a final GPT Pro follow-up packet without live-head evidence.
- Before any GPT Pro follow-up, read `reviews/stage_03/GPT_PRO_FOLLOWUP_PACKET.md`, `reviews/stage_03/CODEX_REVIEW_SUMMARY.md`, `deployments/stage_03/GITHUB_PR.md`, and `CONTROL/24_CURRENT_STAGE_STATE.md`.
- Insert the live PR head, live CI job links, live Codex review result, unresolved blockers, and exact acceptance status into the follow-up request at submission time.
- If any current-head CI, Codex, or blocker evidence is missing or stale, GPT Pro must return CONDITIONAL PASS or FAIL and Stage 03 implementation remains unauthorized.
- GPT Pro submission route: initial Chrome extension and in-app Browser routes were insufficient, but an off-screen Microsoft Edge Default profile controlled through CDP opened the logged-in GPT Pro page and submitted this Stage 03 planning packet without entering secrets. GPT Pro returned CONDITIONAL PASS. Response and action items are saved in `reviews/stage_03/GPT_PRO_REVIEW_RESPONSE.md` and `reviews/stage_03/GPT_PRO_ACTION_ITEMS.md`.
- GPT Pro conditional must-fix: corrected gate artifacts must be committed back to PR #9, local exact-head `gh pr view 9 --json headRefOid` / CI / Codex evidence must be recorded, and follow-up GPT Pro confirmation is required before Stage 03 implementation `/goal`.

If this packet is resubmitted after any evidence commit, reject stale embedded head evidence and require the live follow-up packet values before deciding whether Stage 03 implementation may be planned.

Please answer:

1. PASS / CONDITIONAL PASS / FAIL for Stage 03 planning.
2. Must-fix plan gaps before implementation may be planned.
3. Deferrable items.
4. Whether the planned connector boundaries preserve Research Mode evidence-stream value.
5. Whether no-network mock testing is sufficient.
6. Whether any forbidden Stage 04+ behavior is leaking into Stage 03.
7. Exact Stage 03 implementation requirements if the plan passes.
8. Stop conditions for connector implementation.

Do not authorize Stage 04 or any evidence extraction work.
