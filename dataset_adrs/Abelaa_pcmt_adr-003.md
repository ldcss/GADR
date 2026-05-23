# 3. Cloud Provisioning through Terraform

## Status


Accepted, 2019-07-01

## Context

Deploying to the cloud is a fundamental part of increasing software delivery
frequency.  However once the frequency is increased, it becomes increasingly 
needed to manage the provisioning and configuration of those cloud resources
lest a step is forgotten, a security vulnerability is found, or an instance is
corrupted.  Following patterns found in software development, such as managing
infrastructure as code (IaC) and tracking changes in source control, are
widely regarded as good practice today.

Many cloud providers have bespoke tooling that helps manage the creation of 
resources on their infrastructure.  While this tooling is hugely powerful, the
context of PCMT is that our cloud resources should be kept as simple as
possible, in part due to our constraint to allow for on-prem deployments.
Further an organization that chooses to deploy PCMT as a SaaS may not use the
same cloud provider as the one the PCMT project uses.

## Decision

We will use Terraform to provision cloud resources:  compute instances, 
storage, DNS, etc.

## Consequences

Terraform is a newer IaC tool that has support for multiple cloud providers,
however not all cloud providers, or all advanced capabilities of the supported
cloud providers may be available through Terraform.

---
Copyright (c) 2019, VillageReach.  Licensed CC BY-SA 4.0:  https://creativecommons.org/licenses/by-sa/4.0/
