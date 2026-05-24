---
name: evidence-graph-architect
description: Govern evidence items, claims, claim-evidence edges, provenance, and research deltas.
---

# Evidence Graph Architect

## When to use

Use for domain models, extraction, claim graph, research delta, literature matrix, method card, and dataset card decisions.

## Procedure

1. Identify EvidenceItem, ResearchClaim, and ClaimEvidenceEdge semantics.
2. Require provenance on every evidence-to-claim relationship.
3. Separate observation, method, dataset, limitation, and claim relation types.
4. Reject unsupported claims and fabricated evidence spans.
5. Document graph changes and delta interpretation.

## Required outputs

- Evidence graph decision record.
- Provenance requirements.
- Test scenarios for supported and unsupported edges.

## Failure conditions

- Claims exist without evidence or provenance.
- Deltas become predictions or investment recommendations.
