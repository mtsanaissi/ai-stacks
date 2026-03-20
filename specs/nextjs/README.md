# Next.js Template

This folder is a standalone Next.js project-root template.

Use it when starting a Next.js repository that needs thin root agent instructions, stack project conventions, review guidance, and CI scaffolding.

## What To Copy

Copy the full contents of this folder into the root of the new repository.

## Included

- Root `AGENTS.md` guidance that a destination repo can optionally copy or rename for specific tools
- `.gitignore`
- `.pre-commit-config.yaml`
- `.continue/checks/` review prompts
- GitHub workflow templates
- Starter `package.json`
- Docs for project structure, naming, recommended project docs, validation, and deployment

## Update After Copying

- Replace the placeholder package name and any copied scripts in `package.json` with the destination repo's real commands and build setup.
- Replace the included install commands, workflow steps, and review prompts with the destination repo's real toolchain and release flow.
- Update `docs/deployment.md` with the real hosting, env var, and release expectations.
- Fill in the recommended project docs listed in `docs/recommended-docs.md` with the real auth, data access, and architecture rules for the copied app.
- If the destination repo wants `CLAUDE.md`, `GEMINI.md`, or another tool-specific entrypoint filename, copy or rename the tailored `AGENTS.md` after deciding that convention.
- Add a repo-local `nextjs` skill only if the destination repository wants the same skill-first agent workflow used in this template library.
- Replace placeholder AI review workflow steps with the real action or check setup.

## MCP Suggestions

- Vercel MCP: Official Vercel server for docs, projects, deployments, and logs. High-value for Next.js teams deploying on Vercel. URL: https://vercel.com/docs/agent-resources/vercel-mcp
- Playwright MCP: Official browser automation server for testing flows, reproducing UI bugs, and validating rendered behavior. URL: https://github.com/microsoft/playwright-mcp
- Context7 MCP: Current framework and library docs, especially useful for Next.js, React, and surrounding tooling. URL: https://github.com/upstash/context7
- GitHub MCP Server: Official GitHub server for repo navigation, issue triage, pull requests, and code search. URL: https://github.com/github/github-mcp-server
