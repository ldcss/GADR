# 8. Use AxonFramework in backend

Date: 2021-01-11

## Status

Accepted

## Context

In [ADR 5](0005-use-cqrs-architectural-style.md) and [ADR 6](0006-use-ddd-tactical-design-patterns.md) we decided to 
adopt CQRS and tactical DDD patterns respectively. In [ADR 7](0007-use-events-as-communication-mechanism-between-modules.md) 
we decided that we'll use events as a means of communication between modules. Maintenance of practicalities behind these
patterns can be quite overwhelming, especially that we are not very experienced.

## Decision

We will use AxonFramework to aid in
- Implementing EDA thanks to the provided EventBus support
- Adopting the DDD building blocks
- Implementing read model projections
- Adopting EventSourcing (optional)

## Consequences

- Domain specific code will be coupled with AxonFramework and Spring Boot/Framework (see [ADR 4](0004-accept-coupling-with-spring-boot-in-backend.md))
- We'll focus on domain behaviour more since building blocks and common patterns are already provided by frameworks
- AxonFramework also provides great support for Event Sourcing. It is not a strict requirement though, each 
module can decide on its own whether to be EventSourced or not 
