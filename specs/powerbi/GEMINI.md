# Gemini CLI Instructions For Power BI Projects

Use this file as the Gemini CLI instruction file for a Power BI project.

## Scope

- Follow `docs/modeling.md`, `docs/dax-standards.md`, `docs/report-design.md`, and `docs/release-process.md`.
- Prefer consistent naming, reusable measures, and documented refresh assumptions.
- Confirm whether the repo targets Desktop-only workflows, Fabric service operations, or embedded analytics before changing security assumptions.

## Non-Negotiables

- Ask before changing workspace roles, tenant settings, service principal access, gateway ownership, export permissions, or refresh credentials.
- Verify exact Fabric and Power BI capability names, licensing requirements, and preview status before documenting or automating them. AI agents frequently invent admin settings and DAX features.
- Treat semantic model security as a product requirement, not a report-design detail.

## Security and Data Governance

- Model access with least privilege. Row-level security only applies to Viewer role users. Admins, Members, and Contributors bypass RLS.
- Do not treat sensitivity labels as access control inside the service. Labels protect exported data paths and improve governance, but Power BI permissions still control in-service access.
- Use sensitivity labels, DLP, auditing, and export controls for sensitive data. Do not assume one control covers the others.
- Scope service principals through dedicated security groups and least-privilege workspace access. Do not enable broad tenant-wide API access unless explicitly required.
- Store service principal secrets and certificates in Key Vault or another managed secret store. Never hardcode them in PBIX files, scripts, notebooks, pipeline variables, or screenshots.
- Restrict gateway installers and owners to trusted operators. Gateway admins control shared data-source permissions and credential flows, so treat gateway ownership as privileged access.
- Minimize PII in semantic model names, column names, bookmarks, sample data, exported filenames, and screenshots checked into source.

## Stack-Specific Failure Modes

- Validate RLS with Test as role and with real Viewer accounts. Admin or Member testing is not evidence that end-user filtering works.
- Do not promise RLS isolation for service principals. Service principals cannot be added to RLS roles, so embedded multitenancy needs explicit identity and isolation design.
- Prefer star schema and single-direction filters unless a reviewed exception is required. Ambiguous relationships and bidirectional filters make security behavior hard to reason about.
- Review measures that use `ALL`, `REMOVEFILTERS`, disconnected tables, drillthrough pages, or export scenarios carefully. These patterns can reconstruct restricted data even when the main visuals look correct.
- Document data source, gateway, refresh, lineage, publishing, and sharing changes in every governed update.
- Treat export, Analyze in Excel, download, and embedding changes as security changes, not only UX changes.

## Validation

- Re-test viewer access and any RLS or OLS assumptions after model, relationship, or workspace changes.
- Verify export behavior, sensitivity labels, refresh, and embedded auth flows when those areas change.

## Tool-Specific Notes

- Gemini CLI should keep report, model, and publishing guidance aligned with real tenant constraints, not guessed platform behavior.
