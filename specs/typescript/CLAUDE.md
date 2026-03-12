# Claude Code Instructions For TypeScript Projects

Use this file as the Claude Code project memory for a TypeScript project.

## Scope

- Follow `docs/coding-standards.md`, `docs/testing.md`, and `docs/tooling.md`.
- Prefer strict typing over `any`.
- Keep runtime behavior explicit and validate external input.

## Commands

- Install: `npm install`
- Lint: `npm run lint`
- Typecheck: `npm run typecheck`
- Test: `npm test`

## Change Rules

- Do not make behavior-changing or user-visible assumptions. Ask for clarification when intent is ambiguous or impact is material.
- Prefer existing project patterns over inventing new abstractions.
- Call out bad practices, risky shortcuts, or changes that diverge from common TypeScript conventions.
- Reuse existing utilities, types, schemas, components, and test helpers when they fit.
- Add new abstractions only when they clearly improve reuse, consistency, or maintainability.
- Update types and tests together when behavior changes.
- Prefer project scripts over direct tool invocations.
- Keep modules cohesive and avoid cross-layer leakage.

## Tool-Specific Notes

- Claude Code should preserve TypeScript project conventions and keep changes easy to review.
