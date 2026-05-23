# 26. Solution facilitates a coherent set of business functions

Date: 2020-09-21

## Status

Accepted

Implements [17. DDD defines ubiquitous language](0017-ddd-defines-ubiquitous-language.md)

Implemented by [28. A solution is implemented by one or more GCP projects](0028-a-solution-is-implemented-by-one-or-more-gcp-projects.md)

## Context

A lot of different functions are required to support the business. These functions can be grouped into coherent sets, referred to as a solution. The functionality defined by the set of functions can then be implemented on the platform, fulfilling the business requirements.
The solution can also implement domain crossing functionality, e.g. a service provided from one domain that is consumed in another domain.

## Decision

We define a solution as the implementation of a coherent set of business functions on the platform.

## Consequences

### Advantages

* Grouping functions into solutions makes implementation and management easier.
* The solution scopes the implementation, allowing modular design.

### Disadvantages

* Many different solution scopes can be defined to group the functions of a domain, the actual defined scope has impact on the changability and flexibility of the resulting implementation. Therefore, scoping the solutions is difficult and cannot be done without vision and strategy.
