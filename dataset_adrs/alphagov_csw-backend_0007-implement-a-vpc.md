# 7. Implement a VPC

Date: 2017-11-22

## Status

Accepted

## Context

If running serverless we could choose to operate outside 
a VPC. This has advantages in terms of the latency of 
requests. We would not need a keep-warm function to 
ensure network interfaces were provisioned. 

Lambdas running outside the VPC could not easily access 
RDS running inside a VPC. 

Given the sensitive nature of the data involved it seems
sensible to protect it further by running RDS inside a VPC 
where we have much easier control over ingress and egress.  

## Decision

Implement a VPC.

## Consequences

Given that we are in a serverless environment this means
lambdas provisioning ENIs to access the VPC. We can either 
accept that this means latency for the user or we can 
incur a small extra cost by implementing a keep-warm 
function to ensure the user facing lambdas are always 
provisioned. 

