# 10. Do not use CLR type names for event types.

Date: 2017-09-12

## Status

Accepted

## Context

Looking at the SqlStreamStore code, we noticed a warning against using the CLR type name as the event type in your event store.

The reason behind this is that your message types will outlive your .net CLR types. Moving events along namespaces will break stuff.

## Decision

Use a dictionary/map between your message types and the CLR type you want to deserialize your message into.

## Consequences

Serializing/Deserializing events will no longer break when refactoring events.
