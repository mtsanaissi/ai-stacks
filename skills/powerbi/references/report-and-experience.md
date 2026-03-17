# Report And Experience

## Layout And Navigation

- Keep page purpose obvious. Overview, detail, and drillthrough flows should be easy to follow without hidden navigation tricks.
- Keep slicer behavior, cross-filtering, and drill interactions predictable. Avoid interaction webs that make it hard to explain why a visual changed.
- When bookmarks or button-driven navigation are used, document the intended state transitions and what must stay synchronized.

## Accessibility And Readability

- Preserve contrast, heading hierarchy, alt text, and clear visual labels. Accessibility regressions are product regressions.
- Check mobile layout separately when the report is used on phones or embedded responsive surfaces.
- Keep titles and labels business-readable, not measure-name shorthand copied directly from the semantic model.

## Export And Embedded Concerns

- Review export, print, Analyze in Excel, and subscription behavior when visuals or filters change. The exported shape can expose more than the on-screen view suggests.
- Check tooltip pages, drillthrough pages, and hidden supporting pages for naming, leakage, and stale filters.
- For embedded reports, keep auth assumptions, tenant context, and role-aware navigation explicit in the docs and validation notes.

## Consistency

- Keep shared visuals, filters, color meaning, and page structure consistent across reports that belong to the same product surface.
- When interaction behavior changes, update user-facing release notes or training material if the report is widely used.
