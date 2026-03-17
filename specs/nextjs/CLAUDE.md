# Claude Code Instructions For Next.js Projects

Use this file as the Claude Code project memory for a Next.js project.

## Scope

- Follow `docs/app-router.md`, `docs/server-actions.md`, `docs/ui-patterns.md`, `docs/performance.md`, and `docs/deployment.md`.
- Assume App Router patterns unless the repo already uses Pages Router in the affected area.
- Keep server, client, and edge runtime boundaries explicit.

## Commands

- Install: `npm install`
- Dev: `npm run dev`
- Lint: `npm run lint`
- Test: `npm test`

## Non-Negotiables

- Verify actual `next`, `react`, and adapter versions before using APIs, config keys, or examples. AI agents often mix guidance across major versions.
- Do not mix App Router, Pages Router, and ad hoc custom server patterns in the same feature unless the repo already does.
- Ask before changing auth flows, session storage, CSP, caching scope, cross-origin behavior, or deployment/runtime targets.

## Security and Data Handling

- Treat every Server Action and Route Handler as a public endpoint. Re-authenticate, authorize, validate input, and return the minimum data required.
- Keep secrets, admin SDKs, database clients, and privileged fetch logic in server-only modules. Never import them into Client Components or pass them through serialized props.
- Do not trust hidden form fields, closure-captured values, or client state for authorization. Derive user and tenant identity from trusted server state on every mutation.
- Validate `FormData`, search params, headers, cookies, webhook payloads, and uploaded file metadata on the server. Client validation is UX, not a trust boundary.
- Do not use `dangerouslySetInnerHTML` with user-controlled content. If raw HTML is unavoidable, sanitize it on the server, document the trusted source, and keep CSP strict.
- Prefer strict CSP with explicit allowances. Avoid broad `script-src`, `style-src`, or wildcard third-party domains just to make an example work.
- When Server Actions run behind proxies or alternate origins, review `serverActions.allowedOrigins` deliberately and keep request body limits tight.
- Do not expose raw stack traces, SQL errors, access tokens, signed URLs, or environment-derived values in rendered UI, API responses, logs, or telemetry.

## Stack-Specific Failure Modes

- Prefer Server Components by default. Adding `"use client"` high in the tree is a security and performance regression because it widens the client bundle and can pull privileged code into unsafe boundaries.
- Keep cache behavior explicit. Never let user-specific, tenant-specific, or permission-scoped data leak through static rendering, shared caches, or over-broad `revalidatePath` and `revalidateTag` calls.
- Do not broaden image, script, or font allowlists to `*`. Keep remote origins explicit and review them like any other inbound trust boundary.
- If sensitive objects may cross the React Server Component boundary, use server-only modules and consider React taint protections where the stack supports them.
- Do not hardcode secrets inside Server Actions or other server functions. Recent React Server Components advisories showed that stale or vulnerable code paths can turn source exposure into secret exposure.
- Validate auth and mutation behavior from the server side. A green client interaction test is not evidence that the endpoint is secure.

## Validation

- Run lint and tests after changes.
- When changing auth, Server Actions, headers, caching, or runtime boundaries, also verify the affected flow manually.

## Tool-Specific Notes

- Claude Code should preserve Next.js runtime boundaries and refuse convenience changes that weaken server-side enforcement.
