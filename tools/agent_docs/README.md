# Agent File Validation

This folder contains tooling for enforcing the repo's checked-in `AGENTS.md` contract.

## Policy

- `AGENTS.md` is the only checked-in canonical instruction file in each tracked folder.
- This repo does not keep checked-in `CLAUDE.md` or `GEMINI.md` duplicates.
- If a copied template wants another tool-specific entrypoint filename, copy or rename `AGENTS.md` in the destination repo after tailoring the content.
- Validation should catch missing canonical files and stale checked-in provider-specific duplicates early.

## Scripts

- `validate_agent_files.py`: verify tracked folders contain `AGENTS.md`, basic heading structure, and no checked-in provider-specific duplicates

## Typical Usage

```bash
python3 tools/agent_docs/validate_agent_files.py
```

## Pre-commit

The repo root `.pre-commit-config.yaml` runs `validate_agent_files.py` as a local hook so canonical-agent drift is caught before commit.
