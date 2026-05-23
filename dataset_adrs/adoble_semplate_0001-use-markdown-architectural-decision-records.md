# Use Markdown Architectural Decision Records

* Status: Accepted
* Date: 2021-02-18


## Context and Problem Statement

We want to record architectural decisions made in this project. Which format and structure should these records follow?

## Considered Options

* [MADR 2.1.0](https://adr.github.io/madr/)
* [Michael Nygard's template](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
* Formless - No conventions for file format and structure


## Decision Outcome

Chosen option is "MADR 2.1.0", because :

* `semplate` is an open source (OS) project which may have more than  one developers   who are not co-located. Documenting the architecture decisions helps in the cohesiveness of the architecture.
* MADR is lightweight and would fit into the workflow of an OS project.
