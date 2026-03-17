# Agent File Contract

When a change touches `AGENTS.md` or template copy guidance, review it against these rules:

1. `AGENTS.md` is the only checked-in canonical instruction file for the folder.
2. The repo should not require checked-in `CLAUDE.md`, `GEMINI.md`, or other provider-specific duplicates.
3. If a copied template may need another entrypoint filename, the README should explain optional copy or rename guidance after `AGENTS.md` is tailored.
4. In `specs/` stack folders, `AGENTS.md` should stay complete enough to stand on its own with the adjacent docs.
5. After edits, run `python3 tools/agent_docs/validate_agent_files.py`.
