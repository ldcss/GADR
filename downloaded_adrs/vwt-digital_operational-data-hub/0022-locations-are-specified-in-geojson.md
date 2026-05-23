# 22. Locations are specified in GeoJSON

Date: 2020-09-21

## Status

Accepted

Implements [16. Pub/Sub implements Event sourcing](0016-pub-sub-implements-event-sourcing.md)

## Context

A large numer of the events on the ODH contain location specific data. It is usefull to standardize the usage for location events.

## Decision

[GeoJSON](https://tools.ietf.org/html/rfc7946) will be used for XYZ (locations) on the ODH. When XYZt data is needed [GeoJSON-events](https://github.com/sgillies/geojson-events) should be considered.

## Consequences

None


