# Claude Code Instructions For Power BI Projects

Use this file as the Claude Code project memory for a Power BI project.

## Scope

- Follow `docs/modeling.md`, `docs/dax-standards.md`, `docs/report-design.md`, and `docs/release-process.md`.
- Use the repo-local `powerbi` skill when available and the task is materially about semantic model design, DAX, report behavior, refresh, embedded analytics, or Power BI and Fabric governance; otherwise follow the docs listed above directly.
- Confirm whether the repo targets Desktop-only workflows, Fabric service operations, or embedded analytics before changing security assumptions.

## Non-Negotiables

- Ask before changing workspace roles, tenant settings, service principal access, gateway ownership, export permissions, or refresh credentials.
- Verify exact Fabric and Power BI capability names, licensing requirements, and preview status before documenting or automating them. AI agents frequently invent admin settings and DAX features.
- Treat semantic model security as a product requirement, not a report-design detail.
- RLS only constrains Viewer-role consumers. Admins, Members, and Contributors bypass it, so elevated-role testing is not end-user proof.
- Do not treat sensitivity labels as access control inside the service.

## Validation

- Re-test viewer access and any RLS or OLS assumptions after model, relationship, or workspace changes.
- Verify export behavior, refresh, gateway, and embedded auth flows when those areas change.

## Tool-Specific Notes

- Claude Code should route to the `powerbi` skill for Power BI-specific work and keep the always-hot guidance in this file minimal.
