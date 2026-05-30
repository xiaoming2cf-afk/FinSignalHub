# Stage 03 GPT Pro Follow-Up Packet

## Purpose

This packet is the Chrome-only follow-up request for Stage 03 after GPT Pro returned CONDITIONAL PASS. It is not an implementation request and does not authorize connector code.

## Project Identity

FinSignalHub is Research Mode-first, MCP-first, and evidence-stream oriented. Stage 03 is planning-only for source connectors that will later normalize OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata into existing Stage 02 `SourceCreate`, `DocumentCreate`, and `ToolCallLog` compatible outputs.

Forbidden directions remain: chatbot, generic RAG, stock prediction, investment advice, report generator, dashboard behavior, Risk Mode, Replay Engine, evidence extraction, claim graph computation, Research Delta computation, and MCP business tool implementation.

## Follow-Up Question For GPT Pro

Please review the updated Stage 03 planning gate after the prior CONDITIONAL PASS.

Evidence now available:

- PR #9: https://github.com/xiaoming2cf-afk/FinSignalHub/pull/9
- Live PR head must be verified immediately before this packet is submitted by reading PR #9, not by trusting an embedded commit hash in this file.
- Required live GitHub evidence to include in the GPT Pro message before submission:
  - `gh pr view 9 --json headRefOid,statusCheckRollup,url`
  - current-head CI PASS links for both Stage Governance jobs
  - current-head Codex result link or current-head Codex blocker link
- If the live PR head has changed after this packet was last committed, GPT Pro must treat any older commit hash or older CI/Codex link as historical evidence only.
- As of the latest committed blocker-evidence head, the follow-up packet itself is blocked until the new head receives fresh CI/Codex evidence. Do not treat the historical `9d71438e90e4dfd7bea0078ff1a6097be454f6b5` no-major result as evidence for a later push.
- Live PR body must be synced from `reviews/stage_03/PR_BODY.md` after any remediation push and before GPT Pro submission.
- Known Codex findings CR-03-001 through CR-03-009 are historical/resolved; CR-03-010/011 are the active GitHub gate findings until the remediation head is pushed and rechecked.
- Stage 03 implementation paths remain absent:
  - `apps/api/finsignalhub_api/connectors`
  - `apps/api/tests/test_stage03_connectors.py`
  - `apps/api/tests/fixtures/stage03_connectors`
- Local governance checks that must pass before GPT Pro submission:
  - `python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03`
  - Stage 03 implementation path absence check
  - tracked secret-pattern scan
  - `git diff --check`
  - artifact/checkpoint ID uniqueness

Please answer:

1. Does this resolve the prior CONDITIONAL PASS must-fix item B-0040?
2. Is Stage 03 planning gate now PASS, CONDITIONAL PASS, or FAIL?
3. May Codex draft Stage 03 implementation `/goal` artifacts while still not implementing connector code until the separate `/goal` begins?
4. If allowed, provide the exact Stage 03 implementation goal requirements, allowed files, forbidden files, required tests, stop conditions, GitHub/Codex gates, and GPT Pro final review gates.
5. If not allowed, list the remaining must-fix items and distinguish critical items from deferrable items.

Required response format:

- VERDICT: PASS / CONDITIONAL PASS / FAIL
- MUST FIX NOW:
- DEFERRABLE:
- NEXT STAGE 03 GOAL REQUIREMENTS:
- STOP CONDITIONS:

End your response with:

`END_STAGE03_FOLLOWUP_REVIEW`

## Current Blocker

Codex attempted the Chrome-only background route requested by the user. Off-screen Chrome CDP opened the specified GPT Pro URL but redirected to ChatGPT login. Codex did not enter credentials, verification codes, payment data, API keys, tokens, or secrets. This blocker is recorded as `CONTROL/20_BLOCKER_LOG.md` B-0045.
