# Project Structure

Use App Router as the default shape unless the project already relies on Pages Router in the affected area.

Recommended layout:

```text
app/
  (marketing)/
  (product)/
  api/
components/
  ui/
  <feature>/
lib/
  server/
  client/
  shared/
docs/
tests/
```

Conventions:

- Keep route-owned UI, loaders, and mutations close to the route segment that owns them.
- Keep `lib/server/` for server-only integrations, data access, and privileged helpers.
- Keep `lib/client/` for browser-only utilities.
- Keep `lib/shared/` small and safe to import from either side.
- Prefer feature folders over generic dumping grounds once a domain has more than a couple of files.
- Keep API route handlers, page components, and shared helpers separated clearly enough that ownership is obvious in review.
