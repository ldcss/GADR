# 8. Do not use local data for CCGs

Date: 2019-10-30

## Status

Accepted

## Context

All current IAPT services should have an ODS code. Any future services must
have an ODS code assigned. There for it is no longer necessary to use local
data to relate CCGs to IAPT services.

## Decision

Remove local data for all CCGs. The source for CCG to IAPT service relationship
data will only be the central data store.

## Consequences

All CCG to IAPT service relationships can be updated centrally in a consistent
manner. Creating a new release to add services will no longer be required.
Adding a new service will require the service to have an ODS code allocated and
the relationship to CCG added to the central data store. The turnaround time
may be longer than for adding a service to local data.
