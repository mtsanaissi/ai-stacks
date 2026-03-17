# Python Testing

Keep validation expectations explicit in the copied project.

Recommended conventions:

- Use pytest as the default test runner unless the project already has a stronger reason not to.
- Run lint, typecheck, and the relevant test targets for every non-trivial change.
- Prefer fast unit tests plus focused integration tests around subprocesses, config loading, serialization, and external service boundaries.
- Test both success and important failure paths, especially for malformed input, auth failures, and unsafe payload handling.
- Keep fixtures small and readable; avoid hidden global state that changes import or runtime behavior.
- Document any manual verification steps that cannot be automated yet.
