# TypeScript Tooling

- Pick one package manager for the repo and commit its lockfile.
- Keep `tsconfig` strict and document any deliberate deviations from the default safety settings.
- Default package manager: `npm` unless the project states otherwise.
- Default linting: ESLint.
- Default typecheck: `tsc --noEmit`.
- Default test runner: Vitest.
- Keep `package.json` scripts, CI commands, and agent docs aligned.
