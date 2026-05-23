# 3. Create Two Observation Comparators

Date: 2020-10-07

## Status

Accepted

## Context

Whale observations have a variety of qualities and may require sorting for research purposes. Two
distinct sorting methods proposed for sorting these observations will require two unique comparison methods.

## Decision

Implement `Comparable<Observation>`, create default field `compareTo` method for `ObservationId` (long) and nested
comparator class for field `sightingTime` (Date) in Observation.

## Consequences

The nested comparator class is the best choice for the program due to its wide availability and reusability in future
iterations of the program, versus the one-use nature of anonymous classes and lambda expressions.