[Home](../../README.md)


# 4. Serverless Framework

Date: 2020-09-21

## Status

Accepted

## Context

We are building a `"Hello World"` application with AWS Lambda. What
tools or frameworks can we leverage?

## Decision

We will use the [Chalice] framework to buiild our serverless
application.

## Consequences

**Pros:**

* Designed for [Python]
* Built and maintained by AWS (and open source community)
* Good documentation

**Cons:**

* Limited support for IaC tools like Terraform


<br/>

[Previous](003-runtime.md) | [Next](005-test-framework.md)


[Chalice]: https://aws.github.io/chalice/
[Python]: https://www.python.org/downloads/release/python-380/
