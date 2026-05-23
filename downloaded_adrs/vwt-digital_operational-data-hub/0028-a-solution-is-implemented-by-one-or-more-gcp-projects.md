# 28. A solution is implemented by one or more GCP projects

Date: 2020-09-21

## Status

Accepted

Implements [17. DDD defines ubiquitous language](0017-ddd-defines-ubiquitous-language.md)

Implements [26. Solution facilitates a coherent set of business functions](0026-solution-facilitates-a-coherent-set-of-business-functions.md)

Related to [27. A GCP project belongs to a single domain](0027-a-gcp-project-belongs-to-a-single-domain.md)

## Context

A [solution facilitates a coherent set of business functions](0026-solution-facilitates-a-coherent-set-of-business-functions.md). Those functions can originate from multiple domains. A [project always belongs to a single domain](0027-a-gcp-project-belongs-to-a-single-domain.md). Therefore, a solution can be implemented by multiple projects, either due to the fact that it requires functions from multiple domains, or because projects allow better modularization of the solution, or both.

![Structure of projects, domains and solutions](solution_project_domain.png "Projects in different domains implementing a solution")

## Decision

We implement a solution by one or more projects.

## Consequences

### Advantages

* The platform's project structure is used to facilitate separation of concerns and modularization.
* Responsibility for functionality is easily defined along the project boundaries.

### Disadvantages

* Additional overhead when multiple small projects need to be created as functionality from multiple domains is required.
