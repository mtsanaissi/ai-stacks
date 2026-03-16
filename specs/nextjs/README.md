# Next.js Template

This folder is a standalone Next.js project-root template.

Use it when starting a Next.js repository that needs AI agent instructions, app-router-oriented conventions, review guidance, and CI scaffolding.

## What To Copy

Copy the full contents of this folder into the root of the new repository.

## Included

- Root agent files for Codex-style agents, Claude Code, and Gemini CLI
- `.gitignore`
- `.pre-commit-config.yaml`
- `.continue/checks/` review prompts
- GitHub workflow templates
- Starter `package.json`
- Docs for routing, server actions, UI patterns, performance, and deployment

## Update After Copying

- Replace the placeholder package name and scripts in `package.json` if the project uses `pnpm`, Turbopack, Playwright, or a different test setup.
- Update `docs/deployment.md` with the real hosting, env var, and release expectations.
- Add domain-specific guidance for auth, data access, design system usage, and caching behavior if those are core to the project.
- Replace placeholder AI review workflow steps with the real action or check setup.

## MCP Suggestions

- Vercel MCP: Official Vercel server for docs, projects, deployments, and logs. High-value for Next.js teams deploying on Vercel. URL: https://vercel.com/docs/agent-resources/vercel-mcp
- Playwright MCP: Official browser automation server for testing flows, reproducing UI bugs, and validating rendered behavior. URL: https://github.com/microsoft/playwright-mcp
- Context7 MCP: Current framework and library docs, especially useful for Next.js, React, and surrounding tooling. URL: https://github.com/upstash/context7
- GitHub MCP Server: Official GitHub server for repo navigation, issue triage, pull requests, and code search. URL: https://github.com/github/github-mcp-server
