# Gemini CLI Instructions For Next.js Projects

Use this file as the Gemini CLI instruction file for a Next.js project.

## Scope

- Follow `docs/project-structure.md`, `docs/naming-and-comments.md`, `docs/recommended-docs.md`, `docs/testing-and-validation.md`, and `docs/deployment.md`.
- Use the repo-local `nextjs` skill when available and the task is materially about Next.js routing, rendering, caching, Server Actions, Route Handlers, or deployment behavior; otherwise follow the docs listed above directly.
- Assume App Router patterns unless the repo already uses Pages Router in the affected area.

## Commands

- Install: `npm install`
- Dev: `npm run dev`
- Lint: `npm run lint`
- Test: `npm test`

## Non-Negotiables

- Verify actual `next`, `react`, and adapter versions before using APIs, config keys, or examples. AI agents often mix guidance across major versions.
- Do not mix App Router, Pages Router, and ad hoc custom server patterns in the same feature unless the repo already does.
- Ask before changing auth flows, session storage, CSP, caching scope, cross-origin behavior, runtime targets, or deployment assumptions.
- Keep server-only code, secrets, and privileged data flows out of client bundles.

## Validation

- Run lint and tests after changes.
- When changing auth, Server Actions, Route Handlers, headers, caching, or runtime boundaries, also verify the affected flow manually.

## Tool-Specific Notes

- Gemini CLI should route to the `nextjs` skill for framework-specific work and avoid speculative framework rewrites in the thin root instructions.
