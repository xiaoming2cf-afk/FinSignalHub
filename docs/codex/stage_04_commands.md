# Stage 04 Commands

Use these commands for Stage 04 planning verification.

## Planning Checks

```powershell
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04
git diff --check
```

## No Implementation Boundary Check

```powershell
Test-Path apps/api/finsignalhub_api/extraction
Test-Path apps/api/tests/test_stage04_extraction.py
Test-Path apps/api/tests/fixtures/stage04_extraction
```

Expected result during planning: all three paths are absent.

## Secret Scan

Use the high-confidence token pattern from the execution log. Expected result: no real secrets.

## Forbidden-Scope Scan

Scan new Stage 04 planning files for accidental claims that implementation already exists or that Stage 04 authorizes claim graph, Research Delta, Repro Pack, MCP business tool, UI/dashboard, chatbot/RAG, stock/investment, Risk Mode, or Replay Engine behavior.

## Future Implementation Checks

These are not active during planning. They must be defined in a separate implementation `/goal` after GPT Pro plan PASS:

```powershell
python -m pytest apps/api/tests/test_stage04_extraction.py
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04
git diff --check
```

Default future tests must use mocks and fixtures only.
