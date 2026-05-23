[Home](../../README.md)
 
 # 2. Compute

Date: 2020-09-21

## Status

Accepted

## Context

We want to build a `"Hello World"` application using one of the
following approaches:

* **Containers** (i.e. K8S, ECS, EC2, etc.)
* **Serverless** (i.e. AWS Lambda)

## Decision

We will use AWS Lambda for this particular assignment.

## Consequences

**Pros:**

* Cost effective
* Optimised for short running processes (i.e. functions)
* Low/no infrastructure to manage (i.e. servers)
* Well suited to stateless applications

**Cons:**

* Cold starts
* Vendor lock-in (i.e. containers are more portable)
* See [AWS Lambda Limits] for more details

<br/>

[Previous](001-record-decisions.md) | [Next](003-runtime.md)


[AWS Lambda Limits]: https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html
