# Create Observation Repository Sort

Date: 2020-10-09

## Status

Accepted

## Context

Researchers may require methods for sorting the lists of Whale Observations to extract key information regarding
whale migration, population, etc. Through Observation's available comparison methods the proposed sorting is possible.

## Decision

Create `sortByDate` and `sortById` methods in ObservationRepository.

`sortByDate` uses the comparator `compareByDate` from the `Comparator<Observation>` interface and `Collections.sort()`
to sort the list of observations by field `sightingTime` (Date).

`sortById` uses the default `compareTo` method from the `Comparable<Observation>` interface and `Collections.sort()`
to sort the list of observations by field `ObservationId` (long).

`Collection.sort()` implements the abstract strategy of the `Comparator` interface using the concrete strategy
`compareByDate` and returns an integer referring to the order of the objects.

## Consequences

Whale Observation lists are sortable. Future iterations of the program can easily add new comparators for sorting
since we have implemented the strategy design pattern with the `Comparator<Observation>` interface.
