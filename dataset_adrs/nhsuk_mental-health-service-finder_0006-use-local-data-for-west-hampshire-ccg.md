# 6. Use local data for West Hampshire CCG

Date: 2019-09-18

## Status

Accepted

## Context

The data synchronisation between front end and back end is broken and is taking
time to fix. In the interim the data can be stored locally within the
application.

## Decision

The data for West Hampshire will be stored locally within the application until
such a time as the data synchronisation has been fixed. Once fixed, the local
data store will be removed so the centrally held data can be requested and used
within the application.

## Consequences

The data stored locally is not managed centrally, as all other data is.
This change is only temporary and will be reverted once the data
synchronisation has been fixed.
