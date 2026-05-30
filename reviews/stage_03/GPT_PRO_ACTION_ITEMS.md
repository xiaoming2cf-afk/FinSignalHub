# Stage 03 GPT Pro Action Items

## Verdict

`CONDITIONAL PASS`

## Must Fix Before Stage 03 Implementation Goal

1. Ensure all Stage 03 gate artifacts no longer contain stale `4c81fe9` / CR-03-005-blocked wording.
2. Ensure `reviews/stage_03/GPT_PRO_REVIEW_PACKET.md`, `CHECKLISTS/STAGE_03_CHECKLIST.md`, `CONTROL/*`, and `RUNLOG/*` reflect the latest verified Gate 6 evidence or explicitly defer to live PR-head verification after a later push.
3. Record local command evidence for:
   - `gh pr view 9 --json headRefOid`
   - `gh pr checks 9`
   - Codex no-major response for the exact current PR head.
4. Record that the review packet submitted to GPT Pro supersedes stale repository artifacts, or commit the corrected packet and review artifacts back to PR #9.
5. Keep Stage 03 implementation blocked until a separate approved `/goal` exists.

## Deferrable

- Live provider API probes.
- Real API keys, paid APIs, private APIs, or credentials.
- Provider rate-limit tuning beyond mocked behavior.
- Full-text upload parsing.
- Evidence extraction.
- Claim graph.
- Research delta.
- RAG answering.
- Dashboard, report, stock, investment, or advice behavior.

## Implementation Requirements If Later Authorized

- Create connector base interface and provider-specific fixture-backed implementations only under the approved Stage 03 implementation file boundary.
- Cover OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata.
- Emit only existing Stage 02 `SourceCreate`, `DocumentCreate`, and `ToolCallLog` compatible outputs.
- Do not change Stage 02 schemas, migrations, domain models, or persisted contracts.
- Store provider metadata in `SourceCreate.bibliographic_metadata`.
- Store transformation choices in `DocumentCreate.transformation_notes`.
- Add mocked no-network tests and fixtures for all providers.
- Run phase check, no-implementation-scope drift scan, no external API call scan, secret scan, test suite, and `git diff --check`.

## Stop Conditions

- Any connector requires secrets, credentials, login, or paid/private API keys.
- Default tests or CI require live network calls.
- Mapping cannot fit existing Stage 02 schemas without migration or schema changes.
- User upload becomes full document parsing, chunking, evidence extraction, or RAG ingestion.
- Output becomes summary, research delta, claim graph, dashboard, report, ranking, investment signal, or advice.
- Provider terms/licensing cannot be represented safely in metadata/provenance notes.
- PR evidence is tied to a stale head rather than the live PR head.
