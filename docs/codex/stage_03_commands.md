# Stage 03 Commands

Use these commands for Stage 03 planning verification.

## Planning Checks

```powershell
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03
# Run the project secret scan pattern used in this stage's execution log.
git diff --check
```

## No Implementation Boundary Check

```powershell
Test-Path apps/api/finsignalhub_api/connectors
Test-Path apps/api/tests/test_stage03_connectors.py
Test-Path apps/api/tests/fixtures/stage03_connectors
```

Expected result during planning: all three paths are absent.

## Future Implementation Checks

These are not active until a later approved `/goal`:

```powershell
python -m pytest apps/api/tests/test_stage03_connectors.py
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03
git diff --check
```
