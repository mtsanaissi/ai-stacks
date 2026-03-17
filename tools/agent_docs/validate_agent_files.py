from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPECS_DIR = ROOT / "specs"
PROVIDER_FILES = ("CLAUDE.md", "GEMINI.md")


def target_dirs() -> list[Path]:
    spec_dirs = sorted(
        path for path in SPECS_DIR.iterdir() if path.is_dir()
    )
    return [ROOT, *spec_dirs]


def validate_folder(folder: Path) -> list[str]:
    errors: list[str] = []
    agents_path = folder / "AGENTS.md"
    if not agents_path.is_file():
        errors.append(f"{agents_path}: missing required canonical agent file")
        return errors

    lines = agents_path.read_text(encoding="utf-8").splitlines()
    if not lines or not lines[0].startswith("# "):
        errors.append(f"{agents_path}: must start with a level-1 heading")
    if not any(line.startswith("## ") for line in lines):
        errors.append(f"{agents_path}: must include at least one level-2 section")

    provider_paths = [folder / file_name for file_name in PROVIDER_FILES if (folder / file_name).exists()]
    if provider_paths:
        joined = ", ".join(str(path) for path in provider_paths)
        errors.append(
            f"{folder}: unexpected checked-in provider-specific agent files found: {joined}"
        )

    return errors


def main() -> None:
    discovered_targets = target_dirs()
    all_errors: list[str] = []
    for folder in discovered_targets:
        all_errors.extend(validate_folder(folder))

    if all_errors:
        for error in all_errors:
            print(error)
        sys.exit(1)

    validated_dirs = ", ".join(
        "." if folder == ROOT else str(folder.relative_to(ROOT))
        for folder in discovered_targets
    )
    print(
        "All canonical AGENTS.md files are present and no checked-in provider-specific "
        f"duplicates remain in {len(discovered_targets)} directories: {validated_dirs}."
    )


if __name__ == "__main__":
    main()
