# TypeScript Template

This folder is a standalone TypeScript project-root template.

Use it when starting a TypeScript repository that needs thin root agent instructions, stack project conventions, code review guidance, and CI scaffolding.

## What To Copy

Copy the full contents of this folder into the root of the new repository.

## Included

- Root agent files for Codex-style agents, Claude Code, and Gemini CLI
- `.gitignore`
- `.pre-commit-config.yaml`
- `.continue/checks/` review prompts
- GitHub workflow templates
- Starter `package.json`
- Docs for coding standards, testing, and tooling

## Update After Copying

- Replace the placeholder package name in `package.json`.
- Adjust scripts if the project uses `pnpm`, `bun`, Jest, or different lint commands.
- Tighten the docs to reflect the project's architecture, boundary validation rules, and runtime model.
- Add a repo-local `typescript` skill only if the destination repository wants the same skill-first agent workflow used in this template library.
- Replace placeholder AI review workflow steps with the real action or check setup.

## MCP Suggestions

- GitHub MCP Server: Official GitHub server for repositories, issues, pull requests, and code search. URL: https://github.com/github/github-mcp-server
- Context7 MCP: Up-to-date library and framework documentation, useful when the agent needs current TypeScript or frontend package docs. URL: https://github.com/upstash/context7
- Filesystem MCP Server: Official reference server for controlled file access inside the repo or workspace. URL: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- Playwright MCP: Browser automation for UI flows, screenshots, accessibility snapshots, and end-to-end investigation. Useful for frontend-heavy TypeScript repos. URL: https://github.com/microsoft/playwright-mcp
