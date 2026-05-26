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
| R-012 | Stage 01 baseline mismatch | high | Stage 01 implementation starts from `main` before PR #6 is merged | PR #6 merged into `main`; PR #7 retargeted to `main`; current-head CI/Codex evidence recorded | GitHub stage deployer | resolved |
| R-013 | GitHub Actions Node.js runtime warning | medium | CI warns about Node.js 20 action runtime deprecation | GPT Pro said warning does not block Stage 01; handle during Stage 01 or Stage 02 CI hardening | CI owner | deferred |
| R-014 | Browser recovery artifacts leak session context | high | visible Chrome or headless profile recovery creates screenshots, cookies, history, or clipboard captures | remove transient session artifacts; commit only sanitized response/action files and safe page-only smoke screenshots; add ignore rules | browser lead | mitigated |
| R-015 | Implementation evidence reused from stale PR head | high | prior CI/Codex PASS is cited after new scaffold files are created | B-0015 required current-head CI and Codex after implementation push; implementation head `f30a02e7fd891d578e0f6e54f858ed475a6d6881` passed both | GitHub stage deployer | resolved |
| R-016 | Final evidence commit changes PR head after GPT Pro PASS | medium | Stage 01 acceptance files are committed after GPT Pro reviewed implementation head | final evidence commit must contain only governance/review records; rerun CI and request Codex follow-up if PR head changes; no Stage 01 runtime scope changes allowed | phase lead | open |
