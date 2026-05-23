# 4. Use Micrometer Prometheus

Date: 2018-06-04

## Status

Superceded by [5. Use Dropwizard Metrics](0005-use-dropwizard-metrics.md)

## Context

We want to provide metrics about the status of a monitored service.

## Decision

We will use _Micrometer_ for creating the metrics and make them available through a _Prometheus_ endpoint. 

## Consequences

_Prometheus_ is already known. Since _Prometheus_ works by scraping the metrics from the application, the availabilty and granularity of the metrics is defined by the availability and scrape interval of the _Prometheus_ server.
 _Micrometer_ is a 'Vendor-neutral application metrics facade' meaning we can freely choose the monitoring tool we integrate with.
