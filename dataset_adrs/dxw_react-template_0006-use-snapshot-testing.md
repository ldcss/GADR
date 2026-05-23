# 6. Use snapshot testing

Date: 2019-10-08

## Status

Accepted

## Context

We want to be confident that any changes to how our React components display are
intentional. Jest has built in support for snapshot testing.

## Decision

We will use snapshot testing as part of testing components.

## Consequences

Snapshot testing means that _intentional_ changes to the way components display
will require explicitly updating the snapshots. This is done with a flag when
running the test suite, and means changes will always be intentional.
