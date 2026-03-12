# Local MCP Server

This folder contains the local MCP server for `ai-stacks` along with the small files needed to run and smoke-test it.

The server is meant for repo-specific maintenance tasks around stack templates and copy guidance. It keeps MCP-specific code close to the supporting tool code it depends on instead of splitting setup docs into a separate top-level folder.

## Exposed Tools

- `list_stacks_tool`: list the available template stacks in `specs/`
- `compare_stack_files_tool`: compare the file inventory of two stack templates
- `check_template_completeness_tool`: check whether a template includes the expected files, directories, and README sections
- `render_copy_checklist_tool`: render `README.md` update steps as a Markdown checklist
- `validate_templates_tool`: validate all templates at once

## Run Locally

1. Create and activate a virtual environment:

```bash
python3 -m venv tools/mcp_server/.venv
source tools/mcp_server/.venv/bin/activate
```

2. Install dependencies:

```bash
python3 -m pip install -r tools/mcp_server/requirements.txt
```

3. Start the server:

```bash
python3 tools/mcp_server/server.py
```

The server uses stdio transport through the official MCP Python SDK.

## Smoke Test

Run the local client to launch the server over stdio and exercise the exposed tools:

```bash
python3 tools/mcp_server/test_client.py
```

Optional arguments:

```bash
python3 tools/mcp_server/test_client.py --stack python --compare-to nextjs
```

## Sample MCP Config

```json
{
  "mcpServers": {
    "ai-stacks": {
      "command": "python3",
      "args": ["tools/mcp_server/server.py"]
    }
  }
}
```

## Folder Layout

- `server.py`: MCP server entrypoint
- `test_client.py`: tiny local stdio client for smoke-testing the server
- `requirements.txt`: Python dependencies for this tool

The server imports shared validation logic from `tools/template_checks/`.

## Related Validation

If you edit agent instruction files in this repo, re-run:

```bash
python3 tools/agent_docs/validate_agent_files.py
```
