# 27. A GCP project belongs to a single domain

Date: 2020-09-21

## Status

Accepted

Implements [17. DDD defines ubiquitous language](0017-ddd-defines-ubiquitous-language.md)

Related to [25. Domains correspond to business departments](0025-domains-correspond-to-business-departments.md)

Related to [28. A solution is implemented by one or more GCP projects](0028-a-solution-is-implemented-by-one-or-more-gcp-projects.md)

## Context

The projects structure of the platform can be used to protect components. By the seperation into projects a modular, loosely coupled design is created. A project belongs to a single [domain](0025-domains-correspond-to-business-departments.md), a domain can consist of multiple projects. The project implements a coherent set of functions within a single domain.

## Decision

The set of functions implemented in one GCP project belongs to a single domain.

## Consequences

### Advantages

* A modular design improves changability and maintainability.
* The platform provides controls to protect resources within a project from being accessed from the outside.
* The amount and complexity of deployment pipelines within a project is limited, making it easy to oversea and manage.
* Responsibility for platform functionality can be assigned at project boundaries.

### Disadvantages

* A lot of projects will exist, which could be overwhelming and hard to manage.
* Projects creation and access management is an additional cost factor.
