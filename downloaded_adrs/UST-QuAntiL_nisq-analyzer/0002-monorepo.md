# Go Monolith First

* Status: accepted
* Deciders: [Marie Salm, Benjamin Weder, Manuela Weigold, Karoline Wild]
* Date: [2020-03-18] <!-- optional -->

## Context and Problem Statement

Should the components in the PlanQK platform be splitted into individual repos?

## Considered Options

* use a separate repo for the main components (NISQ analyser, core, semantic knowledge graph component)
* Monolith: use one repo

## Decision Outcome

Start with a monorepo, split up later if needed. Let FOCUS decide what is best for their semantic knowledge graph component.

### Positive Consequences <!-- optional -->

* Recommended approach by [Martin Fowler](https://martinfowler.com/bliki/MonolithFirst.html)


