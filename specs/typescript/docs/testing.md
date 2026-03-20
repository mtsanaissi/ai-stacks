# TypeScript Testing

- Prefer fast unit tests for logic-heavy modules.
- Add integration tests where contracts cross process, package, or network boundaries.
- Add negative tests for validators, config parsing, and auth-sensitive inputs.
- Run the repo's typecheck step in CI alongside tests when the project defines one. The starter template uses `npm run typecheck`.
- Tests should assert behavior, not implementation details.
