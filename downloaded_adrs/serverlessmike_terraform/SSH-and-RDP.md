# Use of SSH and RDP

Date: 03/10/2019

## Context

We currently use RDP for Windows Server and SSH for Linux to connect to the servers to be migrated, when we have server administration tasks to perform. However, if EC2 instances are stateless, then we would not need to log into these servers, if they are sick, then then can be terminated.

## Decision

RDP and SSH are allowed for all non-production EC2 istances, but are left blocked for production EC2 instances.

## Consequences

Administrators will not be able to log into the production EC2 instances that the project creates. We will have to automatically ship the Windows WEvent logs and Linux syslogs to a central location or database in order to view them. Other administration tasks will need to be automated and deployed using Terraform.
