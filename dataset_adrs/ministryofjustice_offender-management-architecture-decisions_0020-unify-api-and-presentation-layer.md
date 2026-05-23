# 20. Unify API and Presentation layers

Date: 2019-02-06

## Status

Accepted

Amends [Separate API and user facing applications](https://github.com/ministryofjustice/offender-management-architecture-decisions/blob/master/decisions/0004-separate-api-and-user-facing-applications)

Amends [Allocation API has less responsibility](https://github.com/ministryofjustice/offender-management-architecture-decisions/blob/master/decisions/0010-allocation-api-has-less-responsibility)

## Context

Previously, it was decided in [ADR 0004](https://github.com/ministryofjustice/offender-management-architecture-decisions/blob/master/decisions/0004-separate-api-and-user-facing-applications) that we would separate data and presentation concerns.  This however was reversed by [ADR 0010](https://github.com/ministryofjustice/offender-management-architecture-decisions/blob/master/decisions/0010-allocation-api-has-less-responsibility) which meant there was an overlap of data concerns with some data access from the presentation layer, and some via the Allocation API.

It was envisioned that starting off with more than one application would mean
that we would be able to structure the responsibilities early in the process and
reduce later efforts, but in practice this has not happened. With more exposure
to some of the APIs we are dependent on which service should access them has
become less clear over time.  For instance, it was discovered that it was better
for the Allocation API to retrieve staff data from Elite2, rather than the
presentation layer.

There was concern that later migration from a monolith to separate services would
be technical debt that we would be unable to pay off in future, due to other
competing pressures. The cost of managing two different services, sharing contexts
and overlapping boundaries has however increased the development complexity and
cognitive load.

There was a requirement that other services are likely to require access to the
allocation information that we have stored. This made sense when there was a
clean separation of concerns (with all data access via the Allocation API) but
currently provides little benefit. Whether the API is a separate service or
a modular component of a monolith is currently a deployment strategy as
architecturally it provides few benefits over a modular application. It is
entirely possible to provide an API via a modular monolith.

As we have progressed with development, we have encountered issues with
our approach of enriching API sourced data with locally acquired data. Processes
where we retrieve data, enrich it with data from external APIs and then enrich it
with data from local APIs result in the movement of lots of data which has
performance costs.  Direct access to the database for 'local' data would
remove issues with both performance and moving data across boundaries containing
isolated (but related) logic.

## Decision

We will integrate the existing Allocation API into the Allocation Manager, and make
the public api available at /api.

We will work in a single unified codebase in a well-designed modules to
reduce some future effort in separating concerns.

## Consequences

We expect this to reduce cognitive load, and complexity for developer whilst improving
the performance with respect to data processing.

We may require some time in decommissioning (but not yet destroying) existing
infrastructure for the Allocation API service.

In the future, should the operational need arise, we may need to spend some time
separating out the minimal public API into a separate service.
