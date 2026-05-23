# 21. Messages are in JSON format

Date: 2020-09-21

## Status

Accepted

Implements [16. Pub/Sub implements Event sourcing](0016-pub-sub-implements-event-sourcing.md)

Implemented by [19. Single schema per topic](0019-single-schema-per-topic.md)

## Context

It is preferred to use a single message type for the business events. This makes it easier to handle messages on the pub/sub system in a standerdized way.

## Decision

All business events on the ODH platform topics are formatted as [JSON](https://tools.ietf.org/html/rfc7159)

## Consequences

### Disadvantages

Messages deliverd to the ODH or messages for systems conneted to the ODH might need other message formats. In these cases the messages need to be transformed from one layout to the other.
