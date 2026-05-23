# 6. use prometheus as monitoring service

Date: 2020-05-25

## Status

Accepted

## Context

This was a clear goal of the challenge: to observe the solution.

As etcd has a metrics endpoint with the structure supported by prometheus,
 it's a logical solution to use it.

Prometheus has several discovery services that can help in a cloud environment.

- static target file
- service discovery modules
  - sd_ec2: plugin to discover AWS instances.

## Decision

I have tested the sd_ec2 plugin and it works fine.  I prefer to implement it
 rather than trying to implement a provisioner in the configuration management
 system that modifies the static target file to add and remove instances.



## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
