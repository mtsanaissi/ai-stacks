# Packaging And Tooling

Packaging choices become long-lived project constraints. Keep them deliberate.

## Rules

- Treat `pyproject.toml` as the packaging source of truth.
- Keep dependencies minimal, explicit, and version-aware. Prefer well-maintained packages with clear ownership.
- Ask before changing build backend, package name, published entry points, Python version floor, or distribution assumptions.
- Keep CLI and automation entry points thin; avoid import-time side effects that break tests or tooling.
- Align local commands, CI, and agent guidance when tooling changes.

## Review Hotspots

- Dependency additions that only save a few lines of code but add maintenance or security risk.
- Tooling changes that update local commands without updating CI or docs.
- Console scripts that import heavy application state before parsing arguments or validating config.
- Optional extras or dependency groups that are documented in one place but not wired into the package metadata.

## Common Mistakes

- Keeping placeholder package metadata after copying a template.
- Adding multiple packaging tools without a clear reason.
- Moving typechecking or lint rules without checking editor, CI, and pre-commit alignment.
- Publishing assumptions leaking into an internal-only repo or, inversely, internal shortcuts leaking into a package intended for distribution.
