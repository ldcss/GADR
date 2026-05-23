# 3. Use Prometheus for exposing metrics

Date: 2017-09-07

## Status

Accepted

## Context

We need to know what the application is doing in a more light weight way than
scraping logs. We need to be able to monitor KPIs of the application in order
to understand the health of the application. This will allow us to react and
potentially pro-actively initiate measures as to ensure the application's
health if sound. Ultimately providing a better service for our users.

## Decision

We will use Prometheus to monitor and alert on the state of the application.

## Consequences

The application needs to be instrumented such that Prometheus will have access
to scrape metrics. This results in an endpoint specifically for exposing those
metrics i.e. /metrics. The instrumentation of the application along with the
additional requests being made to the application, from scraping the metrics
incurs a performance cost. The cost is small, is outweighed by the benefits of
having the data provided by the metrics and is a compromise worth making.
