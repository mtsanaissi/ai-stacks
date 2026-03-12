# Claude Code Instructions For Python Projects

Use this file as the Claude Code project memory for a Python project.

## Scope

- Follow `docs/coding-standards.md`, `docs/testing.md`, `docs/tooling.md`, and `docs/packaging.md`.
- Prefer type hints for new and changed code.
- Keep side effects explicit and isolate IO.

## Commands

- Setup: `uv sync`
- Lint: `uv run ruff check .`
- Typecheck: `uv run pyright`
- Test: `uv run pytest`

## Change Rules

- Do not make behavior-changing or user-visible assumptions. Ask for clarification when intent is ambiguous or impact is material.
- Prefer existing project patterns over inventing new abstractions.
- Call out bad practices, risky shortcuts, or changes that diverge from common Python conventions.
- Reuse existing modules, services, validators, fixtures, and test helpers when they fit.
- Add new abstractions only when they clearly improve reuse, consistency, or maintainability.
- Prefer standard library and simple abstractions first.
- Validate external input at the boundary.
- Keep modules small and responsibilities clear.

## Tool-Specific Notes

- Claude Code should preserve Python project conventions and keep validation steps explicit.
