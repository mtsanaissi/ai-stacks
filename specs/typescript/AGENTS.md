# TypeScript Project Instructions

This file is meant to live at the root of a TypeScript project.

## Scope

- Follow `docs/coding-standards.md`, `docs/testing.md`, and `docs/tooling.md`.
- Prefer strict typing over `any`.
- Keep runtime behavior explicit and validate external input.

## Commands

- Install: `npm install`
- Lint: `npm run lint`
- Typecheck: `npm run typecheck`
- Test: `npm test`

## Non-Negotiables

- Verify installed package exports and runtime behavior before using new APIs. AI agents often invent imports that exist only in examples or different major versions.
- Ask before changing public types, serialization formats, auth boundaries, env contracts, or build targets.
- Do not lower TypeScript strictness to make generated code compile. Fix the model, narrow the types, or validate the boundary.

## Security and Data Handling

- Treat TypeScript types as design-time help, not runtime protection. Validate all untrusted input at the process, API, or message boundary.
- Keep environment variable parsing centralized and fail fast on invalid config. Do not scatter `process.env.FOO!` across the codebase.
- Do not suppress security-relevant type errors with `any`, `@ts-ignore`, `as unknown as`, or blanket non-null assertions.
- Avoid `eval`, `new Function`, dynamic `vm` execution, and dynamic imports or requires derived from user input or mutable config.
- Guard against prototype pollution and unsafe object merges. Use schema validation, allowlists, and `Object.hasOwn()` when traversing untrusted objects.
- Keep secrets, tokens, and PII out of logs, thrown error payloads, snapshots, demo fixtures, and client-visible source maps.
- Prefer stable, reproducible installs for automation and CI. Commit lockfiles, review install scripts, and do not add dependencies casually.

## Stack-Specific Failure Modes

- Update runtime validators and declared types together. Drift between schemas and interfaces is a security bug, not a documentation issue.
- Use discriminated unions, branded IDs, and narrow interfaces for auth, tenant, and resource ownership boundaries.
- If `tsconfig` is touched, tighten rather than relax. Preserve `strict` and do not disable safeguards like `exactOptionalPropertyTypes` or `noUncheckedIndexedAccess` to hide bugs.
- Do not deserialize JSON into trusted domain objects without shape checks, version checks, and explicit handling for optional fields.
- For Node-based TypeScript services, prefer `npm ci` in CI and consider the Node permission model only as blast-radius reduction for trusted code, not as a supply-chain security guarantee.
- Do not widen exported types to `string`, `Record<string, unknown>`, or `unknown` just to get around a design mismatch without documenting the real invariant.

## Validation

- Run lint, typecheck, and tests after changes.
- Add negative tests when schemas, auth paths, env handling, or serialization behavior changes.
