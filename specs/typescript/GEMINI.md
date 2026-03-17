# Gemini CLI Instructions For TypeScript Projects

Use this file as the Gemini CLI instruction file for a TypeScript project.

## Scope

- Follow `docs/coding-standards.md`, `docs/testing.md`, and `docs/tooling.md`.
- Use the repo-local `typescript` skill when available and the task is materially about type contracts, runtime validation, `tsconfig`, package exports, or toolchain behavior; otherwise follow the docs listed above directly.
- Keep runtime behavior explicit and validate external input.

## Commands

- Install: `npm install`
- Lint: `npm run lint`
- Typecheck: `npm run typecheck`
- Test: `npm test`

## Non-Negotiables

- Verify installed package exports and runtime behavior before using new APIs. AI agents often invent imports that exist only in examples or different major versions.
- Ask before changing public types, serialization formats, auth boundaries, env contracts, package manager choices, or build targets.
- Do not lower TypeScript strictness or add unsafe escape hatches to make generated code compile. Fix the model, narrow the types, or validate the boundary.

## Validation

- Run lint, typecheck, and tests after changes.
- Add negative tests when schemas, auth paths, env handling, or serialization behavior changes.

## Tool-Specific Notes

- Gemini CLI should keep TypeScript commands, docs, and validation steps aligned.
