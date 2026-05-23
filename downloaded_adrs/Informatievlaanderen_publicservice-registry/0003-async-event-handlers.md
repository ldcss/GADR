# 3. Use async event handlers

Date: 2017-09-12

## Status

Accepted

## Context

While we had great benefits from using an event sourced system in `Wegwijs`, the specific implementation had some drawbacks, specifically the transactional part.

To get up and running quickly, we used a cqrs-es template application as the starting point of `Wegwijs`. To protect us from some of the harder parts of event sourcing, we choose to use an in-process, transactional approach to the way our events and projections were stored, ie: in one all-or-nothing transaction.

This enabled us to get a quick start on `Wegwijs`, delivering features fast. Though we still stand by that decision, the template application also had some drawbacks in terms of testability and modularity. Since we also had in-memory state, this forced us to create rollback logic for this in-memory state in case the transaction failed.

In short: we feel that this approach was great for fast start-up, but over time brings in more complexity than needed.

We feel that, with the knowledge and experience we built on `Wegwijs`, we could now take the step a more modular approach using async event handlers.

## Decision

We will use async event handlers, and thus eventual consistency in our application.

## Consequences

Our system will have eventual consistency, which we need to take into account, especially at the front-end of the application.

Both storing events and updating projections will be more simple, with no transaction between the two to keep in mind.

Both the event store and event handlers will be more easily testable.

Moving away from the `Wegwijs` architecture will make us have to replace parts of its infrastructure.
