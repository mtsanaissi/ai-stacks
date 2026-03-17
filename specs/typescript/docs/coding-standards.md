# TypeScript Coding Standards

- Use strict TypeScript settings and document any deliberate exceptions in the repo.
- Prefer discriminated unions, branded types, and narrow public interfaces for meaningful domain boundaries.
- Keep validators, serializers, and declared types aligned at API, message, and config boundaries.
- Keep side effects and runtime-specific code near the edge of the system.
- Centralize environment variable parsing instead of scattering raw `process.env` reads.
