# Modeling And DAX

## Semantic Model Boundaries

- Prefer explicit star-schema ownership. Make fact grain, dimension grain, and surrogate-key assumptions obvious in docs and review notes.
- Prefer single-direction filters unless a reviewed exception is required. Bidirectional filters and ambiguous relationship paths raise both correctness and security risk.
- Keep relationship intent easy to inspect. Avoid hidden many-to-many behavior unless the business rule genuinely needs it and the tests cover it.
- Treat source-system cleanup, semantic calculations, and report-only formatting as separate concerns where possible.

## Measure Design

- Prefer measures over calculated columns unless the value truly belongs at refresh time and the storage cost is acceptable.
- Name base measures, reusable helper measures, and presentation measures consistently so reviewers can see reuse instead of duplicated logic.
- Use variables when they improve readability or prevent repeated expensive expressions.
- Keep time-intelligence assumptions explicit. Do not assume the date table, fiscal calendar, or inactive-relationship strategy matches a generic example.

## Filter Context And Data Exposure

- Review `ALL`, `ALLEXCEPT`, `ALLSELECTED`, `REMOVEFILTERS`, disconnected tables, and custom ranking logic carefully. These patterns can bypass the intended shape of restricted views.
- Check totals, subtotals, drillthrough pages, tooltips, and exported detail for leakage, not only the main visual state.
- If a measure relies on `USERELATIONSHIP`, inactive relationships, or virtual relationships, document the intended path and failure mode.

## Maintainability

- Keep display folders, descriptions, and naming aligned with the business language used in the report.
- Prefer a smaller set of well-named reusable measures over many near-duplicate report-local calculations.
- When a change affects grain, relationships, or time logic, update the model documentation and downstream report assumptions together.
