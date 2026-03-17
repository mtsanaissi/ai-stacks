# Power BI Template

This folder is a standalone Power BI project-root template.

Use it when starting a Power BI-focused repository that needs thin root agent instructions, stack project conventions, governance reminders, and workflow scaffolding.

## What To Copy

Copy the full contents of this folder into the root of the new repository.

## Included

- Root `AGENTS.md` guidance that a destination repo can optionally copy or rename for specific tools
- `.gitignore`
- `.pre-commit-config.yaml`
- `.continue/checks/` review prompts
- GitHub workflow templates
- Docs for modeling, DAX standards, report design, and release process

## Update After Copying

- Treat the included workflow steps and review prompts as starter defaults until the destination repo replaces them with its real publishing, governance, and review process.
- Add the real publishing workflow, workspace targets, gateway owners, and governance requirements.
- Document data sources, refresh expectations, semantic model ownership, and embedded or service-principal assumptions.
- Extend the docs with the project's naming rules, metric catalog, accessibility expectations, and release sign-off steps.
- If the destination repo wants `CLAUDE.md`, `GEMINI.md`, or another tool-specific entrypoint filename, copy or rename the tailored `AGENTS.md` after deciding that convention.
- Add a repo-local `powerbi` skill only if the destination repository wants the same skill-first agent workflow used in this template library.
- Replace placeholder AI review workflow steps with the real action or check setup.

## MCP Suggestions

- Microsoft Learn MCP Server: Official Microsoft documentation and code-sample server. High-value for Power BI, Fabric, Azure, and Microsoft ecosystem guidance. URL: https://github.com/MicrosoftDocs/mcp
- SQL MCP Server: Official Microsoft SQL-focused MCP for controlled data access through Data API builder. Useful when Power BI work depends on governed relational data exploration. URL: https://learn.microsoft.com/en-us/azure/data-api-builder/mcp/overview
- GitHub MCP Server: Official GitHub server for repo docs, issues, pull requests, and versioned report-development workflows. URL: https://github.com/github/github-mcp-server
- Filesystem MCP Server: Official reference server for controlled local file access when reports, exports, or supporting docs live in the repo. URL: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
