# Tooling And Config Safety

## Rules

- Verify actual package exports, script names, and runtime behavior before using examples from docs or older repos.
- If config changes, preserve existing safety checks unless the change deliberately documents why a relaxation is required.
- Ask before changing the repo's install flow, build targets, module format, or published export structure.
- Commit lockfiles and prefer reproducible installs for automation and CI.
- Keep module-resolution choices aligned with the real runtime, bundler, and test runner.

## Review Hotspots

- Config changes that reduce safety checks or mask import-resolution problems.
- New dependencies added for small tasks without checking whether the repo already has an accepted pattern.
- Script changes in `package.json` that drift from docs, CI, or agent instructions.
- Export map or path-alias changes that may break downstream consumers or tests.

## Common Mistakes

- Using looser compiler settings to hide a module or design bug.
- Assuming one install-flow example applies unchanged to a different repo setup.
- Changing export paths or module format without validating consumer imports and test execution.
