Scaling and Consolidation of EC2

Date: 03/10/2019

## Context

We are moving from platforms such as VMWare, where instances are kept small and are encouraged to scale out. If we were to scale up instead, then we would require either 
1. A workload that is able to make efficient use of multi-threading.
1. Workloads that are able to co-exist peacefully.
It cannot be assumed that the workloads we are moving into AWS will fit neatly into either category.

## Decision

Our preference for enterprise applications is to consolidate onto a smaller number of instances.

## Consequences

The reduced footprint will result in a lower TCO. However, some functions, such as performance analysis of an instance, will be more difficult.
