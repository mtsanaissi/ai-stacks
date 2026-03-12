from __future__ import annotations

import sys

from core import validate_templates


def main() -> None:
    result = validate_templates()
    if result["complete"]:
        print(f"All {result['template_count']} templates are complete.")
        return

    for template_result in result["results"]:
        if template_result["complete"]:
            continue
        print(f"{template_result['stack']}:")
        for issue in template_result["issues"]:
            print(f"  - {issue}")
    sys.exit(1)


if __name__ == "__main__":
    main()
