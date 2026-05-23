# 4. Use `SqlStreamStore`

Date: 2017-09-12

## Status

Accepted

## Context

Since we decided to use event sourcing, we need a way to store events in our database.

In `Wegwijs` we stored events in `MSSQL`, which allows easy debugging of events. All sql statements to save/read events were hand-written.

**However**, since we decided on async event handlers in a previous ADR, we would benefit a lot from having catch-up subscriptions for our event handlers. Catch-up subscriptions allow event handlers to be in charge of what events they are interested in, and give event handlers more autonomy over their own rebuilds.

While `GetEventStore` supports this, and is most likely a top-notch choice for storing events, this would require us to take care of hosting this. We also have doubts about the support for storing business-critical data outside of `MSSQL` in `AIV`.

We currently host no VMs for business-critical concerns, and we feel that hosting `GetEventStore` ourselves, would add a significant burden.

As an alternative, `SqlStreamStore` is an OSS library on GitHub which supports storing events into `MSSQL`, and has support for catch-up subscriptions. It has an active community, and has been used in several production systems successfully according to that community.

## Decision

We will use the `SqlStreamStore` library as our event store. We will keep an eye on ongoing developments from `SqlStreamStore`.

## Consequences

We will no longer have to implement saving/reading events ourselves.

We will have the option to use catch-up subscriptions, giving event handlers more autonomy.

We will need to keep an eye on `SqlStreamStore` developments, through github updates and the `#`sqlstreamstore` `channel on https://ddd-cqrs-es.slack.com.

We will be able to use constantly updated best practices from the community.

It will be harder to customize saving/reading the event store, though we don't see the need for that at this point.
