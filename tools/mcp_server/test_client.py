from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


ROOT = Path(__file__).resolve().parents[2]


def build_server_params() -> StdioServerParameters:
    return StdioServerParameters(
        command="python3",
        args=[str(ROOT / "tools" / "mcp_server" / "server.py")],
    )


async def run(stack: str, compare_to: str) -> None:
    async with stdio_client(build_server_params()) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"- {tool.name}")

            calls = [
                ("list_stacks_tool", {}),
                ("validate_templates_tool", {}),
                ("check_template_completeness_tool", {"stack": stack}),
                ("render_copy_checklist_tool", {"stack": stack}),
                ("compare_stack_files_tool", {"stack_a": stack, "stack_b": compare_to}),
            ]

            for name, arguments in calls:
                result = await session.call_tool(name, arguments=arguments)
                print(f"\n{name}")
                print(json.dumps(result.structuredContent, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description="Smoke-test the local ai-stacks MCP server.")
    parser.add_argument(
        "--stack",
        default="nextjs",
        help="Primary stack to use for completeness and checklist checks.",
    )
    parser.add_argument(
        "--compare-to",
        default="typescript",
        help="Secondary stack to compare against the primary stack.",
    )
    args = parser.parse_args()
    asyncio.run(run(stack=args.stack, compare_to=args.compare_to))


if __name__ == "__main__":
    main()
