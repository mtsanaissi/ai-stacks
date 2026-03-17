---
name: nextjs
description: Use this skill when the task is materially about Next.js application structure, App Router behavior, Route Handlers, Server Actions, server and client boundaries, caching and revalidation, rendering behavior, security headers, or deployment/runtime choices in a Next.js project.
---

# Next.js

Use this skill for implementation, debugging, refactoring, and review work where Next.js behavior materially affects the answer.

Do not use this skill for generic TypeScript, CSS, or React tasks unless Next.js routing, runtime, deployment, or cache behavior is part of the work.

## Before You Change Code

1. Inspect the installed `next`, `react`, and adapter versions before using framework-specific APIs or config.
2. Check whether the affected area uses App Router, Pages Router, or a hybrid layout.
3. Read [references/task-routing.md](references/task-routing.md) first, then load only the referenced files that match the task.

## Reference Routing

- Read [references/server-boundaries.md](references/server-boundaries.md) for Server Actions, Route Handlers, auth-sensitive mutations, forms, uploads, cookies, headers, and webhook entry points.
- Read [references/cache-and-data-safety.md](references/cache-and-data-safety.md) for fetching, revalidation, static rendering, streaming, and user-specific data safety.
- Read [references/client-boundaries.md](references/client-boundaries.md) for `"use client"`, React Server Components, browser-only libraries, serialization boundaries, and UI composition tradeoffs.
- Read [references/deployment-and-security.md](references/deployment-and-security.md) for CSP, allowed origins, remote asset allowlists, runtime targets, environment handling, and deployment concerns.
- Read [references/validation-matrix.md](references/validation-matrix.md) before closing work so the validation matches the change.

## Workflow

1. Inspect local versions, config, and existing route/runtime patterns.
2. Load only the references that match the task shape.
3. Preserve server and client boundaries instead of flattening them for convenience.
4. Make the smallest change that fits the existing project shape.
5. Run the relevant validation from the validation matrix.
6. Report any remaining security, caching, or deployment risk explicitly.

## Common Failure Modes

- Mixing App Router and Pages Router patterns in the same feature without checking the repo.
- Treating TypeScript types or client validation as sufficient for trust boundaries.
- Moving privileged code into client bundles through a broad `"use client"` boundary.
- Forgetting that Server Actions and Route Handlers are public entry points.
- Leaking user-specific or tenant-specific data through shared caches, static rendering, or over-broad revalidation.
- Hallucinating Next.js config keys, React APIs, or runtime behavior from a different major version.

## Output Expectations

- Name the Next.js boundary being changed: route, component tree, action, handler, cache scope, or deployment surface.
- Call out any version-sensitive assumptions.
- If auth, caching, origins, or CSP changed, say what was verified and what still needs manual confirmation.
