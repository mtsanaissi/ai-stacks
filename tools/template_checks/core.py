from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SPECS_DIR = ROOT / "specs"


@dataclass(frozen=True)
class TemplateRequirement:
    required_files: tuple[str, ...]
    required_dirs: tuple[str, ...]
    required_readme_sections: tuple[str, ...]


REQUIREMENTS: dict[str, TemplateRequirement] = {
    "common": TemplateRequirement(
        required_files=("AGENTS.md", "README.md"),
        required_dirs=("docs",),
        required_readme_sections=("What To Copy", "Update After Copying"),
    ),
    "typescript": TemplateRequirement(
        required_files=(
            "AGENTS.md",
            "README.md",
            ".gitignore",
            ".pre-commit-config.yaml",
            "package.json",
        ),
        required_dirs=(".continue/checks", ".github/workflows", "docs"),
        required_readme_sections=("What To Copy", "Included", "Update After Copying", "MCP Suggestions"),
    ),
    "nextjs": TemplateRequirement(
        required_files=(
            "AGENTS.md",
            "README.md",
            ".gitignore",
            ".pre-commit-config.yaml",
            "package.json",
        ),
        required_dirs=(".continue/checks", ".github/workflows", "docs"),
        required_readme_sections=("What To Copy", "Included", "Update After Copying", "MCP Suggestions"),
    ),
    "python": TemplateRequirement(
        required_files=(
            "AGENTS.md",
            "README.md",
            ".gitignore",
            ".pre-commit-config.yaml",
        ),
        required_dirs=(".continue/checks", ".github/workflows", "docs"),
        required_readme_sections=("What To Copy", "Included", "Update After Copying", "MCP Suggestions"),
    ),
    "powerbi": TemplateRequirement(
        required_files=(
            "AGENTS.md",
            "README.md",
            ".gitignore",
            ".pre-commit-config.yaml",
        ),
        required_dirs=(".continue/checks", ".github/workflows", "docs"),
        required_readme_sections=("What To Copy", "Included", "Update After Copying", "MCP Suggestions"),
    ),
}


def list_stack_names() -> list[str]:
    return sorted(path.name for path in SPECS_DIR.iterdir() if path.is_dir())


def stack_path(stack: str) -> Path:
    path = SPECS_DIR / stack
    if not path.is_dir():
        raise ValueError(f"Unknown stack: {stack}")
    return path


def relative_files(path: Path) -> list[str]:
    return sorted(str(file.relative_to(path)) for file in path.rglob("*") if file.is_file())


def readme_sections(path: Path) -> list[str]:
    sections: list[str] = []
    readme = path / "README.md"
    if not readme.exists():
        return sections
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            sections.append(line.removeprefix("## ").strip())
    return sections


def extract_update_after_copying_items(path: Path) -> list[str]:
    readme = path / "README.md"
    if not readme.exists():
        return []

    lines = readme.read_text(encoding="utf-8").splitlines()
    items: list[str] = []
    in_section = False
    for line in lines:
        if line.startswith("## "):
            if in_section:
                break
            in_section = line == "## Update After Copying"
            continue
        if in_section and line.startswith("- "):
            items.append(line[2:].strip())
    return items


def list_stacks() -> dict[str, object]:
    stacks = []
    for name in list_stack_names():
        path = stack_path(name)
        stacks.append(
            {
                "name": name,
                "path": str(path.relative_to(ROOT)),
                "has_agents_checks": (path / ".agents" / "checks").is_dir(),
                "has_docs": (path / "docs").is_dir(),
                "has_readme": (path / "README.md").is_file(),
            }
        )
    return {"stacks": stacks}


def compare_stack_files(stack_a: str, stack_b: str) -> dict[str, object]:
    path_a = stack_path(stack_a)
    path_b = stack_path(stack_b)
    files_a = set(relative_files(path_a))
    files_b = set(relative_files(path_b))
    shared = sorted(files_a & files_b)
    only_a = sorted(files_a - files_b)
    only_b = sorted(files_b - files_a)
    return {
        "stack_a": stack_a,
        "stack_b": stack_b,
        "shared_file_count": len(shared),
        "only_in_a": only_a,
        "only_in_b": only_b,
    }


def check_template_completeness(stack: str) -> dict[str, object]:
    path = stack_path(stack)
    requirement = REQUIREMENTS.get(stack)
    if requirement is None:
        raise ValueError(f"No completeness rules defined for stack: {stack}")

    missing_files = [
        file_name for file_name in requirement.required_files if not (path / file_name).is_file()
    ]
    missing_dirs = [
        dir_name for dir_name in requirement.required_dirs if not (path / dir_name).is_dir()
    ]
    actual_sections = set(readme_sections(path))
    missing_readme_sections = [
        section for section in requirement.required_readme_sections if section not in actual_sections
    ]

    issues: list[str] = []
    if missing_files:
        issues.append(f"Missing required files: {', '.join(missing_files)}")
    if missing_dirs:
        issues.append(f"Missing required directories: {', '.join(missing_dirs)}")
    if missing_readme_sections:
        issues.append(f"Missing README sections: {', '.join(missing_readme_sections)}")

    return {
        "stack": stack,
        "complete": not issues,
        "missing_files": missing_files,
        "missing_dirs": missing_dirs,
        "missing_readme_sections": missing_readme_sections,
        "issues": issues,
    }


def validate_templates() -> dict[str, object]:
    results = [check_template_completeness(stack) for stack in list_stack_names()]
    incomplete = [result["stack"] for result in results if not result["complete"]]
    return {
        "complete": not incomplete,
        "template_count": len(results),
        "incomplete_templates": incomplete,
        "results": results,
    }


def render_copy_checklist(stack: str) -> dict[str, object]:
    path = stack_path(stack)
    items = extract_update_after_copying_items(path)
    checklist = [f"- [ ] {item}" for item in items]
    return {
        "stack": stack,
        "item_count": len(checklist),
        "checklist_markdown": "\n".join(checklist),
        "items": items,
    }
