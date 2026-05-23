# 12. Use ECS for hosting applications

Date: 2018-07-18

## Status

Accepted

## Context

This ADR applies to the applications outlined in [ADR-0004][adr-0004].

In [ADR-0008][adr-0008] we've decided that we will host the service using Amazon
Web Services (AWS). In [ADR-0005][adr-0005] we decided to use Docker to
containerise applications so we could use a Platform as a Service offering.

AWS offers 2 Platform as a Service hosting platforms for Docker containers:
[Elastic Beanstalk][service-beanstalk] (Beanstalk) and [Elastic Container
Service][service-ecs] (ECS).

Both services offer similar capabilities, including the ability to automatically
scale the application based on usage metrics.

Beanstalk's container environment is a wrapper on-top of ECS, which abstracts
some elements away from the service. Using ECS directly allows for more
fine-grained control.

## Decision

We will use ECS for hosting the applications outlined in [ADR-0004][adr-0004].

## Consequences

We will need to build and configure the ECS environment using Terraform as
outlined in [ADR-0006][adr-0006].

[adr-0004]: 0004-use-ruby-on-rails-for-applications.md
[adr-0005]: 0005-use-docker-for-applications.md
[adr-0006]: 0006-use-terraform-to-create-and-document-infrastructure.md
[adr-0008]: 0008-use-aws-for-hosting.md
[service-beanstalk]: https://aws.amazon.com/elasticbeanstalk/
[service-ecs]: https://aws.amazon.com/ecs/
