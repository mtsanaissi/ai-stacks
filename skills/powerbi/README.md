# Power BI Skill

This skill holds the repo-owned agent guidance for Power BI-specific work.

## Purpose

Use this skill for tasks where Power BI or Fabric behavior materially affects the answer, such as:

- semantic model design and relationship behavior
- DAX measures, filter context, and calculation patterns
- report interaction, accessibility, bookmarks, and export-sensitive UX
- RLS, OLS, workspace roles, refresh, gateways, and deployment flow
- embedded analytics, service principals, and tenant-governance decisions

## Layout

- `SKILL.md`: trigger rules, workflow, and reference-routing guidance
- `references/`: deep Power BI operating references for agents

## Repository Status

This skill is intentionally repo-owned but not selected for mirroring into `.agents/skills/` in this repository.

The stack template under `specs/powerbi/` can still reference the skill as an optional repo-local capability for repositories that choose to install it.
