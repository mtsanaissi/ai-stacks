# DAX Standards

Keep semantic model logic readable, reusable, and reviewable.

Recommended conventions:

- Prefer measures over calculated columns unless the value truly belongs at refresh time.
- Keep measure names business-readable and consistent with report labels.
- Factor repeated logic into reusable base measures instead of near-duplicate report-specific expressions.
- Use variables when they make filter-context transitions or intermediate logic easier to review.
- Document time-intelligence assumptions such as the date table, fiscal calendar, inactive relationships, or custom period logic.
- Review `ALL`, `ALLEXCEPT`, `ALLSELECTED`, `REMOVEFILTERS`, disconnected tables, and ranking patterns carefully when they affect secured or exported data.
- Add or update descriptions for important shared measures so downstream report authors understand intended use.
