# 10. Use postcodes.io for reverse geocoding

Date: 2017-11-22

## Status

Accepted

## Context

The coordinate provided by the browser needs to be reverse geocoded in order to
identify the country of origin.

## Decision

The decision is to use the same lookup service as is already employed to lookup
postcodes and places. That service is postcodes.io.

## Consequences

- All place, postcode and location lookups are performed by the same service
- The existing API client can be used
- There is no data for non-UK locations
