# Claude Code Instructions For Next.js Projects

Use this file as the Claude Code project memory for a Next.js project.

## Scope

- Follow `docs/app-router.md`, `docs/server-actions.md`, `docs/ui-patterns.md`, `docs/performance.md`, and `docs/deployment.md`.
- Prefer App Router patterns.
- Keep server and client boundaries deliberate.

## Commands

- Install: `npm install`
- Dev: `npm run dev`
- Lint: `npm run lint`
- Test: `npm test`

## Change Rules

- Do not make behavior-changing or user-visible assumptions. Ask for clarification when intent is ambiguous or impact is material.
- Prefer existing project patterns over inventing new abstractions.
- Call out bad practices, risky shortcuts, or changes that diverge from common Next.js conventions.
- Reuse existing components, hooks, utilities, schemas, and route patterns when they fit.
- Add new abstractions only when they clearly improve reuse, consistency, or maintainability.
- Prefer Server Components by default.
- Add `"use client"` only when interactivity requires it.
- Validate form inputs on the server.

## Tool-Specific Notes

- Claude Code should preserve Next.js server-client boundaries and app-router conventions.
