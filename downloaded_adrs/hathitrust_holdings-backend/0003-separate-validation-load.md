# 3. Conceptual separation between data validation/transformation and load steps

Date: 2020-05-04

## Status

Accepted

## Context

The new print holdings system has a persistent backend to which we build
incrementally (see print holdings ADR-1). Updates to data come from a variety
of sources -- Zephir, HathiTrust members, and OCLC -- and cannot be assumed to
be well-formed or consistent prior to loading. Changes do not come one at a
time but rather as a "change set" provided all at once. The persistent back-end
operates on the notion of individual create/update/delete operations for each
kind of data.

## Decision

In the new system, there will be:

* the notion of a change set for each type of data

* functionality for validating and normalizing change sets

* functionality for transforming a validated change set into a stream of
individual create/update/delete operations

## Consequences

This architecture decision should help us separate the responsibilities for
classes dealing with the incoming change sets from the responsibilities of
classes dealing with data in the persistent back-end.

Because validation and normalization happens before changes are loaded, this
also implies that additional transformations should not be made on an ad-hoc
basis -- updates should only happen via a new change set or via managed
migrations.

There will need to be a clearly defined interface between the change set and
the loading process.
