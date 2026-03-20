# Python Testing

Keep validation expectations explicit in the copied project.

Recommended conventions:

- Keep the project's automated test entry points documented in one place, especially if different change types use different commands.
- Run the repo's defined validation steps for every non-trivial change.
- Prefer fast unit tests plus focused integration tests around subprocesses, config loading, serialization, and external service boundaries.
- Test both success and important failure paths, especially for malformed input, auth failures, and unsafe payload handling.
- Keep fixtures small and readable; avoid hidden global state that changes import or runtime behavior.
- Document any manual verification steps that cannot be automated yet.
