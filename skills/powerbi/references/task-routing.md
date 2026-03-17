# Task Routing

Read this file first, then load only the references that match the task.

## Semantic Model Or DAX Work

Load [modeling-and-dax.md](modeling-and-dax.md) when the task touches:

- star schema design, grain, relationship direction, or bridge-table choices
- calculated columns, measures, calculation groups, time intelligence, or KPI logic
- filter-context changes, disconnected tables, drillthrough data shaping, or totals behavior
- naming, foldering, descriptions, or semantic model maintainability

Also read [validation-matrix.md](validation-matrix.md).

## Governance, Refresh, Or Service Configuration

Load [governance-and-service.md](governance-and-service.md) when the task touches:

- workspace roles, RLS, OLS, audiences, app permissions, or sharing behavior
- service principals, embedding, tenant settings, export controls, labels, or audit assumptions
- gateways, data source credentials, scheduled refresh, incremental refresh, or deployment pipelines
- publishing flow, lineage, promotion across environments, or incident rollback expectations

Also read [validation-matrix.md](validation-matrix.md).

## Report UX Or Embedded Consumption

Load [report-and-experience.md](report-and-experience.md) when the task touches:

- page layout, navigation, visual interaction, slicers, drillthrough, bookmarks, or tooltips
- accessibility, contrast, screen-reader labels, mobile layout, or export readability
- embedded report behavior, viewer journeys, role-aware navigation, or cross-report consistency

Also read [validation-matrix.md](validation-matrix.md).

## Docs-Only Or Template Guidance Updates

Load only the references that match the documented surface:

- use [modeling-and-dax.md](modeling-and-dax.md) for model and DAX guidance
- use [governance-and-service.md](governance-and-service.md) for service and access guidance
- use [report-and-experience.md](report-and-experience.md) for report UX guidance

If the docs change operating expectations, still read [validation-matrix.md](validation-matrix.md) so the closeout lists the right checks or intentional non-checks.
