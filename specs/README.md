# Specs Library

This repository stores reusable AI-agent standards and project-root templates.

- `specs/common/` is a standalone generic work-project template.
- `specs/typescript/`, `specs/nextjs/`, `specs/python/`, and `specs/powerbi/` are standalone stack-specific templates intended to be copied into the root of a new repository.
- Stack templates do not rely on `specs/common/`.

## Template Quality Bar

Every stack template should be complete enough to copy into a new repository root and use with minimal restructuring.

Minimum expected contents:

- Root `AGENTS.md` as the checked-in canonical agent file
- Ignore rules appropriate for the stack
- Validation commands or scripts appropriate for the stack
- AI review checks under `.continue/checks/` when the stack benefits from them
- CI workflow templates
- Long-form docs for coding, testing, review, or delivery expectations
- A template `README.md` with copy instructions and immediate follow-up edits

Minimum expected quality:

- The template stands on its own and does not depend on another folder in this repo.
- The template does not assume one package manager, repo shape, application topology, or deployment model beyond the stack itself unless that choice is clearly labeled as a starter default.
- Commands shown in agent files match the starter manifest files in the template.
- Instructions prefer existing project patterns and avoid unnecessary abstraction.
- The template is opinionated enough to be useful, but easy to trim down after copying.
- Placeholder files clearly mark which values should be replaced in the destination project.

When copying a stack template into a new project:

1. Copy the entire contents of the chosen `specs/<stack>/` folder into the new repository root.
2. Rewrite `AGENTS.md` for the real project before relying on it, and optionally copy or rename it for tool-specific entrypoints only if the destination repo wants that.
3. Replace starter commands, workflow steps, placeholder metadata, and review prompts with the real project choices before relying on them.
4. Trim files you do not need.
