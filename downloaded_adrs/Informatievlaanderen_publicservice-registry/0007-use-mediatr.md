# 7. Use MediatR as in-process bus.

Date: 2017-09-12

## Status

Accepted

## Context

When doing cqrs, we need a way to send commands to their command handler.
Similarly, we need a way to send events to their event handlers (note: plural).

MediatR is a low-ambition OSS library trying to solve a simple problem - decoupling the in-proc sending of messages from handling messages. Cross-platform, supporting .NET 4.5 and netstandard1.1.

MediatR can accomodate both handling Request/Reply (commands) and Fire/Forget (events) scenarios. Handlers are simply decorated with a marker interface, are self-contained and easily tested.

## Decision

We will use MediatR for sending commands to their command handler.
We will use MediatR for sending events to their event handlers.

We will keep the pipelines for these two scenarios separate from each other.

## Consequences

We will need to invest some time into building the pipeline for eg: enriching commands.

Handlers will be easily testable.
