# Fluid Interface

* Status: Accepted
* Date: 2021-04-24
* Supercedes #0003

## Context and Problem Statement

How does a client use the interface?

## Considered Options

* A **single class** whose public methods form the API.
* A set of classes that provide a [fluent API](https://martinfowler.com/bliki/FluentInterface.html) which redirects to other components

## Decision Outcome

Chosen option is to implement as a **fluent API**, as early use of the library showed that this was easier to understand and provided a means 
to expand the evolve the functionality.
