# Runtime And Input Safety

TypeScript only protects checked code paths. Untrusted input still needs runtime enforcement.

## Rules

- Validate all untrusted input at the process, API, message, or CLI boundary.
- Keep environment variable parsing centralized and fail fast on invalid config.
- Do not suppress security-relevant type errors with `any`, `@ts-ignore`, `as unknown as`, or blanket non-null assertions.
- Avoid `eval`, `new Function`, dynamic `vm` execution, and dynamic imports or requires that are derived from user input or mutable config.
- Guard against prototype pollution and unsafe object merges when traversing user-controlled structures.

## Review Hotspots

- Request or message handlers that type a payload but do not validate it.
- `process.env.FOO!` spread across the codebase instead of a single config bootstrap.
- JSON parsing or object merging paths that trust arbitrary keys.
- Helper modules that accept `unknown` or `any` and immediately cast to domain types.

## Common Mistakes

- Assuming a passing browser or happy-path test proves the server boundary is safe.
- Suppressing a type error instead of narrowing or validating the boundary.
- Trusting third-party payloads, webhook metadata, or config files because an interface compiles.
