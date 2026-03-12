# Template Checks

This folder contains repo-local validation logic for `specs/` templates.

It is intentionally independent from the MCP server so the same checks can be used by:

- pre-commit hooks
- local scripts
- MCP tools

## Files

- `core.py`: shared template inspection and validation logic
- `validate_templates.py`: command-line validator for template completeness
