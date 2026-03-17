# Python Tooling

Use this file to keep local commands, CI, and editor expectations aligned after copying the template.

Default stack:

- Environment and package workflow: `uv`
- Linting: Ruff
- Typecheck: Pyright
- Tests: pytest

Recommended follow-up after copy:

- Confirm the install, lint, typecheck, and test commands still match `pyproject.toml` and CI.
- Replace any placeholder tooling if the project standard is Poetry, Hatch, mypy, tox, nox, or another stack.
- Document pre-commit hooks, formatting expectations, and any generated code steps that contributors must run locally.
