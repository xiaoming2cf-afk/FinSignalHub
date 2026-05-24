---
name: repro-pack-builder
description: Define Repro Pack export requirements for auditable research evidence.
---

# Repro Pack Builder

## When to use

Use during Stage 08 and earlier planning for exportable evidence artifacts.

## Procedure

1. Define export formats: BibTeX, CSV, JSONL, Markdown, and Manifest.
2. Preserve source metadata, tool-call lineage, file list, checksums when available, and limitations.
3. Ensure exports support GPT Pro and human review.
4. Reject report-only exports without structured evidence.

## Required outputs

- Repro Pack manifest requirements.
- Export acceptance checklist.
- Tests for provenance preservation.

## Failure conditions

- Export loses provenance or becomes only narrative report text.
