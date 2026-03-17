# Governance And Service

## Access Model

- Treat workspace role assignments, app audiences, sharing links, and semantic model permissions as first-class product behavior.
- RLS applies only to Viewer role consumers. Admins, Members, and Contributors bypass RLS, so do not use their experience as end-user proof.
- Do not promise RLS isolation for service principals. Service principals cannot be members of RLS roles, so embedded multitenancy needs an explicit identity and isolation design.
- OLS, Build permission, Analyze in Excel, export controls, and downstream dataset reuse need separate review. One control does not imply the others.

## Tenant And Governance Controls

- Verify exact Fabric and Power BI capability names, preview status, and licensing requirements before documenting or automating them.
- Do not treat sensitivity labels, DLP, audit logs, or endorsement metadata as access control inside the service.
- Scope service principals through dedicated security groups and least-privilege workspace access. Avoid tenant-wide enablement unless the requirement is explicit and documented.
- Keep secrets and certificates out of PBIX files, scripts, notebooks, pipeline variables, screenshots, and sample docs.

## Refresh, Gateway, And Deployment

- Document data sources, credential owners, gateway dependencies, refresh windows, and failure escalation paths for every governed change.
- Restrict gateway installers and owners to trusted operators. Gateway admins control shared data-source permissions and credential flows.
- When incremental refresh, DirectQuery, composite models, or Fabric pipeline promotion changes, note the operational preconditions and rollback path.
- Treat publishing, app updates, deployment pipelines, and embedded rollout as release surfaces, not just a file-copy step.

## Change Review Hotspots

- Re-check lineage, downstream dependencies, and app audiences when renaming semantic models, measures, or report pages used by consumers.
- Treat changes to export, download, subscriptions, or embedded access as security changes, not only usability changes.
- Record whether a change requires tenant admin coordination, gateway operator action, or workspace-permission updates.
