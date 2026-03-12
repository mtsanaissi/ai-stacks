# Skill Sync Tools

This folder contains small utilities for managing how repo-local skills are mirrored into `.agents/skills/`.

## Current Tool

- `sync_selected_skills.py`: sync only the skills listed in `.agents/skills/selected-skills.txt` from `skills/` into `.agents/skills/`

## Intended Model

- `skills/` is the canonical source for repo-owned skills
- `.agents/skills/` is a managed mirror for the subset of skills that should be usable inside this repo
- not every skill in `skills/` has to be enabled for this repo

## Typical Usage

```bash
python3 tools/skills/sync_selected_skills.py
```

To verify that `.agents/skills/` already matches the selected set without changing files:

```bash
python3 tools/skills/sync_selected_skills.py --check
```
