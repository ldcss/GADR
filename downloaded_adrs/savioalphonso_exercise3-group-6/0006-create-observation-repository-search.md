# Create Observation Repository Search

Date: 2020-10-09

## Status

Accepted

## Context

Researchers may require methods to search for a particular Whale Observation or set of Whale Observations during their
studies. For the program to accomplish this task two search methods may require implementation.

## Decision

Create `getByDate` and `getById` methods in ObservationRepository.

`getByDate` uses the Observation iterator to compare Observation objects `sightingTime` (Date) to the date passed to the
method and creates an array list of matching objects. This function uses an iterator rather than `Collections.binarySearch()`
to reduce the runtime given that there may exist multiple objects of a similar date.

`getById` uses `Collections.binarySearch()` to search and possibly return the object with the `ObservationId` matching
the long passed to the method.

Collection.sort()` used in `getById` implements the abstract strategy of the `Comparator` interface using the concrete
strategy `compareByDate` and returns an integer referring to the order of the objects.

## Consequences

Searching for Whale Observation objects with the same `sightingTime` or for a particular `ObservationId` is now 
possible.
