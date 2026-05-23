# 1. Hosting on cloud.gov

Date: 2021-08-09

## Status

Accepted

## Context

The purpose of this API is to support the E&I phase of 18F's work with the Administrative Office of the Courts. This work includes creating a small API as well as demonstrating DevOps practices. As such, this project should be continuously deployable in a simple, dependable way. There are many ways to do this including using bash scripts and/or Terraform or other infrastructure-as-code tools with a cloud provider's APIs. For this phase of work our primary infrastructure requirements are a relational database service and a virtual server that is capable of executing Python code and communicating with the server and serving incoming user requests. Additionally, we require a means to deploy to this services in a repeatable, automated way.

## Decision

For this phase of work we will use Cloud.gov and the RDS database service (PostgreSQL) is provides.

## Consequences

Cloud.gov provides all of the services this API currently needs. Additionally, Cloud.gov includes a simple and reliable method to deploy new instances with `cf push`, which works well in continuous integration/delivery tools like CircleCI or Github Actions. Because Cloud.gov already has a Provisional Authority to Operate (P-ATO), it can simplify compliance with federal requirements.

While Cloud.gov runs on top of AWS services and provides many services, including Elasticsearch, Redis, and S3, it does not provide everything available on AWS. It is conceivable that future phases of this project may benefit from services such as Lambda functions, SQS queues, or SNS notifications, which are not currently available on Cloud.gov.
