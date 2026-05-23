# 7. Use Ubuntu 18.04

Date: 2018-08-15

## Status

Accepted

## Context

Prometheus needs to run on a Linux distribution. The choice of distribution impacts the methods of packaging, deploying and configuring Prometheus. It is important to consider what is currently used across GDS as prior experience of distribution is helpful when supporting the service. Ubuntu is currently in use in Verify and GOV.uk (and possibly others) which provides a pool operators with the experience to be able to support the service.
Alternatives considered were Amazon Linux, the advantage of this distribution is that it is optimised to the Amazon cloud, however this advantage did not overcome the advantage of familiarity across GDS Reliability Engineering 

## Decision

Use Ubuntu 18.04 LTS

## Consequences

Ubuntu provide security updates and support until 2023, reducing the support burden. The use of Ubuntu matches other programs choice.
