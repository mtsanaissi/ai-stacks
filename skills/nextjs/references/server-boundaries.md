# Server Boundaries

Treat every Server Action and Route Handler as a public endpoint.

## Rules

- Re-authenticate, authorize, validate input, and return the minimum data required.
- Keep secrets, admin SDKs, database clients, and privileged fetch logic in server-only modules.
- Do not trust hidden form fields, closure-captured values, or client state for identity, role, or tenant selection.
- Validate `FormData`, search params, headers, cookies, webhook payloads, and uploaded file metadata on the server.
- Do not leak stack traces, SQL errors, signed URLs, tokens, or environment-derived secrets in responses or logs.

## Review Hotspots

- Actions or handlers that infer authorization from client-submitted IDs.
- Mutations that update multiple resources without obvious ownership checks.
- Upload handlers that trust file names, MIME types, or metadata from the client.
- Webhooks that skip signature verification or rely only on origin or IP assumptions.
- Shared helper modules that are imported by both server and client code.

## Common Mistakes

- Moving validation from the server to the client because the form already uses schema validation.
- Returning full ORM objects when only one field or status is needed.
- Storing privileged service clients in modules that can be pulled into client bundles indirectly.
- Treating a passing browser test as evidence that the server endpoint is secure.
