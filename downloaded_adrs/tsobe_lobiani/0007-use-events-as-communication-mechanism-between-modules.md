# 7. Use events as communication mechanism between modules

Date: 2021-01-11

## Status

Accepted

## Context

We need a communication mechanism between modules. We can let each module directly consume the API of another module, or
we could let each module subscribe to events published by other modules   

## Decision

Since in [ADR 2](0002-start-with-modular-monolith-backend.md) we decided to be ready for microservices, we will use the 
second approach - events as the communication mechanism

## Consequences

- Overall system will be more loosely coupled
- Transitioning to microservices will be easier due to location transparency
- System complexity will increase due to increased indirection and asynchronous nature of messaging
- We'll have to cope with eventual consistency
