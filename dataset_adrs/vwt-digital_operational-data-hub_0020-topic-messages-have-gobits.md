# 20. Topic messages have gobits

Date: 2020-09-21

## Status

Accepted

Implements [16. Pub/Sub implements Event sourcing](0016-pub-sub-implements-event-sourcing.md)

## Context

Data lineage includes the data origin, what happens to it and where it moves over time. Data lineage gives visibility while greatly simplifying the ability to trace errors back to the root cause in a data analytics process.

By adding tracing information to every single message it is possible to trace back a single business event to its source (and all the systems inbetween).

## Decision

Every event published on a pub/sub topic has a gobits record added. Every applications handling/modifing or relaying the event should add a gobits record to that single business event.

## Consequences


### Disadvantages

Adding gobits tot the data adds some message overhead to a single message. This disadvantage is accepted as storage costs these days are getting lower and the simplicity that there is not another system needed to provide data lineage functions.
