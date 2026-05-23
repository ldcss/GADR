# 3. Install Kubernetes directly on metal, as a single node

Date: 2020-06-16

## Status

Accepted

## Context

- I wasn't getting anything built with all of the libvirt shenanigans
- I have a NAS now, so things I'm worried about running on Kubernetes can go there

## Decision

Install Kubernetes straight onto a Debian install on `swan`. Use MetalLB or similar later to manage the routing.

## Consequences

- It'll be more dangerous running things outside of the cluster on that machine

  - Might be able to mitigate with [KubeVirt]?

[KubeVirt]: https://kubevirt.io/
