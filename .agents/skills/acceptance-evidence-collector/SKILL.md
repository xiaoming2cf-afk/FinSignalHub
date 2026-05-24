---
name: acceptance-evidence-collector
description: Collect stage acceptance evidence for FinSignalHub review gates.
---

# Acceptance Evidence Collector

## When to use

Use before phase-gate-auditor and before GPT Pro packet finalization.

## Procedure

1. Gather local check output, file lists, PR URL, CI status, Codex review summary, GPT Pro response, action items, and blockers.
2. Register evidence in `CONTROL/18_ARTIFACT_REGISTRY.md`.
3. Ensure every hard gate has a path or blocker.
4. Reject empty evidence files.

## Required outputs

- Artifact registry updates.
- Evidence list for review packet.
- Missing evidence blocker entries.

## Failure conditions

- Gate evidence is missing but marked passed.
- Acceptance relies on an empty placeholder file.
