# 8. Data is location and time aware

Date: 2020-09-21

## Status

Accepted

## Context

All data that is related to geographic structures is added to the ODH in a standardized way.

## Decision

GeoJSON is a format for encoding a variety of geographic data structures (https://tools.ietf.org/html/rfc7946)
GeoJSON-events extends RFC 7649 GeoJSON with instants and intervals of time (https://github.com/sgillies/geojson-events)

## Consequences

### Advantages

Representation of geolocation is clear and specific.

### Disadvantages

Geolocation data can be represented in many different ways. Transformation to GeoJSON before publishing on the ODH and back to other formats for outgoing data introduces additional cost.
