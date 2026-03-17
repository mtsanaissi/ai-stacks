# Client Boundaries

Prefer Server Components by default and widen the client boundary only when the interaction actually requires it.

## Rules

- Add `"use client"` at the narrowest practical boundary.
- Do not import server-only modules, admin clients, or privileged helpers into Client Components.
- Pass only the serialized data the client needs; avoid pushing whole domain objects across the React Server Component boundary.
- Keep browser-only dependencies isolated so the rest of the tree can stay server-rendered.
- Avoid `dangerouslySetInnerHTML` with user-controlled content. If raw HTML is unavoidable, sanitize on the server and document the trusted source.

## Review Hotspots

- Layouts or top-level route segments marked with `"use client"` for a small interactive child.
- Shared utility modules that mix browser helpers with server-only logic.
- Props that include secrets, tokens, or internal identifiers that only server code should see.
- Interactive wrappers that cause large data payloads to serialize into the client tree.

## Common Mistakes

- Marking a whole subtree as client-rendered because one child needs state.
- Passing privileged feature flags or internal role details that the browser does not need.
- Relying on client state to preserve auth-sensitive invariants after initial render.
