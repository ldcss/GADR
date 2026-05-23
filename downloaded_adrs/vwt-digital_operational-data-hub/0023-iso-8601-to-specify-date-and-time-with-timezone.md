# 23. ISO-8601 to specify date and time with timezone

Date: 2020-09-21

## Status

Accepted

Implements [16. Pub/Sub implements Event sourcing](0016-pub-sub-implements-event-sourcing.md)

## Context

JSON does not specify how a date(time) string should be formatted. The ISO 8601 standard is widely used within the JSON community to specify date-time objects. [RFC 3339]([https://tools.ietf.org/html/rfc3339) describes the usage of the ISO-8601 standard.

## Decision

We will use the ISO-8601 (latest version) standard (as described in RFC-3339) for formatting date(time) objects whenever a date(time) object is serialized. This applies (but is not limited) to JSON messages, logging, data-store/firestore timestamps.

All date objects must have a time-zone included. 

## Consequences

Other date formats need to be transformed from and to the ISO-8601 format whenever needed. This may cause a little overhead.

## References
- [RFC 3339]([https://tools.ietf.org/html/rfc3339)
- [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)

