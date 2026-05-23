# 3. Not PaaS

Date: 2017-11-22

## Status

Accepted

## Context

The first architecture considered was using the PaaS. 

This tool collects data about misconfigurations in a 
database. Since the data held is quite sensitive we 
wanted to take all reasonable measures to protect that 
data.

There are a lot of advantages to using the PaaS in that 
it limits the amount of work required for common 
operational tasks like deployment and monitoring.  

## Decision

At the present time we felt the Paas was not a viable 
option for this tool because of the following: 
* Shared tenancy RDS 
* Shared tenancy VPC 
* No ability to natively control ingress
* No ability to control egress

__Some of these issues are being addressed by the PaaS so 
we may revisit this decision in future.__

## Consequences

By not using the PaaS we can implement our own RDS 
instance with no other users in a more tightly controlled 
VPC where we can control ingress and egress. 

By not using the PaaS there are a number of thingss we 
have to do for ourselves like health monitoring. 

We are also responsible for managing the infrastructure 
we build to support it. 

