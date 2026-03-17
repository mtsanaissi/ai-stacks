# Tooling And Config Safety

TypeScript configuration changes are behavior changes. Treat them as such.

## Rules

- Verify actual package exports, script names, and runtime behavior before using examples from docs or older repos.
- If `tsconfig` changes, tighten rather than relax. Preserve safeguards such as `strict`, `exactOptionalPropertyTypes`, and `noUncheckedIndexedAccess` when they already exist.
- Ask before changing package manager, build targets, module format, or published export structure.
- Commit lockfiles and prefer reproducible installs for automation and CI.
- Keep module-resolution choices aligned with the real runtime, bundler, and test runner.

## Review Hotspots

- `tsconfig` changes that reduce strictness or mask import-resolution problems.
- New dependencies added for small tasks without checking whether the repo already has an accepted pattern.
- Script changes in `package.json` that drift from docs, CI, or agent instructions.
- Export map or path-alias changes that may break downstream consumers or tests.

## Common Mistakes

- Using looser compiler settings to hide a module or design bug.
- Assuming `npm` examples apply unchanged to a `pnpm`, `bun`, or workspace-managed repo.
- Changing export paths or module format without validating consumer imports and test execution.
