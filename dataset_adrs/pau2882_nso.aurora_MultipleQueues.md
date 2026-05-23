# Title
Multiple queues

## Status

accepted

## Context

The messages from Order Management is probably more important than those that are coming from Rating Manager and Recommendation Manager.

## Decision

The decision is to introduce another queue for Order Management

## Consequences

Without this, customers might not receive important messages regarding their orders in timely manner 
