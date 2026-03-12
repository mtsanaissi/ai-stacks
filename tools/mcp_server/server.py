from __future__ import annotations

from pathlib import Path
import sys

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_CHECKS_DIR = ROOT / "tools" / "template_checks"
if str(TEMPLATE_CHECKS_DIR) not in sys.path:
    sys.path.insert(0, str(TEMPLATE_CHECKS_DIR))

from core import (  # noqa: E402
    check_template_completeness,
    compare_stack_files,
    list_stacks,
    render_copy_checklist,
    validate_templates,
)


mcp = FastMCP("ai-stacks")


@mcp.tool()
def list_stacks_tool() -> dict[str, object]:
    """List the available template stacks in specs/."""
    return list_stacks()


@mcp.tool()
def compare_stack_files_tool(stack_a: str, stack_b: str) -> dict[str, object]:
    """Compare the file inventory of two stack templates."""
    return compare_stack_files(stack_a=stack_a, stack_b=stack_b)


@mcp.tool()
def check_template_completeness_tool(stack: str) -> dict[str, object]:
    """Check whether a stack template includes the expected core files, folders, and README sections."""
    return check_template_completeness(stack=stack)


@mcp.tool()
def render_copy_checklist_tool(stack: str) -> dict[str, object]:
    """Render the README 'Update After Copying' section for a stack as a Markdown checklist."""
    return render_copy_checklist(stack=stack)


@mcp.tool()
def validate_templates_tool() -> dict[str, object]:
    """Validate all stack templates against the repo's completeness rules."""
    return validate_templates()


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
