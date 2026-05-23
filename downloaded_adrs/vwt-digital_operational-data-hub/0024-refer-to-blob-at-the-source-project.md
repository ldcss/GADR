# 24. Refer to BLOB at the source project

Date: 2020-09-21

## Status

Accepted

Implements [17. DDD defines ubiquitous language](0017-ddd-defines-ubiquitous-language.md)

## Context

Although inter-domain communication should be done using ODH topics, this technology is less suitable to transfer large binary objects. Therefore, references of large binaries are communicated on the ODH topics instead of the large binary itself. This reference can be used by consumers to retrieve the binary object at its source.

## Decision

Instead of the large binary object itself, we will pass references to it on ODH topics, which can be used by consumers to retrieve the object at its source.

## Consequences

### Advantages

* Efficient and effective communication around large binary objects.

### Disadvantages

* Inter-dependency from projects consuming large binary objects to projects sourcing the objects.
* Permissioning on the storage of large binary object needs to be configured for each consumer.
