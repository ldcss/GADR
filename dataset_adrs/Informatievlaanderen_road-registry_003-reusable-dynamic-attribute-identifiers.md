# 3. Reusable Dynamic Attribute Identifiers

Date: 2021-02-15

## Status

Accepted

## Context

Lanes, Widths, Surfaces are dynamic attributes which might change both in number and attributes over the life time of a road segment.
Each lane, width, surface is identified using an attribute identifier.
Handing out a new attribute identifier upon each change could cause us to exhaust the attribute identifier space rapidly.

## Decision

We keep track of all the attribute identifiers we have handed out for a road segment.
We do this for Lanes, Widths and Surfaces separately.
Upon each change in the number of dynamic attributes we try to exhaust the previously used identifiers first, that is we reuse them.
If additional attribute identifiers are needed we allocate them, continuing with the next free attribute identifier across road segments.
As soon as an identifier is allocated, it becomes dedicated to the road segment.
It remains so even after a road segment was removed.

## Consequences

We can now reduce the rate at which we consume attribute identifiers.
The downside being this is now behavior that downstream consumers need to take into account.
A future improvement could involve pooling identifiers of removed road segments.
