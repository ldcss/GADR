# Normalize IDs

## Status

Accepted

## Context

Identifiers in API responses are inconsistent.

See [here]() vs [here]() and [here]().

## Decision

In all resource classes, both `id` and `uid` fields will be mapped to the `id` property.

## Consequences

Accessing the ID field becomes consistent across resource types. You no longer need to remember which calls return an `id` vs a `uid`.

The downside to this is we deviate from the vercel API. This makes a little bit hard to go back and forth.