# Tools

This folder contains local utilities and repo-specific automation.

## Layout

- `agent_docs/`: validation scripts and policy notes for canonical `AGENTS.md` files
- `skills/`: utilities for selectively mirroring repo-owned skills into `.agents/skills/`
- `template_checks/`: shared template validation logic and command-line checks
- `mcp_server/`: local MCP server and supporting repo template tools

Keep tools grouped by purpose so the repository can grow without dropping unrelated scripts into a single flat folder.
