# Common Work Project Template

This folder is a standalone generic template for work projects that use AI agents.

It intentionally avoids language-specific or software-only assumptions. Use it for research, operations, documentation, planning, analytics, or mixed projects that still benefit from clear agent instructions.

Contents:

- Root-level `AGENTS.md` guidance
- Generic workflow and collaboration docs
- Generic review and decision-tracking guidance

## What To Copy

Copy the contents of this folder into the root of a new project when the project does not need a language-specific template.

## Update After Copying

- Rewrite the project purpose and scope in `AGENTS.md` before relying on it.
- If a destination tool expects `CLAUDE.md`, `GEMINI.md`, or another entrypoint filename, copy or rename the tailored `AGENTS.md` only after deciding that convention in the destination repo.
- Replace generic process expectations in `docs/workflow.md` with the real workflow for that project.
- Start using `docs/decision-log.md` once project-level decisions begin to accumulate.
