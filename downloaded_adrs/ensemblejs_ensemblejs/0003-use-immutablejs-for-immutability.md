# 1. Use ImmutableJS for immutability

Date: 15/06/2016

## Status

Accepted

## Context

The cost of cloning JSON, while fast degrades with object size and as we're doing it serveral times per frame the cost is too much.

## Decision

Implement ImmutableJS to avoid the need to clone data. I'm hoping the internal behaviour of ImmutableJS is smart enough to avoid the cost of cloning by cleverly moving references around. The data has to be created once, but I am hopeful that that is the only time.

## Consequences

`JSON.parse(JSON.stringify(data))` is easy to reason about as well as being fast enough for most uses. The use of standard JavaScript objects is also easy to reason about. ImmutableJS enforces it's own API and it's another thing for someone to learn.