# Agent File Sync

This folder contains tooling for keeping `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` aligned.

## Policy

- `AGENTS.md` is the canonical source in each folder.
- `CLAUDE.md` and `GEMINI.md` should keep the same core section structure as `AGENTS.md`.
- Small provider-specific differences are allowed through a dedicated `## Tool-Specific Notes` section and file title/intro text.
- Shared sections should stay textually identical after normalization.

## Scripts

- `sync_agent_files.py`: regenerate `CLAUDE.md` and `GEMINI.md` from each folder's `AGENTS.md`
- `validate_agent_files.py`: verify triplets are present and structurally aligned

## Typical Usage

```bash
python3 tools/agent_docs/sync_agent_files.py
python3 tools/agent_docs/validate_agent_files.py
```

## Pre-commit

The repo root `.pre-commit-config.yaml` runs `validate_agent_files.py` as a local hook so drift is caught before commit.
