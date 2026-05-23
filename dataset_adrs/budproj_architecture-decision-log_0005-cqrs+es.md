# ADR 0005: CQRS+ES

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)
  * [Updates](#updates)

## Context

Our product has a specific security requirement: data reliability. Since we're dealing with big companies' strategies, we cannot afford to lose data. Having conflicts or problems in our data pipelines is extremely dangerous to us.

We must create extremely reliable software that is failure-proof and can make an audit easier.

## Decision

Command Query Responsibility Segregation and Event-Driven Architecture (CQRS+ES) solves those problems with ease. When we took a look, especially at [Martin's Event-Sourcing technique](https://martinfowler.com/articles/201701-event-driven.html), we understood that we could create an event-driven application that can react only to events.

The idea is simple: since we're dealing with compliance and audit departments, we can see **every** action in the platform as **commands** and dispatch **events** based on the result of those commands. That way, we can restore **any** entity from scratch. Even if we suffer from a mass failure in all our servers in this architecture, we could still reconstruct every entity from their event store.

This pattern adds an extra layer of complexity: reading data. If we try to build our entities from scratch at every query, we would have a poor performance. That's where CQRS (Comand Query Responsibility Segregation) comes in handy.

CQRS segregates (as the name suggests) the **command** and **query** stacks. Before digging into the concept, you must understand the definition of those two concepts:
* **Command:** is an intention, an action. Always imperative, like: `RaiseSalary`. Our domain layer receives commands to execute side effects based on those.
* **Event:** is the result of a command. Always in the past, like: `SalaryRaised`. Our domain dispatches events based on resulting side-effects.

In a nutshell, the CQRS architecture focuses our domain layer in handling commands (received from a message broker queue). In contrast, our application layer can return our entities' last know state by accessing the database directly. Like the following diagram:
![Diagram explaining the CQRS Layered Architecture hierarchy](../assets/0005-cqrs+es/cqrs-layered-architecture.png)

Our domain layer will not have any updated copy of our entities. Executing all actions again could cost a lot in compute time, so we're going to create some snapshots to consolidate our entities' state in time. This strategy is a pretty common CQRS standard, and most databases support it.

The last concept we must cover is the sync between our command and query stacks. In our architecture, we will do it using a consumer that will consume dispatched events and update our query database accordingly.

**IMPORTANT:** This architecture is not mandatory across all bounded contexts. Some of those may not have any benefits from event-sourcing at all. Those could use a more standard approach instead of the suggested in this ADR.

## Status

**REJECTED** _check [update 1](#update-1)_

## Consequences

Event-Driven Architecture and CQRS are pretty new concepts, and most software engineers never heard of it. We must ensure that our developers have the required knowledge before changing our domain architecture.

Although this is a pretty stable architecture, it is pretty easy to break the rules and execute actions directly. We must avoid those to sustain reliable software.

Also, we must watch out for external sources of mutation. Those could break the reliability of our event structure. If any external application mutates our entities, those must produce events to notify about that change.

---

## More reading

* [Martin Fowler's blog post](https://martinfowler.com/articles/201701-event-driven.html)

## Updates

### Update 1

After [ADR#0014](0014-reducing-initial-complexity.md), we've decided that CQRS+ES is way too complicated for our initial release. We plan to add it shortly, but not in our MVP.
