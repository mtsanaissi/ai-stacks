# Gemini CLI Instructions For Python Projects

Use this file as the Gemini CLI instruction file for a Python project.

## Scope

- Follow `docs/coding-standards.md`, `docs/testing.md`, `docs/tooling.md`, and `docs/packaging.md`.
- Prefer type hints for new and changed code.
- Keep side effects explicit and isolate IO.

## Commands

- Setup: `uv sync`
- Lint: `uv run ruff check .`
- Typecheck: `uv run pyright`
- Test: `uv run pytest`

## Non-Negotiables

- Verify real package APIs and version-specific behavior before coding. AI agents often mix stdlib, framework, and library guidance across versions.
- Ask before changing auth flows, credential storage, packaging entry points, database migrations, or deployment/runtime assumptions.
- Keep trust boundaries obvious. Validation belongs at entry points, not after the data has already crossed half the codebase.

## Security and Data Handling

- Treat type hints as documentation, not enforcement. Validate and normalize untrusted input at the boundary.
- Never use `pickle`, `shelve`, or `multiprocessing.Connection.recv()` with untrusted data. Do not accept Python object graphs as a wire format across trust boundaries.
- Use `secrets` for tokens, reset links, API keys, and any security-sensitive randomness. Do not use `random` for security decisions.
- Do not use `http.server` for production or internet-facing traffic.
- Prefer `subprocess` argument lists over shell command strings. Avoid `shell=True`; if shell use is unavoidable, keep untrusted input out of command construction and escape explicitly.
- Treat attacker-controlled XML as hostile input. If XML must be parsed, bound size and parser behavior, and be aware of Expat version-related risks.
- Keep secrets, access tokens, PII, and internal hostnames out of logs, exception messages, reprs, fixtures, notebooks, and committed sample payloads.
- Do not accept logging configuration from untrusted sources. Python's logging configuration mechanisms can evaluate input.

## Stack-Specific Failure Modes

- Do not widen `sys.path`, rely on current-directory import precedence, or shadow stdlib module names to make imports "just work".
- Keep configuration loading centralized and typed. Avoid scattered `os.getenv()` calls with silent fallbacks for security controls.
- Avoid broad `except Exception` blocks around auth, payment, queueing, or network boundaries. Catch expected failures and preserve audit-relevant errors.
- Do not invent framework helpers, request objects, or Pydantic behaviors that are not present in the installed version.
- Prefer maintained dependencies with clear security posture. Do not add obscure packages or unreviewed code generators to save a small amount of boilerplate.
- When writing CLI or automation entry points, keep import-time side effects minimal and avoid leaking local machine state into tests.

## Validation

- Run lint, typecheck, and tests after changes.
- Add negative tests for malformed input, auth failures, subprocess boundaries, and serialization edges when those areas change.

## Tool-Specific Notes

- Gemini CLI should keep Python commands, packaging guidance, and validation expectations aligned with the installed stack, not copied examples.
