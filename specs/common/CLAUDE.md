# Claude Code Instructions For Generic Work Projects

Use this file as the root project memory for a generic work project.

## Scope

- Use this file as the primary instruction entrypoint for AI agents.
- Follow existing project documents before introducing new structure.
- Prefer the simplest process that keeps work clear, auditable, and easy to hand off.

## Working Rules

- Keep changes narrow and relevant to the request.
- Do not make behavior-changing or user-visible assumptions. Ask for clarification when intent is ambiguous or impact is material.
- Preserve the project's existing terminology and structure unless the task changes it.
- Prefer existing project patterns over inventing new abstractions.
- Call out bad practices, risky shortcuts, or changes that diverge from common conventions for this type of project.
- Reuse existing templates, documents, checklists, and workflows when they fit.
- Add new structure only when it clearly improves reuse, consistency, or maintainability.
- Record important decisions and open questions in project docs.
- Flag sensitive, irreversible, or externally visible actions before taking them.

## Review Standard

- Look for factual errors, unclear assumptions, missed dependencies, and weak handoff quality first.
- Prefer outputs that another person can quickly review and continue.

## Supporting Docs

- `docs/workflow.md`
- `docs/review-guidance.md`
- `docs/decision-log.md`

## Tool-Specific Notes

- Claude Code should treat this file as project memory for generic work projects.
