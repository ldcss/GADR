# 6. Don't use memory caches anymore (across handlers).

Date: 2017-09-12

## Status

Accepted

## Context

In `Wegwijs` we used a memory cache across all event handlers.

These memory caches, however, were built up from certain projections. An example of this was the `organisation names` cache, which was built up from the `OrganisationDetail` projection.

Using the memory cache outside the in-process event handlers, where the `OrganisationDetail` projection was built, causes a dependency between projections. This means that if we now want to rebuild projection X while the OrganisationDetail is not fully built, the memory cache is in an incorrect state. This defeats the purpose of the memory cache.

## Decision

We will re-evaluate the use of memory caches. If we do use them, we will use them fully isolated within the containing handler.

## Consequences

We will need to rethink caching, eg with caching to MSSQL tables.

We will no longer have hidden dependencies between projections, resulting in more reliable projections.
