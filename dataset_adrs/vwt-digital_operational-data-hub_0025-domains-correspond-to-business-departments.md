# 25. Domains correspond to business departments

Date: 2020-09-21

## Status

Accepted

Implements [17. DDD defines ubiquitous language](0017-ddd-defines-ubiquitous-language.md)

Related to [27. A GCP project belongs to a single domain](0027-a-gcp-project-belongs-to-a-single-domain.md)

## Context

The organizational model of a company has a great influence on the communication structure in the company. Within a department, people tend to use the same terminology and definitions. This relates closely to the definition of ubiquitous language. Therefore, the domain model used on the platform should be closely related to the organizational model of the company. This is also supported by Conway's law.

## Decision

We will structure the domain model on the platform around the departments organizational model of the company.

## Consequences

### Advantages

* People working closely together will use the same language, definitions and terminology of the department can be used, no need to go through difficult agreement on these things between departments.
* Domains will also determine the structure on the platform, when linking domains to departments, there is no counterforce from Conway's law.

### Disadvantages

* Changes in the organizational model will impact the domain model. This will result in synonyms or obsolete names being used or renaming platform components to reflect the new structure.

## References

* https://en.wikipedia.org/wiki/Conway%27s_law, retrieved 13 October 2020
