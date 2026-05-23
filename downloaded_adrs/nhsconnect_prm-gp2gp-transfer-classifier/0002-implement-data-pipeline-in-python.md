# 2. Implement Data Pipeline in Python

Date: 2020-01-20

## Status

Accepted

## Context

We are looking to build a dashboard that will display GP2GP related metrics.
This information could be obtained from one or more sources, including SPINE,
GP2GP MI and ODS portal. The initial features are expected to be powered by
data derived from SPINE messages. However, the format and level of granularity
of this data set does not make it suitable for directly powering a dashboard.
Therefore a data pipeline is needed to interpret the metrics and outcomes
implied by these low level system messages.

It is assumed that:
- The pipeline will be deployed on public cloud, likely AWS.
- This codebase will receive contributions from polyglot software engineers.
- The pipeline will need to interact with web APIs

## Decision

We have decided to implement the data pipeline in Python 3.

## Consequences

Python has a well established ecosystem for many of our core use cases,
including data manipulation, interacting with AWS, and working with web APIs

We can also leverage “big data” tooling like Spark, which has good integration
with Python. This is something we may need to use if we decide to process data
across multiple machines.

We considered Javascript, as this is another language the team is familiar
with, but its data ecosystem is less mature.

While not everyone in the team is currently fluent in Python, it is a very
mainstream language and one that is fairly easy to learn.

Python is a dynamically typed language that places an emphasis on "forgiveness
over permission". We should be mindful of the trade-offs this introduces for
working with data.

Python may not be fastest or most efficient for CPU intensive tasks. This can
be mitigated by using libraries which are partially implemented in lower level
language like C.
