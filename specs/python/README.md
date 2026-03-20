# Python Template

This folder is a standalone Python project-root template.

Use it when starting a Python repository that needs AI agent instructions, review guidance, CI scaffolding, and baseline tooling conventions.

## What To Copy

Copy the full contents of this folder into the root of the new repository.

## Included

- Root `AGENTS.md` guidance that a destination repo can optionally copy or rename for specific tools
- `.gitignore`
- `.pre-commit-config.yaml`
- `.continue/checks/` review prompts
- GitHub workflow templates
- Docs for coding standards, testing, tooling, and packaging

## Update After Copying

- Replace the placeholder workflow and command guidance with the destination repo's real environment, packaging, validation, and test setup.
- Update `AGENTS.md` and the docs in `docs/` so they name the actual commands contributors should run locally and in CI.
- Adjust the copied guidance if the project uses Poetry, Hatch, tox, nox, plain `pip`, or another environment and validation setup.
- Extend the docs with framework-specific guidance such as FastAPI, Django, CLI, or data pipeline conventions.
- If the destination repo wants `CLAUDE.md`, `GEMINI.md`, or another tool-specific entrypoint filename, copy or rename the tailored `AGENTS.md` after deciding that convention.
- Replace placeholder AI review workflow steps with the real action or check setup.

## MCP Suggestions

- GitHub MCP Server: Official GitHub server for repo navigation, issue work, reviews, and code search. URL: https://github.com/github/github-mcp-server
- Context7 MCP: Current library and framework docs, useful for Python packages, web frameworks, and SDK-heavy projects. URL: https://github.com/upstash/context7
- Filesystem MCP Server: Official reference server for controlled file access and safe workspace operations. URL: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- SQL MCP Server: Official Microsoft SQL-focused MCP for controlled data operations through Data API builder. Useful for Python data services and internal tools. URL: https://learn.microsoft.com/en-us/azure/data-api-builder/mcp/overview
