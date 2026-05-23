# 15. Ouch solid js <For> caching

Date: 2022-03-30

## Status

Accepted

## Context

The `For` construct in solid js caches so that updating properties of rendered items does not work.

Looks like it is [caching items by reference](https://www.solidjs.com/docs/latest/api#maparray).

How is reference equality determined?

## Decision

Tried `Index` but it has the same issue.

Instead of updating fields in news items we need to replace with entirely new ones so that they are different references.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
