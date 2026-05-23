# 2. Create Repository Interface (From Exercise 2)

Date: 2020-09-22

## Status

Accepted

## Context

The system has various data types that users may want aggregated together so that they are easily accessible and sortable.
e.g. Types `Whale` and `Observation`. The system should have a consistent interface so that the user may access various
types of records.

## Decision

We decided to implement a `Repository <T>` interface that can be realised by `Whale` or `Observation` objects. Users 
who need to access a large list/repository of Whale's or Observation's will do so through the `Repository <T>` interface.

## Consequences

This design decision ensures there are common methods for sorting and accessing large records whether they are of type
`Whale` or `Observation` which will make working with these data structures more straightforward. If another type of class is going to be recorded in a large collection, that collection should be implemented by realising the 
`Repository <T>` interface.
