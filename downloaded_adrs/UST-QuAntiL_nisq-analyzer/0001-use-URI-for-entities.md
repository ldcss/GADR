# Use URI to enable links to entities of the Pattern/QC Atlas

* Status: accepted
* Deciders: [Marie Salm, Benjamin Weder, Manuela Weigold, Karoline Wild]
* Date: [2020-03-18] <!-- optional -->

## Context and Problem Statement

In the near future, QC Algorithms stored in the platform will reference QC patterns stored in the Pattern Atlas and vice versa.
We need references for the links.

## Considered Options

* UUIDs
* URIs

## Decision Outcome

Chosen option: "[URIs]", because UUIDs are generated and thus depend on the underlying database system.
We will use them as natural ids, so the database will check uniqueness of the uri identifiers.

### Positive Consequences <!-- optional -->

* We follow solid [W3C specification](https://www.w3.org/Addressing/URL/uri-spec.html)


