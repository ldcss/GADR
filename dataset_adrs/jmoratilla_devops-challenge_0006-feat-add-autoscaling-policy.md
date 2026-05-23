# 6. feat-add-autoscaling-policy

Date: 2020-02-20

## Status

Accepted

## Context

Goal: The platform must be scalable according to the load

We need to autoscale nodes in case we need to cope with a high load.

I have researching, and I have found that we have to scale the nodes
 as well as the pods.

For some loads, scaling pods can be enough, but for other workloads it
 can be better to scale the cluster nodes.

Issues then:

1. Autoscaling pods
2. Autoscaling nodes




## Decision

For the first issue, I'm going to use:

* [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

This object is a controller and an API resource that is included in kubectl.  It
 allows to set a period of time to check the load of a pod (cpu or custom metrics)
 and increase the number of pods running.

For the second issue, I'm going to use:

* [Cluster Autoscaler Addon](https://github.com/kubernetes/kops/tree/master/addons/cluster-autoscaler)

With this addon, you can set a policy in AWS IAM and attach it to the previously
 defined autoscaling group for nodes.

I haven't found another way to set the AutoScale of the nodes instanceGroup 


## Consequences

This is complex to me, as I use to manually manage the load of the system and
 plan the scaling based on schedules.

A problem it can occurs is that by any mean, somebody attacks the services so
 the cluster begins to grow uncontrolled and spend money and resources.

