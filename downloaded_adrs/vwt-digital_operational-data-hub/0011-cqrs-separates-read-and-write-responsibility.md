# 11. CQRS separates read and write responsibility

Date: 2020-09-21

## Status

Accepted

Related to [10. Event sourcing captures every change to business state](0010-event-sourcing-captures-every-change-to-business-state.md)

Related to [9. URI identifies data](0009-uri-identifies-data.md)

Implemented by [16. Pub/Sub implements Event sourcing](0016-pub-sub-implements-event-sourcing.md)

## Context

CQRS stands for Command Query Responsibility Segregation. It's a pattern that I first heard described by Greg Young. At its heart is the notion that you can use a different model to update information than the model you use to read information.

The core of the ODH are the [pubsub](0016-pub-sub-implements-event-sourcing.md) topics implementing [event sourcing](0010-event-sourcing-captures-every-change-to-business-state.md). This allows consumers of these events to build a data representation (model) from these events that exactly fits their use case. The result is that different models exist, representing the same real-life entities.

## Decision

We will implement Command Query Responsibility Segregation (CQRS) on the ODH between  [projects](0028-a-solution-is-implemented-by-one-or-more-gcp-projects.md).

CQRS is not required within a project and should only be applied at project level if the additional complexity is justified by CQRS-specific advantages.

## Consequences

### Advantages

Use case specific models can be used in [solutions](0026-solution-facilitates-a-coherent-set-of-business-functions.md), allowing simpler and performant implementations.

Read representations can be rebuild by loading events from topic history.

### Disadvantages

Multiple representations can exist for the same entitiy, which could cause confusion and duplicates. This is mitigated by using [URIs](0009-uri-identifies-data.md).

Due to the eventual consistency of CQRS different represenations could temporarily show inconsistent information about an entity. Combining information where such inconsistency is not acceptable requires implementation of a specific representation that is built from all events in scope of the comparison.

## References

* https://martinfowler.com/bliki/CQRS.html, retrieved 30 September 2020
