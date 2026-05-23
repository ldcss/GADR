# 4. Separate API and user-facing applications

Date: 2018-10-12

## Status

Accepted

Amended by [10. Allocation API has less responsibility](0010-allocation-api-has-less-responsibility.md)

Amended by [18. Unify API and Presentation layer](0018-unify-api-and-presentation-layer.md)

## Context

We are moving into beta on allocations, which is the first area of our work on
Manage Offenders in Custody. The team is now also in discovery on handover, and
there are more areas which we know very little about at this stage which we
intend to look at in future.

We anticipate that we will build more than one product as part of this work, to
meet different needs of different users. That means that we're very likely to
build more than one application as part of this larger service area in future.

We need to decide now whether we should start out by building one application
for allocations, or follow the common pattern of separating an API layer from
presentation.

### Microservices

There are many advantages to a microservices architecture, but also some costs.

If we start off with more than one application, the decisions we make early on
about their responsibilities may take more work to change later on, as we learn
more.

On the other hand, if we start off with one application and decide later that
we want to split it into several, that work is likely to be substantial. Given
the timescales involved in OMiC, it may be hard to prioritise paying off that
technical debt when it becomes a burden.

We anticipate that other services will need to use allocation data, and so we
are likely to need to make it accessible via APIs at some stage anyway. Those
services may need to access allocation data in different ways from our
frontend, so more work may be needed then to support them even if we do have
an API from the start.

### Operating microservices

Microservices can introduce more operational complexity by moving function
calls to network calls and by introducing more moving parts which need to be
deployed. However we expect the number of microservices to remain relatively
small so do not anticipate this complexity to be significant for us.

Our choice of the Kubernetes-based Cloud Platform for hosting (see [ADR 0002](0002-use-cloud-platform-for-hosting.md))
should make it easier to scale small services efficiently and independently.
It also gives us easy access to tooling designed to support many small
services.

We expect our decision on how far we should follow a microservices approach to
have minimal impact on our hosting costs.

## Decision

We will start off with two applications for allocation:

- an allocation API which will call other APIs (to read data from NOMIS, and
  in future Delius and OASys)
- an allocation frontend which will call the allocation API and serve
  progressively enhanced HTML to users (see [ADR 0003](0003-use-progressive-enhancement.md))

## Consequences

We will have a clear separation of data and presentation concerns from the
start.

We will need to define our approach to our API early on, before other teams
need to use our data as well. That will make it easier for other teams to
contribute to the allocation API.

Starting off with more than one service will ensure that we choose our tooling
and workflows to support multiple services from the start, which will make it
easier to spin up new services for other areas of our work on Manage Offenders
in Custody.
