# Logging Approach

* Status: Accepted
* Deciders: [Daniel Grant](https://github.com/danielgrant),
  [Robert Kenny](https://github.com/kenoir)
* Date: 2020-12-01

Technical Story: to identity and utilise an approach to log management
that aligns with Wellcome Collection's existing logging requirements and
infrastructure.

## Context and Problem Statement

The Identity platform consists of numerous interconnected components,
each responsible for generating their own log outputs. Some of these log
outputs will be driven by the implementation of logging within a
component, and others will be provided "out-of-the-box" by a managed
service. In either case, these logs files must be readily accessible,
queryable, and persisted over a long period.

## Decision Drivers

* Collation of logs to a single, centralised platform utilised by all
  platforms in Wellcome Collection's technical estate.
* Minimal infrastructure / configuration required in components to
  utilise the centralised logging platform.

## Considered Options

* AWS CloudWatch
* Elasticsearch, Logstash, Kibana (ELK)

## Decision Outcome

- For containers deployed into AWS ECS / AWS Fargate, Wellcome
  Collection's existing ELK stack will be utilised. Logs will be pushed
  to the stack via a Firelens sidecar containers.

- For all log generating services (e.g. Lambda Function and API Gateway
  logs), the default AWS CloudWatch configurations will be used.
