# Stage 03 GPT Pro Action Items

## Current Verdict

`PASS` for the Stage 03 planning gate.

The earlier CONDITIONAL PASS items were resolved by the Chrome follow-up saved in:

- `reviews/stage_03/GPT_PRO_FOLLOWUP_RESPONSE.md`
- `reviews/stage_03/GPT_PRO_FOLLOWUP_ACTION_ITEMS.md`

## Resolved Must-Fix Items

- `B-0040`: resolved by GPT Pro follow-up.
- `B-0057` / `CR-03-020`: resolved by live-head CI PASS and current-head Codex no-major evidence for PR #9 head `dfe38f2ecfd600bed1a38f8ad21ce9305fc5ab79`.
- Stale Stage 03 gate artifacts were corrected before the follow-up packet was submitted.
- Local exact-head evidence, CI links, and Codex no-major evidence were supplied in the GPT Pro follow-up message.

## Current Required Closeout

- Save follow-up response/action items.
- Update Stage 03 acceptance and state records.
- Push the closeout evidence.
- After that push, verify live PR #9 CI and current-head Codex again before merge. Do not create another evidence-only commit solely to record that external verification unless a reviewer requires it.

## Implementation Requirements If Later Authorized

- Create connector base interface and provider-specific fixture-backed implementations only under the approved Stage 03 implementation file boundary.
- Cover OpenAlex, Crossref, Semantic Scholar, arXiv, and user-upload metadata.
- Emit only existing Stage 02 `SourceCreate`, `DocumentCreate`, and `ToolCallLog` compatible outputs.
- Do not change Stage 02 schemas, migrations, domain models, or persisted contracts unless a new blocker and ADR approve the exception.
- Store provider metadata in `SourceCreate.bibliographic_metadata`.
- Store transformation choices in `DocumentCreate.transformation_notes`.
- Add mocked no-network tests and fixtures for all providers.
- Run phase check, forbidden-scope scan, no external API call scan, secret scan, test suite, CI, current-head Codex review, and GPT Pro final implementation review.

## Stop Conditions

- Any connector requires secrets, credentials, login, or paid/private API keys.
- Default tests or CI require live network calls.
- Mapping cannot fit existing Stage 02 schemas without migration or schema changes.
- User upload becomes full document parsing, chunking, evidence extraction, or RAG ingestion.
- Output becomes summary, research delta, claim graph, dashboard, report, ranking, investment signal, or advice.
- Provider terms/licensing cannot be represented safely in metadata/provenance notes.
- PR evidence is tied to a stale head rather than the live PR head.
