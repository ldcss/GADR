# 14. Adopt Command-query separation (CQS)

Date: 2020-05-09

## Status

Accepted

## Context

[Command-query separation](https://martinfowler.com/bliki/CommandQuerySeparation.html) states that every method should
either be a command that performs an action, or a query that returns data to the caller, but not both.

Adopting command-query separation makes a clear separation of methods that change state from those that don't. So we can
use queries with much more confidence, and only be careful with commands orchestration.

Commands and queries terminology is already used in the `menu-generation` application.

## Decision

Command-query separation will be enforced in the [core hexagon](./0003-adopt-hexagonal-architecture.md), especially in
application services.

## Consequences

For each command handler (service method), a corresponding `Command` object contains all the information necessary for
the command to be executed. Those command objects are immutable value objects. Similarly, complex queries will
correspond to a `Query` object with the same constraints (immutability, self contained query). Those objects explicit
the concepts through naming (based on an action verb and the corresponding aggregate) and ease evolvability, enforcing
parameters encapsulation for most actions on domain services.

In terms of transactions, we can assume that queries are read-only, thus using a lighter transaction scope.

In the case of events being generated for commands execution, aggregates may still return a list of corresponding
events when handling a command so that the command handler (service method) originally delegating to aggregate is able
to propagate those events to other parts of the application, or to an event store.

Command-query separation will ease a possible future use of [Command-query responsibility segragation](https://martinfowler.com/bliki/CQRS.html)
(CQRS) and all the associated advantages.
