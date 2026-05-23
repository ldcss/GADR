# 17. DDD defines ubiquitous language

Date: 2020-09-21

## Status

Accepted

Implemented by [24. Refer to BLOB at the source project](0024-refer-to-blob-at-the-source-project.md)

Implemented by [25. Domains correspond to business departments](0025-domains-correspond-to-business-departments.md)

Implemented by [26. Solution facilitates a coherent set of business functions](0026-solution-facilitates-a-coherent-set-of-business-functions.md)

Implemented by [27. A GCP project belongs to a single domain](0027-a-gcp-project-belongs-to-a-single-domain.md)

Implemented by [28. A solution is implemented by one or more GCP projects](0028-a-solution-is-implemented-by-one-or-more-gcp-projects.md)

Implemented by [29. Components are named according to naming conventions](0029-components-are-named-according-to-naming-conventions.md)

## Context

Domain-driven design (DDD) is the concept that the structure and language of software code (class names, class methods, class variables) should match the business domain. For example, if a software processes loan applications, it might have classes such as LoanApplication and Customer, and methods such as AcceptOffer and Withdraw.

DDD connects the implementation to an evolving model.

Domain-driven design is predicated on the following goals:
- placing the project's primary focus on the core domain and domain logic;
- basing complex designs on a model of the domain;
- initiating a creative collaboration between technical and domain experts to iteratively refine a conceptual model that addresses particular domain problems.

Concepts of the model include:

### Context
The setting in which a word or statement appears that determines its meaning;
### Domain
A sphere of knowledge (ontology), influence, or activity. The subject area to which the user applies a program is the domain of the software;
### Model
A system of abstractions that describes selected aspects of a domain and can be used to solve problems related to that domain;
### Ubiquitous Language
A language structured around the domain model and used by all team members to connect all the activities of the team with the software.

## Decision

We In the context of the ODH we will use the pricniples of Domain Driven Design and use the language which is related to the business where it is operated.

## Consequences

In order to help maintain the model as a pure and helpful language construct, the team must typically implement a great deal of isolation and encapsulation within the domain model. Consequently, a system based on domain-driven design can come at a relatively high cost. While domain-driven design provides many technical benefits, such as maintainability, Microsoft recommends that it be applied only to complex domains where the model and the linguistic processes provide clear benefits in the communication of complex information, and in the formulation of a common understanding of the domain

References: https://en.wikipedia.org/wiki/Domain-driven_design
