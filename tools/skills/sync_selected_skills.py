from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "skills"
TARGET_DIR = ROOT / ".agents" / "skills"
SELECTION_FILE = TARGET_DIR / "selected-skills.txt"


def load_selected_skills() -> list[str]:
    if not SELECTION_FILE.exists():
        raise SystemExit(f"missing selection file: {SELECTION_FILE}")

    selected: list[str] = []
    for raw_line in SELECTION_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        selected.append(line)
    return selected


def available_skills() -> set[str]:
    return {
        path.name
        for path in SOURCE_DIR.iterdir()
        if path.is_dir() and (path / "SKILL.md").exists()
    }


def directories_match(source: Path, target: Path) -> bool:
    if not target.exists() or not target.is_dir():
        return False

    comparison = filecmp.dircmp(source, target, ignore=[])
    if comparison.left_only or comparison.right_only or comparison.diff_files or comparison.funny_files:
        return False

    return all(
        directories_match(source / name, target / name)
        for name in comparison.common_dirs
    )


def sync_selected_skills(check_only: bool) -> int:
    selected = load_selected_skills()
    available = available_skills()
    missing = [name for name in selected if name not in available]
    if missing:
        names = ", ".join(sorted(missing))
        raise SystemExit(f"selected skill(s) not found under skills/: {names}")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    changed = False

    for name in sorted(available):
        source_path = SOURCE_DIR / name
        target_path = TARGET_DIR / name
        should_exist = name in selected

        if should_exist:
            if check_only:
                if not directories_match(source_path, target_path):
                    print(f"would sync {target_path.relative_to(ROOT)}")
                    changed = True
            else:
                if target_path.exists():
                    shutil.rmtree(target_path)
                shutil.copytree(source_path, target_path)
                print(f"synced {target_path.relative_to(ROOT)}")
            continue

        if target_path.exists():
            if check_only:
                print(f"would remove {target_path.relative_to(ROOT)}")
                changed = True
            else:
                shutil.rmtree(target_path)
                print(f"removed {target_path.relative_to(ROOT)}")

    if check_only and changed:
        print("selected skills are out of sync")
        return 1

    if check_only:
        print("selected skills are in sync")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync selected repo-local skills into .agents/skills."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="report drift without writing changes",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raise SystemExit(sync_selected_skills(check_only=args.check))


if __name__ == "__main__":
    main()
