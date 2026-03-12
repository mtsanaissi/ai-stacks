from __future__ import annotations

import sys
from pathlib import Path

from agent_sync import TARGET_DIRS, normalize_body, parse_generic_file


ALLOWED_EXTRA_SECTION = "## Tool-Specific Notes"


def validate_folder(folder: Path) -> list[str]:
    errors: list[str] = []
    agents_path = folder / "AGENTS.md"
    claude_path = folder / "CLAUDE.md"
    gemini_path = folder / "GEMINI.md"

    for path in (agents_path, claude_path, gemini_path):
        if not path.is_file():
            errors.append(f"{path}: missing required agent file")
            return errors

    _, _, agent_sections = parse_generic_file(agents_path)
    for other_path in (claude_path, gemini_path):
        _, _, other_sections = parse_generic_file(other_path)

        expected_headings = [heading for heading, _ in agent_sections] + [ALLOWED_EXTRA_SECTION]
        actual_headings = [heading for heading, _ in other_sections]
        if actual_headings != expected_headings:
            errors.append(
                f"{other_path}: section headings differ from AGENTS.md; expected {expected_headings}, got {actual_headings}"
            )
            continue

        for (agent_heading, agent_body), (other_heading, other_body) in zip(
            agent_sections, other_sections[:-1], strict=True
        ):
            if agent_heading != other_heading:
                errors.append(
                    f"{other_path}: section heading mismatch for shared content: {agent_heading} vs {other_heading}"
                )
                continue
            if normalize_body(agent_body) != normalize_body(other_body):
                errors.append(
                    f"{other_path}: shared section {agent_heading} differs from AGENTS.md"
                )

        if len(other_sections) > len(agent_sections) + 1:
            errors.append(f"{other_path}: contains unexpected extra sections")

    return errors


def main() -> None:
    all_errors: list[str] = []
    for folder in TARGET_DIRS:
        all_errors.extend(validate_folder(folder))

    if all_errors:
        for error in all_errors:
            print(error)
        sys.exit(1)

    print("All agent file triplets are aligned.")


if __name__ == "__main__":
    main()
