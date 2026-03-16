# Python Template

This folder is a standalone Python project-root template.

Use it when starting a Python repository that needs AI agent instructions, review guidance, CI scaffolding, and baseline tooling conventions.

## What To Copy

Copy the full contents of this folder into the root of the new repository.

## Included

- Root agent files for Codex-style agents, Claude Code, and Gemini CLI
- `.gitignore`
- `.pre-commit-config.yaml`
- `.continue/checks/` review prompts
- GitHub workflow templates
- Starter `pyproject.toml`
- Docs for coding standards, testing, tooling, and packaging

## Update After Copying

- Replace the placeholder project metadata in `pyproject.toml`.
- Adjust commands if the project uses Poetry, Hatch, mypy, or another environment and typechecking setup.
- Extend the docs with framework-specific guidance such as FastAPI, Django, CLI, or data pipeline conventions.
- Replace placeholder AI review workflow steps with the real action or check setup.

## MCP Suggestions

- GitHub MCP Server: Official GitHub server for repo navigation, issue work, reviews, and code search. URL: https://github.com/github/github-mcp-server
- Context7 MCP: Current library and framework docs, useful for Python packages, web frameworks, and SDK-heavy projects. URL: https://github.com/upstash/context7
- Filesystem MCP Server: Official reference server for controlled file access and safe workspace operations. URL: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- SQL MCP Server: Official Microsoft SQL-focused MCP for controlled data operations through Data API builder. Useful for Python data services and internal tools. URL: https://learn.microsoft.com/en-us/azure/data-api-builder/mcp/overview
