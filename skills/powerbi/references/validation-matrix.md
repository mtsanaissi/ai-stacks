# Validation Matrix

Use the smallest validation set that still proves the changed surface is safe.

## Docs-Only Changes

- Re-read the affected instructions or template docs for contradictions against the rest of the stack template.
- Verify copied-template guidance still makes sense without the repo-local `powerbi` skill.

## Semantic Model Or DAX Changes

- Re-test the affected measures, totals, and filter behavior in the intended report context.
- Re-check relationship direction, grain assumptions, and any RLS or OLS interaction that the change could affect.
- Confirm downstream docs still describe the model accurately.

## Report UX Changes

- Verify the affected navigation, slicers, drillthrough, bookmarks, and cross-filter behavior manually.
- Check accessibility-sensitive surfaces such as titles, labels, contrast, and mobile layout when applicable.
- Re-check export or subscription output if the changed visual surface participates in those flows.

## Governance, Access, Or Service Changes

- Re-test viewer access with the correct role, not only with elevated workspace roles.
- Verify export, Analyze in Excel, embedded auth, refresh, gateway, and publishing behavior for the surfaces that changed.
- Call out any checks that require tenant admin help, service credentials, or manual production confirmation.
