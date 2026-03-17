# Testing And Validation

Keep validation expectations explicit in the copied project.

Recommended conventions:

- Run lint and the project test suite for every non-trivial change.
- Add targeted tests for route handlers, server actions, and data-shaping helpers when they enforce business rules or trust boundaries.
- Add manual verification steps for auth, caching, uploads, webhooks, and security headers when those areas change.
- Keep mock setup lightweight and favor tests that exercise real route ownership and data boundaries.
- Document any manual release checks that cannot be automated yet.
