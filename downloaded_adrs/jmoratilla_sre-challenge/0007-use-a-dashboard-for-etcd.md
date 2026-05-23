# 7. use a dashboard for etcd

Date: 2020-05-25

## Status

Accepted

## Context

To visualize the metrics of the etcd cluster, I would like to implement a
 dashboard using the USE and RED methods.

- USE to measure the performance of the system hosting the etcd cluster
- RED to measure the performance of the gRPC side of the etcd cluster

But I haven't found anything like this and I have no time to waste.  So
 I have found a dashboard on the grafana site that has some metrics.


## Decision

As I'm out of time, I'm just going to implement it at the configuration
 management system, to automatically provision the dashboard and the
 datasource.

## Consequences

Nothing.