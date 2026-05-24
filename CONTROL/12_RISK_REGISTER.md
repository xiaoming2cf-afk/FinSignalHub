# 12 Risk Register

## Purpose

Tracks project risks that can block product alignment, security, review gates, or reproducibility.

## Owner

Engineering lead and product process lead.

## When to update

Update when a risk appears, changes severity, is mitigated, or becomes a blocker.

## Required fields

- Risk ID
- Risk
- Severity
- Trigger
- Mitigation
- Owner
- Status

## Example format

`R-001 | Product drift to chatbot | high | chat UI request | invoke governor | product lead | open`

## Current state

| Risk ID | Risk | Severity | Trigger | Mitigation | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| R-001 | Product drift to chatbot or generic RAG | high | chat-first or RAG-first request | use product governor and blocker log | product lead | open |
| R-002 | Premature Risk Mode | high | financial risk workflow before P0 | block until post-MVP | product lead | open |
| R-003 | Premature Replay Engine | medium | replay implementation before core evidence stream | defer to later stage | engineering lead | open |
| R-004 | Codex skips GPT Pro | high | stage marked complete without GPT Pro result | hard Gate 7 | phase lead | open |
| R-005 | GitHub not deployed but marked complete | high | no PR URL | hard Gate 6 | phase lead | open |
| R-006 | Skills created but not used | medium | future stages ignore local skills | require skill registry and log entries | engineering lead | open |
| R-007 | Computer Use overreach | high | login, secret, payment, permission prompt | stop and ask user | browser lead | open |
| R-008 | GPT Pro page inaccessible | high | login/captcha/permission | blocker plus copy-ready packet | GPT Pro preparer | open |
| R-009 | Connector lacks mock tests | high | Stage 03 connector without fixtures | connector-builder gate | test lead | planned |
| R-010 | Evidence lacks provenance | high | claim edge without source metadata | evidence-graph gate | architecture lead | planned |
| R-011 | Logs incomplete | high | missing execution/artifact/goal entries | codex-log-keeper gate | phase lead | open |
