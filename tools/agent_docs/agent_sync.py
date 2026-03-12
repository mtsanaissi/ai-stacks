from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
TARGET_DIRS = [
    ROOT,
    ROOT / "specs" / "common",
    ROOT / "specs" / "typescript",
    ROOT / "specs" / "nextjs",
    ROOT / "specs" / "python",
    ROOT / "specs" / "powerbi",
]
PROVIDERS = ("claude", "gemini")


@dataclass(frozen=True)
class ProviderProfile:
    title: str
    intro: str
    notes: tuple[str, ...]


@dataclass(frozen=True)
class FolderProfile:
    claude: ProviderProfile
    gemini: ProviderProfile


FOLDER_PROFILES: dict[str, FolderProfile] = {
    ".": FolderProfile(
        claude=ProviderProfile(
            title="# Claude Code Instructions For ai-stacks",
            intro="Use this file as project memory for maintaining the `ai-stacks` repository.",
            notes=(
                "Claude Code should treat this file as project memory and preserve repo-local conventions.",
            ),
        ),
        gemini=ProviderProfile(
            title="# Gemini CLI Instructions For ai-stacks",
            intro="Use this file as the root instruction file for maintaining the `ai-stacks` repository.",
            notes=(
                "Gemini CLI should use this file as its primary repo instruction entrypoint.",
            ),
        ),
    ),
    "specs/common": FolderProfile(
        claude=ProviderProfile(
            title="# Claude Code Instructions For Generic Work Projects",
            intro="Use this file as the root project memory for a generic work project.",
            notes=(
                "Claude Code should treat this file as project memory for generic work projects.",
            ),
        ),
        gemini=ProviderProfile(
            title="# Gemini CLI Instructions For Generic Work Projects",
            intro="Use this file as the root instruction file for a generic work project.",
            notes=(
                "Gemini CLI should use this file as the primary instruction file for generic work projects.",
            ),
        ),
    ),
    "specs/typescript": FolderProfile(
        claude=ProviderProfile(
            title="# Claude Code Instructions For TypeScript Projects",
            intro="Use this file as the Claude Code project memory for a TypeScript project.",
            notes=(
                "Claude Code should preserve TypeScript project conventions and keep changes easy to review.",
            ),
        ),
        gemini=ProviderProfile(
            title="# Gemini CLI Instructions For TypeScript Projects",
            intro="Use this file as the Gemini CLI instruction file for a TypeScript project.",
            notes=(
                "Gemini CLI should keep TypeScript commands, docs, and validation steps aligned.",
            ),
        ),
    ),
    "specs/nextjs": FolderProfile(
        claude=ProviderProfile(
            title="# Claude Code Instructions For Next.js Projects",
            intro="Use this file as the Claude Code project memory for a Next.js project.",
            notes=(
                "Claude Code should preserve Next.js server-client boundaries and app-router conventions.",
            ),
        ),
        gemini=ProviderProfile(
            title="# Gemini CLI Instructions For Next.js Projects",
            intro="Use this file as the Gemini CLI instruction file for a Next.js project.",
            notes=(
                "Gemini CLI should keep routing, deployment, and validation guidance aligned with project docs.",
            ),
        ),
    ),
    "specs/python": FolderProfile(
        claude=ProviderProfile(
            title="# Claude Code Instructions For Python Projects",
            intro="Use this file as the Claude Code project memory for a Python project.",
            notes=(
                "Claude Code should preserve Python project conventions and keep validation steps explicit.",
            ),
        ),
        gemini=ProviderProfile(
            title="# Gemini CLI Instructions For Python Projects",
            intro="Use this file as the Gemini CLI instruction file for a Python project.",
            notes=(
                "Gemini CLI should keep Python commands, packaging guidance, and validation steps aligned.",
            ),
        ),
    ),
    "specs/powerbi": FolderProfile(
        claude=ProviderProfile(
            title="# Claude Code Instructions For Power BI Projects",
            intro="Use this file as the Claude Code project memory for a Power BI project.",
            notes=(
                "Claude Code should preserve semantic model clarity and document governance-sensitive changes.",
            ),
        ),
        gemini=ProviderProfile(
            title="# Gemini CLI Instructions For Power BI Projects",
            intro="Use this file as the Gemini CLI instruction file for a Power BI project.",
            notes=(
                "Gemini CLI should keep report, model, and publishing guidance aligned with project docs.",
            ),
        ),
    ),
}


def folder_key(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return "." if str(rel) == "." else str(rel).replace("\\", "/")


def parse_agents_file(path: Path) -> tuple[str, str, list[tuple[str, str]]]:
    text = path.read_text(encoding="utf-8").strip() + "\n"
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"{path} must start with a level-1 heading")

    title = lines[0].strip()
    remaining = lines[1:]

    intro_lines: list[str] = []
    index = 0
    while index < len(remaining):
        line = remaining[index]
        if line.startswith("## "):
            break
        intro_lines.append(line)
        index += 1
    intro = "\n".join(intro_lines).strip()

    sections: list[tuple[str, str]] = []
    current_heading: str | None = None
    current_lines: list[str] = []
    for line in remaining[index:]:
        if line.startswith("## "):
            if current_heading is not None:
                sections.append((current_heading, "\n".join(current_lines).strip()))
            current_heading = line.strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_heading is not None:
        sections.append((current_heading, "\n".join(current_lines).strip()))

    return title, intro, sections


def serialize_markdown(title: str, intro: str, sections: list[tuple[str, str]]) -> str:
    parts = [title, "", intro.strip(), ""]
    for heading, body in sections:
        parts.append(heading)
        parts.append("")
        parts.append(body.strip())
        parts.append("")
    return "\n".join(parts).strip() + "\n"


def provider_profile_for(path: Path, provider: str) -> ProviderProfile:
    profile = FOLDER_PROFILES[folder_key(path)]
    return getattr(profile, provider)


def sync_provider_file(folder: Path, provider: str) -> str:
    _, _, sections = parse_agents_file(folder / "AGENTS.md")
    provider_profile = provider_profile_for(folder, provider)
    synced_sections = list(sections)
    synced_sections.append(
        (
            "## Tool-Specific Notes",
            "\n".join(f"- {note}" for note in provider_profile.notes),
        )
    )
    return serialize_markdown(provider_profile.title, provider_profile.intro, synced_sections)


def normalize_body(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def parse_generic_file(path: Path) -> tuple[str, str, list[tuple[str, str]]]:
    return parse_agents_file(path)

