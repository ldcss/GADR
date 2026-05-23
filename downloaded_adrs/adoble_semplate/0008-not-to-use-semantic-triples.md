# Not to use semantic triples

* Status: Accepted
* Date: 2021-02-18

## Context and Problem Statement

Semantic information can be represented using sematic triples  as defined in the [W3C Resource Description Framework - RDF](https://www.w3.org/RDF/).

Is this an option for `semplate`?


## Considered Options

* Use a notation based on semantic triples
* Use a notation based on the fieldname of Java object being processed by `semplate`

## Decision Outcome

As the library is intended to be directly call from Java programs, the **notation is based on the fieldname of Java object being processed**.
