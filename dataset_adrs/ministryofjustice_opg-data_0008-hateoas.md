# 8. HATEOAS - Hypermedia as the Engine of Application State

Date: 2020-01-27

## Status

Proposed

## Context

We wish to build a RESTful API, and to be technically RESTful, we must implement HATEOAS. This gets us to stage 3 of the [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html)

For full context / a HATEOAS primer, [read the supporting notes](../supporting-notes/hateoas.md)

## Decision

Our API is to be as RESTful as it can be.

We recognise that we must implement Hypermedia as the Engine of Application State.

The content structure already discussed in [0005-content-structure.md](0005-content-structure.md) implements links within our resource object... this ADR is to explicitly state our aim is to implement HATEOAS.

Furthermore, for every endpoint on the API we will implement an OPTIONS verb, returning every action possible at that endpoint.

For full context / a HATEOAS primer, [read the supporting notes](../supporting-notes/hateoas.md)

## Consequences

* Our API will be more RESTful
* Our API will be consumed more easily
