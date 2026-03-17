# Type And API Boundaries

Public types are contracts. Runtime validators and serialization behavior must move with them.

## Rules

- Update schemas, validators, serializers, and declared types together.
- Prefer discriminated unions, branded IDs, and narrow exported interfaces for auth, tenant, and resource ownership boundaries.
- Do not widen exported contracts to `string`, `Record<string, unknown>`, or `unknown` just to hide a design mismatch.
- Keep external transport types distinct from trusted domain models when the invariants differ.
- Document the real invariant when a boundary must stay broader for compatibility.

## Review Hotspots

- API or event payload types changed without matching parser or serializer updates.
- Generated or inferred types are being used as if they enforce runtime guarantees.
- Privileged boundaries modeled as generic dictionaries or optional fields.
- Domain unions replaced with free-form strings to avoid narrowing logic.

## Common Mistakes

- Casting parsed JSON directly to a domain type.
- Treating a shared interface as proof that every producer and consumer validates the same shape.
- Exporting one overly-broad type because multiple call sites disagree on the real contract.
