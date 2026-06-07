# Stage 04 Commands

Use these commands for Stage 04 implementation verification.

## Planning Checks

```powershell
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04
git diff --check
```

## Implementation Checks

```powershell
python -m pytest apps/api/tests/test_stage04_extraction.py
python -m compileall apps/api/finsignalhub_api
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 04
git diff --check
```

## Secret Scan

Use the high-confidence token pattern from the execution log, scoped to changed Stage 04 files. Expected result: no real secrets.

## Forbidden-Scope Scan

Scan new Stage 04 runtime files for Stage 05+ behavior. The implementation must remain mock-only and candidate-only.

```powershell
rg -n -i "claim graph computation|research delta computation|repro pack export|mcp business tool|chatbot ui|generic rag|stock prediction|investment advice|risk mode|replay engine|production queue|provider api call" apps/api/finsignalhub_api/extraction
```

Expected result: no matches.
