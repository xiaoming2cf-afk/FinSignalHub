# relation-enum-agent

## Files touched

No direct subagent edits. Main integration created `apps/api/finsignalhub_api/extraction/relations.py`.

## Summary

Defined `ExtractionRelationType` as a Stage 04-only `StrEnum`. The enum is isolated from persisted Stage 02 edge relations and does not create graph edges.

## Risks

Future stages must not treat these labels as persisted graph relations without a separate approved goal.

## Tests

Relation validation is covered by `test_relation_type_is_bounded_to_stage04_enum`.

## Unresolved issues

None locally.

