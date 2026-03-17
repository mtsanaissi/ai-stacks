# Deployment And Security

## Rules

- Prefer strict CSP with explicit allowances; do not widen directives to `*` just to satisfy an example.
- Keep image, script, font, and third-party origin allowlists explicit and reviewable.
- Review `serverActions.allowedOrigins` deliberately when proxies or alternate origins are involved.
- Keep environment handling explicit. Document which values are build-time, runtime, server-only, or intentionally public.
- Ask before changing edge versus node runtime, session storage model, cross-origin behavior, or hosting assumptions.

## Review Hotspots

- Broad `script-src`, `style-src`, or remote asset patterns.
- Environment variables moved from server-only usage into client-visible configuration.
- Runtime changes that break existing Node libraries, auth middleware, or logging expectations.
- Deployment-specific code paths that only work in preview or only work in production.

## Common Mistakes

- Adding wildcard remote patterns instead of the one host actually required.
- Assuming preview and production have the same header, cookie, and origin behavior.
- Moving secrets into code paths that can be serialized or logged accidentally.
