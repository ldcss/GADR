# 2. Command

Date: 2018-06-24

## Status

Accepted

## Context

We need to decide the format and semantics of a command type within the actor system.

## Decision

We will use a regular class for a command. The data of a command is added as properties with public getters and setters. A command should be handled as an immutable type.

## Reason

We don't enforce immutability on type level to reduce verbosity.

## Alternatives

Make properties read-only and define constructors. We could also use struct types to reduce garbage collector work but that may require pass-by-ref semantics for best efficiency.