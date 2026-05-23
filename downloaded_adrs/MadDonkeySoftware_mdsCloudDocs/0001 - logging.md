# 0001. Logging

Date: 2020-Mar-09

## Status

Accepted

## Decision

All logging shall be done through a easily machine readable format as a first class citizen. If needed a tool or utility will be provided that can / will translate the logs into a human readable format.

## Context

When deciding on a logging mechanism two main options are available to use. One provides a first class experience for machine readable logs while the other provides a first class experience for human readable logs. The leading tools used for this context are Bunyan (machine-readable) and Winston (human-readable).

It was decided that a machine-readable format should be the foremost approach to use as translating these logs to a human-readable format is easier to accomplish than going from human-readable to machine-readable. Complexity lies in that human readable format may drift over time and thus parsing logs to a machine readable format would become problematic over that time frame.

## Consequences

With a machine-readable format logs are easy to transport to multiple mechanisms, such as rolling files consumed by a file viewer, as well as a log aggregation platform, such as a ELK stack.

Logs natively written to disk may be problematic for users to read directly. A tool can be written, should the need arise, to translate these logs into a more human friendly format.
