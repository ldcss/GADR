# 8. Use AWS for hosting

Date: 2018-06-11

## Status

Accepted

## Context

[CCS-ADR-0001][ccs-adr-0001] says that all new services should use a common
cloud hosting provider.

This will enable CCS to consider consolidating future support and operations
for these services.

The decision is to use Amazon Web Services (AWS) for the next 6 months.

### Impacts on Data Submission Service

In [ADR-0005][adr-0005] we decided to use Docker for packaging applications to
allow us to use a Platform as a Service offering.

In [ADR-0006][adr-0006] we decided to use Terraform to create and document our
cloud based Infrastructure.

Terraform supports building infrastructure in AWS, and AWS provides several
Platform as a Service offerings for applications in Docker containers (Elastic
Beanstalk and Elastic Container Service).

## Decision

Data Submission Service will be hosted in AWS.

## Consequences

Our Docker containers will be deployed to either Elastic Beanstalk or Elastic
Container Service on AWS, and we will use Terraform to build our AWS
infrastructure

[ccs-adr-0001]: https://github.com/Crown-Commercial-Service/CCS-Architecture-Decision-Records/blob/master/doc/adr/0001-use-a-common-cloud-provider.md
[adr-0005]: 0005-use-docker-for-applications.md
[adr-0006]: 0006-use-terraform-to-create-and-document-infrastructure.md
