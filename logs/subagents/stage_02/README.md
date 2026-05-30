# Stage 02 Subagent Logs

## Purpose

This directory stores bounded subagent logs for Stage 02 planning and later approved Stage 02 implementation. It records verification evidence, not product runtime output.

## How future stages use this directory

- `plan-scope-verifier.md` records the read-only Stage 02 planning audit by Archimedes.
- Later approved Stage 02 implementation subagents must write one log per subagent here, including files touched, summary, risks, tests, and unresolved issues.

## Maintenance rules

Subagents must not modify files outside their declared ownership. Logs must avoid secrets, raw browser session captures, unrelated local paths, and business implementation content before approval.
