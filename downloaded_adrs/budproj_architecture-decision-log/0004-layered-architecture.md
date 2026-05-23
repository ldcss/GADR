# ADR 0004: Layered Architecture

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)

## Context

Since we're planning to use an Event-Driven Architecture, we may face difficulties while defining microservices to develop. It is common to either break them too much or too little. Defining software boundaries is challenging, and we should pay extra attention since we're dealing with a complex domain.

## Decision

We are going to use Layered Architecture to help us solve those problems. In a nutshell, Layered Architecture breaks our system into four layers:

1. **Presentation:** This layer is responsible for showing the user all the elements for interaction.
2. **Application:** This layer is responsible for handling user interactions and processing them accordingly.
3. **Domain:** This layer is accountable for your core business. It contains all business logic to control your entities and required resources.
4. **Infrastructure:** As the name suggests, this layer is responsible for handling your infrastructure: interacting with databases, handling memory, and so forth.

This pattern is like a Russian doll. If you drill-down inside a microservice from the presentation layer, it can have their Presentation, Application, Domain, and Infrastructure likewise.

A layer can also only talk with the layer below it (except for the Infrastructure layer). For example, the Presentation layer can only interact with the Application layer and the Infrastructure layer. And so forth.

![Diagram explaining the Layered Architecture hierarchy](../assets/0004-layered-architecture/hierarchy-diagram.png)

## Status

**DEPRECATED** _check [update 1](#update-1)_

## Consequences

By adopting this decision, we're going to improve our software's stability, but increase the complexity of architectural solutions and increase the ramp-up time of new engineers. But this pattern makes it easier to develop high-cohesive and low-coupled software.

## Updates

### Update 1
Date: 2021-07-22

This ADR is not valid anymore, since our only back-end is updated following the Hexagonal DDD pattern (which still lacks an ADR)
