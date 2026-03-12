# Claude Code Instructions For ai-stacks

Use this file as project memory for maintaining the `ai-stacks` repository.

## Scope

- Treat the repository itself as the first proof of concept for AI-friendly repo practices.
- Keep `specs/` copy-ready as standalone templates.
- Keep `skills/` reusable, inspectable, and easy to evolve.

## Repository Map

- `README.md`: top-level overview and setup guide for the repo
- `specs/`: project-root templates and stack-specific standards
- `skills/`: reusable agent skills
- `tools/`: local utilities and repo-specific automation
- `tools/mcp_server/`: local MCP server code, setup docs, and smoke-test client
- `.agents/checks/`: vendor-neutral review prompts and expectations

## Working Rules

- Keep changes narrow and relevant to the request.
- Do not make behavior-changing or user-visible assumptions. Ask for clarification when intent is ambiguous or impact is material.
- Prefer existing project patterns over inventing new abstractions.
- Call out bad practices, risky shortcuts, or changes that diverge from common conventions for template libraries and agent-facing repos.
- Reuse existing templates, docs, checks, and workflows when they fit.
- Add new structure only when it clearly improves reuse, consistency, or maintainability.
- When updating a stack template, keep it self-contained and do not make it depend on another folder in this repo.
- When changing commands in agent files, keep starter manifest files and docs aligned.
- When changing shared expectations across templates, check for drift in related `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` files.
- Treat `AGENTS.md` as the canonical source in each folder and keep provider-specific differences limited.

## Skills

- Treat `skills/` as productized assets, not scratch notes.
- Preserve existing skill conventions unless the task explicitly changes them.
- Treat `skills/` as the canonical source for repo-owned skills.
- Treat `.agents/skills/` as a managed mirror of only the skills listed in `.agents/skills/selected-skills.txt`; do not hand-edit mirrored copies unless the task explicitly changes the sync mechanism.
- If work involves repo-local task tracking, use the `task-ledger` skill.

## Validation

- For docs and template changes, validate by checking consistency across related files.
- Prefer lightweight validation commands that fit a docs/templates repo.
- Do not add placeholder automation that implies a working integration unless the file clearly marks it as a template.
- Run `python3 tools/agent_docs/validate_agent_files.py` after editing agent instruction files.
- Run `python3 tools/template_checks/validate_templates.py` after changing stack template structure or required docs.

## Review Standard

- Look for contradictions, template drift, missing copy-after-edit guidance, and unclear handoff quality first.
- Prefer findings that would matter to someone copying a template into a new repo.

## Tool-Specific Notes

- Claude Code should treat this file as project memory and preserve repo-local conventions.
