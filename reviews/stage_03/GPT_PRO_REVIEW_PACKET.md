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
- CI: PASS for Stage Governance CI.
- Codex review: BLOCKED because the Codex connector responded that this repository needs a Codex environment before Codex can run.
- GPT Pro submission route: this packet is ready, but background Chrome control returned `native pipe is closed`; foreground visual recovery is suspended because the user is using Chrome.

If this packet is submitted after the route is restored, please also advise whether the Codex environment blocker must be resolved before any Stage 03 implementation can proceed.

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
