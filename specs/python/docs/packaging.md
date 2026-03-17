# Packaging

Use this file to record the real packaging and runtime assumptions of the copied project.

Recommended sections:

- Python version floor and supported runtimes
- Package or application layout
- Dependency groups and optional extras
- CLI entry points, workers, or other runtime commands
- Build, publish, or internal distribution notes

Conventions:

- Keep dependencies minimal, explicit, and justified.
- Prefer `pyproject.toml` as the packaging source of truth.
- Document entry points, optional extras, and required Python versions in one place.
- Ask before changing build backend, package name, or distribution assumptions after copy.
