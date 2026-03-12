from __future__ import annotations

from pathlib import Path

from agent_sync import PROVIDERS, TARGET_DIRS, sync_provider_file


def main() -> None:
    for folder in TARGET_DIRS:
        for provider in PROVIDERS:
            filename = "CLAUDE.md" if provider == "claude" else "GEMINI.md"
            output_path = Path(folder) / filename
            output_path.write_text(sync_provider_file(folder, provider), encoding="utf-8")
            print(f"synced {output_path}")


if __name__ == "__main__":
    main()
