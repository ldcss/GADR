# 5. Use Dropwizard Metrics

Date: 2018-06-20

## Status

Accepted

Supercedes [4. Use Micrometer Prometheus](0004-use-micrometer-prometheus.md)

## Context

We want to provide metrics about the status of a monitored service.

## Decision

We will use _Dropwizard_ for creating the metrics.

## Consequences

_Micrometer_ does not allow us to remove or unregister a metric.
With _Dropwizard_ we can unregister a metric when we no longer need it. This is useful when we decide that it's no longer needed to monitor a given service.
