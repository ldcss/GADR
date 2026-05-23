# Documentation structure


## Context

This project is well suited to experiment with documentation strategies as well. Additionally, if it will grow larger, having a good documentation in place will only help its further development and maintenance.


## Decision

We will write documentation according to the following structure:
```
system
    features: description of features and use cases, with the Gherkin language
    decisions: log of design and architectural decisions
    architecture
        components: description of feature components (plugins)
        systems: description of deployable systems (adapters)
source code docblocks
```

This structure might be subjected to revision the more it's used and evaluated. Additional inspiration can be drawn from https://www.altexsoft.com/blog/business/software-documentation-types-and-best-practices/.


## Status

Proposed


## Consequences

Decisions and descriptions of already developed components should be added to the documentation a little at a time.

Future decisions should be recorded, systems and components should be documented, and necessary docblocks should be written as soon as new work is done on the project.
