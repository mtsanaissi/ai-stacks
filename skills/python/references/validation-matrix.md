# Validation Matrix

Use the smallest validation set that still exercises the risk introduced by the change.

## Always

- Run project lint.
- Run the relevant tests.

## Package Structure, Imports, Or Type Shape Changes

- Run the project's typecheck after changing public interfaces, imports, or typed contracts.
- Verify the changed modules still import cleanly in the intended runtime context.

## Trust Boundary, Serialization, Subprocess, Or Config Changes

- Add or run negative tests for malformed input, unauthorized use, subprocess failure, or unsafe payload handling as applicable.
- Exercise the boundary directly instead of only through a higher-level happy path.
- Re-check logging and error surfaces for secret or environment leakage.

## Packaging Or Tooling Changes

- Verify local commands, CI expectations, and documented commands still agree.
- Check that entry points, dependency groups, and Python version assumptions match `pyproject.toml`.

## Test-Only Changes

- Run the smallest relevant pytest target plus any lint or typecheck gates the touched files require.
