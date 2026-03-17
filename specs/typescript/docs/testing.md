# TypeScript Testing

- Prefer fast unit tests for logic-heavy modules.
- Add integration tests where contracts cross process, package, or network boundaries.
- Add negative tests for validators, config parsing, and auth-sensitive inputs.
- Run `npm run typecheck` in CI alongside tests.
- Tests should assert behavior, not implementation details.
