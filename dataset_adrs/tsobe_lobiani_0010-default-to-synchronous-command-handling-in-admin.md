# 10. Default to synchronous command handling in admin

Date: 2021-02-07

## Status

Accepted

## Context

In [ADR 5](0005-use-cqrs-architectural-style.md) we decided to adopt CQRS architectural style. Therefore, we need a 
strategy, or a guideline for handling commands issued to admin sub-system. Couple of things we can take into the
account:
- Admin tool is intended for "internal use" only, i.e. it won't be exposed to the wild (customers)
- There is no strict requirement about predictable and stable latency

## Decision

Commands issued to admin will be handled synchronously by default. An asynchronous mode is still allowed though for 
exceptional cases only.

## Consequences

- Implementation will be easier, as there is no need to have a dedicated communication channel for notifying failures
- Command handling feedback will be known immediately 
- User experience may be degraded slightly due to higher latency
