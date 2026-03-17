# Modeling

Use this file to document the intended semantic model shape after copying the template.

Recommended sections:

- Business entities and main facts
- Fact grain and dimension grain
- Relationship direction and any approved exceptions
- Naming and display-folder conventions
- Security boundaries such as RLS, OLS, or sensitive dimensions
- Refresh, lineage, and upstream source ownership

Conventions:

- Prefer star-schema design where practical.
- Keep fact and dimension responsibilities clear and document the grain explicitly.
- Prefer single-direction filters unless a reviewed exception is required.
- Record surrogate keys, bridge tables, inactive relationships, and calculation-group assumptions where they exist.
- Update this file when semantic model changes would affect report behavior, refresh, or downstream consumers.
