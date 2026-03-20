# TypeScript Project Instructions

This file is meant to live at the root of a TypeScript project.

## Scope

- Follow `docs/coding-standards.md`, `docs/testing.md`, and `docs/tooling.md`.
- Use the repo-local `typescript` skill when available and the task is materially about type contracts, runtime validation, `tsconfig`, package exports, or toolchain behavior; otherwise follow the docs listed above directly.
- Keep runtime behavior explicit and validate external input.

## Starter Commands

- Replace these after copy if the destination repo uses different scripts or install flow.
- Install: `npm install`
- Lint: `npm run lint`
- Typecheck: `npm run typecheck`
- Test: `npm test`

## Non-Negotiables

- Verify installed package exports and runtime behavior before using new APIs. AI agents often invent imports that exist only in examples or different major versions.
- Ask before changing public types, serialization formats, auth boundaries, env contracts, package manager choices, or build targets.
- Do not lower TypeScript strictness or add unsafe escape hatches to make generated code compile. Fix the model, narrow the types, or validate the boundary.

## Validation

- Run the repo's configured validation for the touched surface after changes. In the starter template, that means lint, typecheck, and tests.
- Add negative tests when schemas, auth paths, env handling, or serialization behavior changes.
