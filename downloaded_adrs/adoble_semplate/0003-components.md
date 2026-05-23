# Components

* Status: Rejected
* Date: 2021-04-24
* **Superceded** by ADR #0009

## Context and Problem Statement

What are the main components of the library?

## Considered Options

* A class implemented the [facade pattern](https://en.wikipedia.org/wiki/Facade_pattern) that provides the API and redirects to other components
* A **single class** whose public methods form the API.

## Decision Outcome

Chosen option is to implement as a **single class**, as the foreseen complexity of the library does not justify the extra complexity of developing a facade pattern implementation.  
