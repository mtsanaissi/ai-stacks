# Power BI Template

This folder is a standalone Power BI project-root template.

Use it when starting a Power BI-focused repository that needs AI agent instructions, review guidance, governance reminders, and workflow scaffolding.

## What To Copy

Copy the full contents of this folder into the root of the new repository.

## Included

- Root agent files for Codex-style agents, Claude Code, and Gemini CLI
- `.gitignore`
- `.pre-commit-config.yaml`
- `.agents/checks/` review prompts
- GitHub workflow templates
- Docs for modeling, DAX standards, report design, and release process

## Update After Copying

- Add the real publishing workflow, workspace targets, and governance requirements.
- Document data sources, refresh expectations, and gateway assumptions.
- Extend report and model guidance with the project's naming rules, metric catalog, and accessibility standards.
- Replace placeholder AI review workflow steps with the real action or check setup.

## MCP Suggestions

- Microsoft Learn MCP Server: Official Microsoft documentation and code-sample server. High-value for Power BI, Fabric, Azure, and Microsoft ecosystem guidance. URL: https://github.com/MicrosoftDocs/mcp
- SQL MCP Server: Official Microsoft SQL-focused MCP for controlled data access through Data API builder. Useful when Power BI work depends on governed relational data exploration. URL: https://learn.microsoft.com/en-us/azure/data-api-builder/mcp/overview
- GitHub MCP Server: Official GitHub server for repo docs, issues, pull requests, and versioned report-development workflows. URL: https://github.com/github/github-mcp-server
- Filesystem MCP Server: Official reference server for controlled local file access when reports, exports, or supporting docs live in the repo. URL: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
