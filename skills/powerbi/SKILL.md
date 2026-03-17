---
name: powerbi
description: Use this skill when the task is materially about Power BI or Fabric semantic models, DAX, report interaction, row-level or object-level security, refresh and gateway behavior, deployment flow, embedded analytics, or workspace and tenant governance choices.
---

# Power BI

Use this skill for implementation, debugging, refactoring, documentation, and review work where Power BI or Fabric behavior materially affects the answer.

Do not use this skill for generic SQL, warehouse modeling, or frontend tasks unless Power BI semantic models, report behavior, or service governance are part of the work.

## Before You Change Artifacts

1. Inspect the repo assets and target surface first: PBIX, TMDL, Tabular Editor metadata, Fabric items, deployment scripts, or docs-only guidance.
2. Confirm whether the task affects Desktop-only workflows, Fabric service operations, embedded analytics, or tenant governance.
3. Read [references/task-routing.md](references/task-routing.md) first, then load only the referenced files that match the task.

## Reference Routing

- Read [references/modeling-and-dax.md](references/modeling-and-dax.md) for semantic model grain, relationships, naming, measure design, filter-context handling, and risky DAX patterns.
- Read [references/governance-and-service.md](references/governance-and-service.md) for workspace roles, RLS and OLS limits, service principals, gateways, refresh, deployment flow, and tenant-level controls.
- Read [references/report-and-experience.md](references/report-and-experience.md) for report layout, interaction design, accessibility, bookmarks, drillthrough, export-sensitive UX, and embedded consumption concerns.
- Read [references/validation-matrix.md](references/validation-matrix.md) before closing work so the validation matches the change.

## Workflow

1. Inspect the actual repo artifacts, target environment, and tenant or licensing assumptions before proposing stack-specific changes.
2. Load only the references that match the task shape.
3. Preserve semantic model, report, and service-governance boundaries instead of flattening them for convenience.
4. Make the smallest change that fits the existing project shape and documented release process.
5. Run the relevant validation from the validation matrix.
6. Report any remaining governance, security, tenant, or refresh risk explicitly.

## Common Failure Modes

- Treating Admin, Member, or Contributor testing as proof that RLS works for viewers.
- Assuming sensitivity labels, DLP, or audit settings replace Power BI permissions.
- Introducing bidirectional filters, ambiguous relationships, or `ALL` and `REMOVEFILTERS` logic without re-checking data-exposure risk.
- Guessing Fabric capability names, licensing requirements, preview availability, or tenant settings instead of verifying them.
- Treating report-only changes as harmless when drillthrough, export, bookmarks, Analyze in Excel, or embedding behavior also changes.
- Closing governed work without documenting refresh, gateway, lineage, publishing, or workspace-impact changes.

## Output Expectations

- Name the Power BI surface being changed: semantic model, DAX layer, report UX, workspace or service configuration, refresh or deployment path, or embedded auth boundary.
- Call out any tenant-sensitive, licensing-sensitive, or preview-sensitive assumptions.
- If RLS, OLS, export, gateway, refresh, service principal, or workspace access changed, say what was verified and what still needs manual tenant confirmation.
