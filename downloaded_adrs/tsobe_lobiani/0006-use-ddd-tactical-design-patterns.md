# 6. Use DDD tactical design patterns

Date: 2021-01-10

## Status

Accepted

## Context

We need some building blocks to model the domain in the software

## Decision

We will adopt tactical design patterns from DDD, that is we'll model the domain in terms of following objects:
- ValueObject - immutable object without identity
- Entity - object encapsulating some business entity with identity
- Aggregate - graph of Entities and ValueObjects enforcing consistency boundaries and business invariants
- AggregateRoot - entity acting as a root object in the Aggregate
- Command - immutable object representing the intention to trigger the behavior of the aggregate
- Event - immutable object representing the important fact that happened in the domain
- Repository - collection-like storage for aggregates
- DomainService - encapsulates the behavior that does not belong to any particular aggregate
- Saga - long-running business transaction

## Consequences

- Changes made in transactions spanning more than one aggregates, will be eventually consistent
- Identifying these building blocks may require trial and error
