# Title
Queuing up the notifications

## Status

accepted

## Context

We shouldn't overwhelm the Notifier.  This would happen then we have many orders, surveys and recommendations to send to customers.

## Decision

The decision is to introduce a queue for all these messages.

## Consequences

Without this, we can easily overwhelm the Notifier.  Scheduling of these messages are important as well.  
