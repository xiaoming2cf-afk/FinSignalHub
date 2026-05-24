# Plugin Scripts

Stage 00.1 adds local-only governance helper scripts for FinSignalHub. These scripts support the project control system; they do not implement product runtime, backend, frontend, database, connectors, or MCP business tools.

## Current helpers

- `phase_check.py`: validates required governance artifacts, rejects unknown stage ids, requires the Stage 00.1 subagent summary when subagent evidence was used, requires explicit plan test categories for Stage 00.1 and later stages, recursively blocks forbidden Stage 00/00.1 runtime scaffold paths while ignoring local environment, cache, and build directories, and uses `--final` when future runtime stages need final acceptance artifacts enforced.
- `log_append.py`: appends monotonic `## Cycle NNNN` entries to a repository-relative path under `RUNLOG/` so autonomous resume logic can trust the latest cycle.
- `export_review_packet.py`: exports a concise governance review packet to a new repository-relative file under `artifacts/`, rejects traversal or protected output paths, refuses overwrites, and fails non-zero when required packet artifacts are missing.

## Maintenance rule

Future helper scripts must stay governance-only unless a later approved stage explicitly authorizes runtime implementation.
