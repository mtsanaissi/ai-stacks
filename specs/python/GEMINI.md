# Gemini CLI Instructions For Python Projects

Use this file as the Gemini CLI instruction file for a Python project.

## Scope

- Follow `docs/coding-standards.md`, `docs/testing.md`, `docs/tooling.md`, and `docs/packaging.md`.
- Use the repo-local `python` skill when available and the task is materially about Python package layout, imports, typing, subprocesses, serialization, packaging, or runtime entry points; otherwise follow the docs listed above directly.
- Prefer type hints for new and changed code.
- Keep side effects explicit and isolate IO.

## Commands

- Setup: `uv sync`
- Lint: `uv run ruff check .`
- Typecheck: `uv run pyright`
- Test: `uv run pytest`

## Non-Negotiables

- Verify real package APIs and version-specific behavior before coding. AI agents often mix stdlib, framework, and library guidance across versions.
- Ask before changing auth flows, credential storage, packaging entry points, database migrations, or deployment/runtime assumptions.
- Keep trust boundaries obvious. Validation belongs at entry points, not after the data has already crossed half the codebase.

## Validation

- Run lint, typecheck, and tests after changes.
- Add negative tests for malformed input, auth failures, subprocess boundaries, and serialization edges when those areas change.

## Tool-Specific Notes

- Gemini CLI should route to the `python` skill for Python-specific work and avoid speculative framework rewrites in the thin root instructions.
