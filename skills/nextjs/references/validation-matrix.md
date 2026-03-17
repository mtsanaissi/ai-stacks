# Validation Matrix

Use the smallest validation set that still exercises the risk introduced by the change.

## Always

- Run project lint.
- Run the relevant automated tests.

## Server Actions, Route Handlers, Auth, Headers, and Origins

- Exercise the affected flow manually from the server boundary, not only from the UI.
- Verify malformed input and unauthorized access paths.
- Re-check cookies, headers, and origin assumptions when proxies or alternate domains are involved.

## Fetching, Caching, Or Rendering Changes

- Verify user-specific and tenant-specific data does not leak across sessions or route variants.
- Check the changed route before and after revalidation.
- Confirm dynamic versus static behavior matches the intended cache scope.

## Client Boundary Changes

- Confirm no server-only imports or secrets cross into the client bundle.
- Verify the browser-only behavior still works with the narrower client boundary.

## Deployment Or Runtime Changes

- Verify build and runtime configuration expectations explicitly.
- Check preview versus production assumptions if the change depends on hosting behavior.
