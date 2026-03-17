# TypeScript Skill

This skill holds the repo-owned agent guidance for TypeScript-specific work.

## Purpose

Use this skill for tasks where TypeScript behavior materially affects the answer, such as:

- public type and schema boundaries
- runtime validation and environment parsing
- `tsconfig`, module resolution, and build-target choices
- package exports, dependency changes, and toolchain alignment

## Layout

- `SKILL.md`: trigger rules, workflow, and reference-routing guidance
- `references/`: deep TypeScript operating references for agents

## Repository Status

This skill is intentionally repo-owned but not selected for mirroring into `.agents/skills/` in this repository.

The stack template under `specs/typescript/` can still reference the skill as an optional repo-local capability for repositories that choose to install it.
