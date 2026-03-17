# Recommended Project Docs

After copying the template, keep a small set of project docs that explain the real system rather than leaving everything in agent instructions.

Recommended files:

- `docs/product-overview.md`
- `docs/architecture.md`
- `docs/auth-and-roles.md`
- `docs/data-access.md`
- `docs/deployment.md`

Kickoff headings:

## `docs/product-overview.md`

- Purpose
- Main user journeys
- Out-of-scope behavior

## `docs/architecture.md`

- App surfaces and route groups
- External services
- Rendering and cache boundaries
- Background jobs or webhooks

## `docs/auth-and-roles.md`

- Identity provider
- Session model
- Roles and permissions
- Tenant or account boundaries

## `docs/data-access.md`

- Primary data stores
- Server-only integrations
- Caching and invalidation rules
- Data ownership assumptions

## `docs/deployment.md`

- Hosting target
- Required environment variables
- Build-time versus runtime config
- Release and rollback notes
