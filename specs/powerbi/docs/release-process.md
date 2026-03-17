# Release Process

Use this file as the project-facing record of how semantic models and reports move across environments.

Recommended sections:

- Source of truth for report and model artifacts
- Workspace targets and promotion path
- Gateway, data source, and credential ownership
- Refresh windows, failure handling, and escalation
- Validation and sign-off before publish
- Rollback or hotfix steps

Conventions:

- Document workspace targets, publishing steps, and app-update expectations.
- Track refresh dependencies, gateway assumptions, and who owns production credentials.
- Record manual validation steps for business-critical dashboards, especially for RLS, exports, and embedded paths.
- Note whether a change needs tenant admin review, gateway operator action, or stakeholder approval before release.
