# 5. Allocation API owns allocation data

Date: 2018-10-12

## Status

Accepted

## Context

Allocation of Prison Offender Managers is a new process being introduced by
OMiC, and it's different from Offender Supervisor allocation (data for which
is mostly stored in per-prison spreadsheets). The data which will be created
by this process does not live anywhere yet.

We've heard that some prisons are starting to use the new terminology and have
started to store staff names as POMs against prisoners in NOMIS (although they
are not actually using the OMiC model yet). There is no support in NOMIS for
the tiering data or anything else needed to support the allocation process.

We have learned from our allocation discovery that staff around the prison
need to know who is responsible for a prisoner, but there's no indication that
storing that data in NOMIS is a good way of meeting that need.

We don't know much yet about the user needs around handover of responsibility
from prison to probation. It's possible that there will be a stronger need to
store some allocation data in Delius (for example) so we may need to revisit
this decision in future.

HMPPS needs to reduce its dependence on NOMIS over time, and building an
ecosystem of APIs around new datastores will enable data to be used in other
services without it all needing to be in one central database. The keyworker
API is an existing example of this pattern.

## Decision

The allocation API will store all data created by the allocation process in its
own database.

We will not also write allocation data back to NOMIS or any other system.

## Consequences

It will be clear where responsibility for this data lies.

We will be responsible for a critical data set, and need to operate the service
appropriately for that context.

This is a high-level principle, so as we begin development we'll need to
consider how far the scope of this decision extends in practice.

We will need to ensure that any POM contacts which have been added to NOMIS are
removed when those prisons move to the OMiC model and start using the
allocation manager.
