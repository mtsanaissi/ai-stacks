# Task Routing

Read this file first, then load only the references needed for the current task.

## App Structure And Boundaries

Use [client-boundaries.md](client-boundaries.md) when the task involves:

- deciding whether code belongs in a Server Component or Client Component
- `"use client"` placement
- colocating route-owned UI, loaders, and mutations
- browser-only libraries, DOM APIs, or interactive widgets

## Mutations And Public Entry Points

Use [server-boundaries.md](server-boundaries.md) when the task involves:

- Server Actions
- Route Handlers
- forms and `FormData`
- cookies, headers, sessions, auth, or uploads
- webhooks or any endpoint that accepts third-party traffic

## Fetching, Rendering, And Revalidation

Use [cache-and-data-safety.md](cache-and-data-safety.md) when the task involves:

- `fetch` behavior
- static rendering versus dynamic rendering
- `revalidatePath` or `revalidateTag`
- suspense and streaming
- user-specific, tenant-specific, or permission-scoped data

## Deployment And Security Surface

Use [deployment-and-security.md](deployment-and-security.md) when the task involves:

- CSP or other security headers
- remote images, fonts, scripts, or asset allowlists
- `serverActions.allowedOrigins`
- edge versus node runtime
- environment variables and deployment differences

## Closing Work

Always read [validation-matrix.md](validation-matrix.md) before finishing implementation or review work.
