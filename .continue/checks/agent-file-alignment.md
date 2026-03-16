# Agent File Alignment

When a change touches `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`, review it against these rules:

1. `AGENTS.md` is the canonical source for the folder.
2. `CLAUDE.md` and `GEMINI.md` should keep the same shared section headings and shared section content as `AGENTS.md`.
3. Provider-specific differences should be limited to the file title, intro paragraph, and `## Tool-Specific Notes`.
4. In `specs/` stack folders, `AGENTS.md` should be at least as complete as the provider-specific files.
5. After edits, run the sync and validation scripts under `tools/agent_docs/`.
