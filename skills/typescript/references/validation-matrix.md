# Validation Matrix

Use the smallest validation set that still exercises the risk introduced by the change.

## Always

- Run project lint.
- Run project typecheck.
- Run the relevant automated tests.

## Public Types, Schemas, And Serialization Changes

- Add or update negative tests for malformed input and incompatible payloads.
- Verify parsers, serializers, and declared types still agree on optional and required fields.
- Re-check any external contract examples or fixtures touched by the change.

## Runtime Boundary, Env, Or Input-Handling Changes

- Exercise invalid input and invalid configuration paths, not only happy paths.
- Verify secrets, tokens, and PII do not leak through thrown errors, logs, or snapshots.
- Confirm the affected entry point still enforces auth or ownership checks where applicable.

## Tooling, Config, Or Dependency Changes

- Verify the documented install, lint, typecheck, and test commands still work.
- Check that lockfile and script changes are intentional and reviewable.
- Confirm runtime and module assumptions still match the chosen package manager, bundler, and test runner.
