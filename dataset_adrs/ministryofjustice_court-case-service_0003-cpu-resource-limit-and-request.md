# 3. Kubernetes CPU resource limit and request

Date: 2020-12-09

## Status

Under review

## Context

Following completion of ticket [PIC-1134](https://dsdmoj.atlassian.net/browse/PIC-1134) to set appropriate cpu and memory request and limits, issue [PIC-1289](https://dsdmoj.atlassian.net/browse/PIC-1289) was raised because there was unwanted throttling happening in prod after the change causing poor performance. 

## Decision

Following some discussion with Cloud Platform and a bit of research we hypothesise that the issue was caused by a non-obvious quirk of how Kubernetes uses CPU requests and limits which can cause heavy throttling where CPU limit is low relative to CPU request.

The key things to note are:
- The CPU request has no bearing on throttling whatsoever, it is only used for pod allocation (a node must have at least this much to be allocated)
- The CPU limit provides an upper limit to how much CPU time a pod can use over a given period (it's not clear what exactly this period is but it's likely to be on the order of hundreds of milliseconds to seconds)

Our current situation is that we have a relatively low limit of 1000m compared to the request of 500m, and we scale out at 100% of CPU request. Because our load profile is spiky we believe we are seeing throttling occur for short periods of time which has 2 consequences:
- It limits processing time at high load causing the application to respond slowly
- It prevents the horizontal scaling threshold of 100% being reached so we never spin up new pods to spread that load


## Consequences

The hope is that setting a *high* cpu limit of 10*request (5000m) will allow the pods to get adequate CPU time at times of heavy load. This in turn will allow the horizontal scaling threshold to be reached allowing persistently high loads to be distributed over multiple pods.  
