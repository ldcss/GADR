# 1. Build print holdings database incrementally

Date: 2020-04-22

## Status

Accepted

## Context

In the existing print holdings system, the build process starts from scratch
each month and reloads all the data. This is computationally expensive, results
in periods of time where particular kinds of data are unavailable in the
system, and results in long lags between submitted data and the visibility of
that data for downstream uses.

## Decision

There will have a persistent data store. We will apply new data as it comes in
to the data store.

We should have robust backups for the data store and separately retain the data
loaded into the data store, so that we can revert to a particular point in time
in case of problems or rebuild from scratch if needed.

## Consequences

We will be able to apply incoming changes more quickly and easily.

We will be able to generate reports at any time other than while we are loading
individual data files.

We will need to support more frequent generation of downstream uses of the
data.

In the old holdings system, we could consider only additions to the data. In
the new system, we must figure out how to add, delete, and change each data
type, and at what granularity we can accept changes.

If we have a single instance of the data store, we will be unable to make
ad-hoc comparisons in the "before" and "after" state -- that is, we would need
to do any analysis of the "before" state before we applied the changes. We may
decide that we want to copy or take a snapshot of the database before making
major changes to better support this.
