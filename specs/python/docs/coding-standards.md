# Python Coding Standards

Keep the copied project boring to import, easy to test, and explicit about trust boundaries.

Recommended conventions:

- Prefer explicit modules and package boundaries over metaprogramming-heavy patterns or import hacks.
- Use type hints for new and modified code, but treat them as documentation unless runtime validation is added explicitly.
- Keep domain logic free of framework-specific request, ORM, or transport objects where practical.
- Isolate IO, subprocess calls, environment reads, and external service clients behind clear boundary modules.
- Keep configuration loading centralized and typed instead of scattering `os.getenv()` calls across the codebase.
- Prefer narrow exception handling over `except Exception`, especially around auth, payment, queue, and network boundaries.
- Keep secrets, PII, and internal hostnames out of logs, reprs, fixtures, and committed examples.
