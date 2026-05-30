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

## Implementation Checks

These are active after GPT Pro accepted the Stage 03 implementation goal:

```powershell
python -m pytest apps/api/tests/test_stage03_connectors.py
python finsignalhub-codex-plugin/scripts/phase_check.py --stage 03
git diff --check
```

Additional checks used before push:

```powershell
python -m pytest apps/api/tests -q
python -m compileall apps/api/finsignalhub_api
rg --pcre2 "(?i)(api[_-]?key|authorization:\\s*bearer|password\\s*=|secret\\s*=|token\\s*=)" -g "!artifacts/runtime/**" -g "!*.png"
```

Expected connector-test evidence:

- Five provider fixture mappings validate as Stage 02 `SourceCreate`, `DocumentCreate`, and `ToolCallLogCreate`.
- No default connector module imports live network clients.
- Secret-like metadata keys are redacted from safe arguments and provider metadata.
- No `EvidenceItem`, claim graph, Research Delta, MCP business tool, UI, RAG, stock/investment, Risk Mode, or Replay Engine behavior is added.
