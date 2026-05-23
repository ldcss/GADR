# Shared Application Insights

## Status

Accepted.

## Context

Marain services need to be able to deliver diagnostic information somewhere.

## Decision

`Marain.Instance` creates a single Application Insights instance and makes its key available to all services. All services use it.

## Consequences

By using a single instance, cross-service operation is captured correctly. Application Insights correlates telemetry when requests cross service boundaries, but it relies on all the relevant services reporting to the same Application Insights instance for this to work. So by having a shared instance, we can see diagnostic and performance information at the whole-system level.