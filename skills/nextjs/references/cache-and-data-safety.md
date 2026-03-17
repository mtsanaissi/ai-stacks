# Cache And Data Safety

Cache behavior is a security and correctness concern, not only a performance concern.

## Rules

- Keep cache scope explicit for every fetch and route.
- Never let user-specific, tenant-specific, or permission-scoped data rely on shared static output unless the cache key or rendering mode is explicitly safe.
- Use `revalidatePath` and `revalidateTag` narrowly. Revalidate only the surfaces affected by the mutation.
- Prefer server-side data fetching over moving large payloads into client components.
- Review suspense and streaming boundaries when sensitive data or role-specific UI is involved.

## Review Hotspots

- Adding static rendering to routes that read session, cookie, or tenant context.
- Fetch helpers with implicit caching behavior used by both public and private pages.
- Over-broad tag reuse across unrelated data domains.
- Dashboard pages that aggregate both public and private data in the same tree.

## Common Mistakes

- Assuming a page is safe to cache because the top-level route is authenticated.
- Revalidating a parent path that also serves other users or tenants.
- Forgetting that a convenience fetch wrapper can change caching behavior for many routes at once.
