# Task Routing

Read this file first, then load only the references needed for the current task.

## Type Contracts And Exported APIs

Use [type-and-api-boundaries.md](type-and-api-boundaries.md) when the task involves:

- public interfaces, DTOs, and exported library types
- discriminated unions, branded IDs, or domain modeling
- serializer, parser, and schema changes
- keeping validators and declared types aligned

## Runtime Boundaries And Untrusted Input

Use [runtime-and-input-safety.md](runtime-and-input-safety.md) when the task involves:

- request, message, webhook, or CLI input handling
- environment variables and config parsing
- JSON parsing, object traversal, or unsafe merges
- `any`, `@ts-ignore`, non-null assertions, or cast-heavy code paths

## Tooling, Build, And Dependency Surface

Use [tooling-and-config-safety.md](tooling-and-config-safety.md) when the task involves:

- `tsconfig` changes
- package manager, lockfile, or dependency updates
- ESM, CJS, module resolution, or export maps
- build scripts, lint scripts, typecheck commands, or runtime target changes

## Closing Work

Always read [validation-matrix.md](validation-matrix.md) before finishing implementation or review work.
