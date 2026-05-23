# 4. Use Elastic Search for Data Storage

Date: 2017-09-06

## Status

Accepted

## Context

Elasticsearch is configured as a cluster for reliability and failover, and
provides a single point for data updates. MongoDB runs as a single instance and
is not clustered.

## Decision

 nearby-services-api will consume data from Elasticsearch rather than MongoDB.

## Consequences

The number of deployed components will be reduced.
The pharmacy-db will no longer be required.
We will no longer need to maintain MongoDB updaters, only the Elasticsearch
updaters.
