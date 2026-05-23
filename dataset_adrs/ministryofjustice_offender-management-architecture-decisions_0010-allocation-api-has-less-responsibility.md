# 10. Allocation API has less responsibility

Date: 2018-11-20

## Status

Accepted

Amends [4. Separate API and user-facing applications](0004-separate-api-and-user-facing-applications.md)

Amended by [18. Unify API and Presentation layer](0018-unify-api-and-presentation-layer.md)

## Context

When we decided to start off with separate API and user-facing applications
(see [ADR 0004](0004-separate-api-and-user-facing-applications.md)) we thought
that we would need to build more than one service as part of this work, to
meet different needs of different users. That may still be true in general, but
from what we've learned in the Handover discovery it's looking more likely at
the moment that the Handover phase of our work will involve expanding on
Allocations rather than being an entirely separate journey and service.

We were also intending that the allocation manager would be a fairly minimal
user-facing application, which would fetch all the data it needed from the
allocation API and then render pages based directly on it.

We've been looking at how we should set up authentication on our two
applications and have realised that that split of responsibilities between the
allocation manager and API could lead to some confusions:

- Calling the Custody API from the allocation API means that the allocation API
  can be seen as sitting in two different layers depending on the context:
  either above the Custody API from the point of view of the allocation manager,
  but on the same level as the Custody API from the point of view of other
  services which need to use allocation data. This lack of clarity raises
  questions around which OAuth2 grant type to use for authentication on the
  allocation API.
- Responsibility for access control may be split between the allocation
  manager and API. The user-facing application would need to know what the user
  should have access to in order to show the right options, but the API may
  also need to know what the user should have access to in order to fetch the
  right data from other APIs.

We still think there's value in having a separate allocation API, but it would
be easier to understand if it were a more RESTful interface to the data it
stores.

## Decision

The allocation API will be a simpler interface to the data held in its database.

The allocation API will not call other APIs to return data from them to the
allocation manager.

The allocation manager will call the allocation API and other APIs (Custody,
Delius etc) directly.

The allocation manager will be entirely responsible for access control for its
users.

## Consequences

The relationships between the various APIs become easier to understand, because
they are all providing data from only their own databases.

The allocation API clearly sits at the same level as the other APIs in this
space.

The allocation manager will now be responsible for both fetching and combining
data from various sources, and displaying it to users.

There's a risk that the allocation manager will acquire more responsibilities
to the point where it needs to be split up in future. We don't know enough at
this stage to decide where its boundaries should be, so will need to keep an
eye on this as we continue to work on Manage Offenders in Custody.

We haven't yet built anything which needs to be moved between applications as a
result of this decision - this only affects future work.
