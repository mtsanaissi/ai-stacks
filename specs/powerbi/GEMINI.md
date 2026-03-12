# Gemini CLI Instructions For Power BI Projects

Use this file as the Gemini CLI instruction file for a Power BI project.

## Scope

- Follow `docs/modeling.md`, `docs/dax-standards.md`, `docs/report-design.md`, and `docs/release-process.md`.
- Prefer consistent naming, reusable measures, and documented refresh assumptions.

## Change Rules

- Do not make behavior-changing or user-visible assumptions. Ask for clarification when intent is ambiguous or impact is material.
- Prefer existing project patterns over inventing new abstractions.
- Call out bad practices, risky shortcuts, or changes that diverge from common Power BI conventions.
- Reuse existing measures, calculation patterns, semantic model structures, and report conventions when they fit.
- Add new abstractions only when they clearly improve reuse, consistency, or maintainability.
- Favor star-schema modeling where possible.
- Prefer measures over calculated columns unless model constraints require otherwise.
- Document data source, refresh, and publishing changes.

## Tool-Specific Notes

- Gemini CLI should keep report, model, and publishing guidance aligned with project docs.
