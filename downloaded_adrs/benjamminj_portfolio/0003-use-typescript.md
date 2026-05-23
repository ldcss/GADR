# 3. Use TypeScript

Date: 2020-09-03

## Status

Accepted

## Context

There's a few large architectural decisions that were made before I started using ADRs, so I'm backfilling them a little.

The first version of this website was all in vanilla JS, but after working a bit more with TypeScript I'm all-in on it. It provides a bunch of fantastic benefits for productivity, refactoring, and documentation.

## Decision

## Consequences

- This will make refactoring significantly easier, since the compiler makes sure the **shapes** of inputs & outputs are correct.
- This will serve as a lightweight documentation of any functions
- This will help boost productivity given the rich ecosystem around TypeScript—stuff like auto-importing, IDE autocompletion, and faster feedback loops
