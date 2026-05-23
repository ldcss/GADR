# ADR 003: Creating or deciding a previously-retired split will merge variants from most recent creation migration

## Status

Accepted

## Context

As we rely more heavily on generated schemas for validation, undoing
destructive actions like deciding or creating a previously-retired split
could result in deviation between the schema and production, meaning
local/prod disparities in the form of missing variants in the schema
file.

While this is not ideal, it's not the end of the world. We'd like to
limit the impact of this scenario by merging in information from prior
migrations if available.

This stance attempts to balance the desire for correctness with the
ability to have schemas that don't grow indefinitely (by deleting retired
splits), as well as migration files that can be culled after they reach
a certain age to cut down on cognitive overhead for app maintainers.

## Decision

When reviving a retired split, the variants of the last creation of that
split will be merged into the set of variants reflected in the new
schema.

## Consequences

We won't be able to do this if the migration is missing. Schema and prod
state will diverge, but again, not probably a huge deal, fixable by
manually creating the split with those variants again, and probably
temporary regardless when we eventually retire the split again.

There is an O(N) performance cost over the number of migrations for
new split creations and decisions in this world. This doesn't seem
likely to hurt for a long time, if ever.
