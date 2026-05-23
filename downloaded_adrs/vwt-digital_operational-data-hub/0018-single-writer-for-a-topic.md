# 18. Single writer for a topic

Date: 2020-09-21

## Status

Accepted

Implements [16. Pub/Sub implements Event sourcing](0016-pub-sub-implements-event-sourcing.md)

## Context

Topics are used to distribute events to other applications. Systems subscribing to these events will be dependent on these events. 

## Decision

Every topic is limited to a single writer process.

## Consequences

Whenever an application needs to publish the same event already used for another application, a new topic needs to be created. When these events need to be combined in one stream a function/process needs to be added which combines the two.
