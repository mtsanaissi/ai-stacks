---
name: typescript
description: Use this skill when the task is materially about TypeScript type design, schema and type drift, runtime validation, environment parsing, tsconfig or module configuration, build targets, package exports, or dependency and toolchain choices in a TypeScript project.
---

# TypeScript

Use this skill for implementation, debugging, refactoring, and review work where TypeScript behavior materially affects the answer.

Do not use this skill for generic JavaScript, CSS, or React tasks unless TypeScript types, config, module boundaries, or runtime safety are part of the work.

## Before You Change Code

1. Inspect the installed `typescript`, runtime, package manager, and relevant framework or build-tool versions before using language or tool-specific APIs.
2. Check the affected runtime and module target first: node, browser, shared, ESM, CJS, bundler, and test runner expectations.
3. Read [references/task-routing.md](references/task-routing.md) first, then load only the referenced files that match the task.

## Reference Routing

- Read [references/type-and-api-boundaries.md](references/type-and-api-boundaries.md) for public types, schema and interface drift, discriminated unions, branded IDs, serializers, and exported contract changes.
- Read [references/runtime-and-input-safety.md](references/runtime-and-input-safety.md) for request or message validation, JSON parsing, environment handling, unsafe casts, dynamic code paths, and untrusted object traversal.
- Read [references/tooling-and-config-safety.md](references/tooling-and-config-safety.md) for `tsconfig`, module resolution, package manager changes, dependency additions, export maps, scripts, and build-target decisions.
- Read [references/validation-matrix.md](references/validation-matrix.md) before closing work so the validation matches the change.

## Workflow

1. Inspect local versions, runtime boundaries, and existing toolchain patterns.
2. Load only the references that match the task shape.
3. Preserve runtime and module boundaries instead of hiding mismatches behind casts or looser config.
4. Make the smallest change that fits the existing project shape.
5. Run the relevant validation from the validation matrix.
6. Report remaining contract, runtime, or toolchain risk explicitly.

## Common Failure Modes

- Treating types as runtime protection and skipping boundary validation.
- Fixing design mismatches by widening exported types or adding review-hostile casts.
- Relaxing `tsconfig` or module settings to hide an integration bug.
- Mixing node, browser, and shared code paths without checking the real runtime boundary.
- Assuming package exports, module formats, or script names from examples instead of the installed repo state.

## Output Expectations

- Name the TypeScript surface being changed: type contract, runtime boundary, config, module system, or dependency surface.
- Call out version-sensitive or runtime-sensitive assumptions.
- If public types, env handling, validation, or build targets changed, say what was verified and what still needs manual confirmation.
