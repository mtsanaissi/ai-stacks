# Naming And Comments

Naming conventions:

- Use lowercase route segment names and reserve route groups for navigation or ownership boundaries, not arbitrary folder nesting.
- Name React components in PascalCase and colocate one primary component per file unless the file is intentionally tiny.
- Name hooks with a `use` prefix and keep them in client-safe modules.
- Name server-only helpers to make the boundary obvious when helpful, such as `getUserSession`, `createServerClient`, or `requireAdmin`.
- Keep schema, validator, and DTO names aligned with the domain language used by the route or feature.

Commenting conventions:

- Prefer comments that explain boundary decisions, security assumptions, cache scope, or framework constraints.
- Do not add comments that restate the code line-by-line.
- Add a short header comment before non-obvious Route Handlers, middleware, or mutation flows when reviewers would otherwise have to reconstruct the trust boundary.
- Use JSDoc or TSDoc for exported helpers when callers need to know runtime assumptions, cache behavior, or server-only constraints.
