---
id: stack-skills-stay-unmirrored-by-default
date: 2026-03-17
kind: decision
scope: project
tags:
  - skills
  - mirroring
  - templates
  - agents
source: user-correction
---

# Stack Skills Stay Unmirrored By Default

## Summary

Keep repo-owned stack skills out of `.agents/skills/` unless `.agents/skills/selected-skills.txt` is deliberately expanded.

## Context

During rollout validation for the stack skill split, the repo already used the sync mechanism correctly with only `memory` and `task-ledger` selected. The user clarified that stack skills should not be mirrored into this repository by default, even though repo tooling includes Python.

## Remember

Treat stack skills as repo-owned reference assets by default. Mirror only the explicitly chosen repo-local subset, and do not select a stack skill just because the repository uses that language in tooling.
