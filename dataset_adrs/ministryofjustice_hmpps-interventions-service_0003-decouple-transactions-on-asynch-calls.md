# 1. Decouple database transactions on asynchronous calls

Date: 2021-09-17

## Status

Accepted

## Context

We need to ensure that when asynchronous calls are made that they do not cause issues with database transactions scopes.
In normal circumstances (without @Async) a transaction gets propagated through the call hierarchy from one Spring @Component to the other.
However, when a @Transactional Spring @Component calls a method annotated with @Async this does not happen. 
The call to the asynchronous method is being scheduled and executed at a later time by a task executor and is thus handled as a 'fresh' call.

## Decision

We decided to prevent issues with @Async calls that we only sent primitive values or DTOs rather than a database entity.
This ensures that there is no unexcepted behaviour when performing a lazy-fetch of the database entity.

## Consequences

1. The NotificationService should have its own @Transactional annotation separate from the calling class.
2. Objects should be re-fetched by service classes within the @Asynch class using an id passed into the @Asynch @Component.
3. Care must be taken that when fetching the same object from the calling class that the entity manager is flushed before calling the @Asynch @Component.

