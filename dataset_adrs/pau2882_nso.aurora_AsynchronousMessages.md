# Title
Asynchronous messages to the Notifier

## Status

accepted

## Context

The messages that are sent from Order Management, Rating Manager and Recommendation Manager can be asynchronous?

## Decision

Yes it can be asynchronous because we don't need to wait for an ack before sending the next one. 

## Consequences

Without it being asynchronous, there might be many messages stuck in the waiting to be sent bucket.
