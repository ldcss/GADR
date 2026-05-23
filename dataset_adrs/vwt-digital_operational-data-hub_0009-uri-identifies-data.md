# 9. URI identifies data

Date: 2020-09-21

## Status

Accepted

Implemented by [57. Naming convention defines URI tags](0057-naming-convention-defines-uri-tags.md)

Related to [11. CQRS separates read and write responsibility](0011-cqrs-separates-read-and-write-responsibility.md)

## Context

A Uniform Resource Identifier (URI) is a string of characters that unambiguously identifies a particular resource. To guarantee uniformity, all URIs follow a predefined set of syntax rules, but also maintain extensibility through a separately defined hierarchical naming scheme (e.g. http://).

To be able to unambiguously identify any element of data, a URI will be defined for every element of data on the ODH platform. Building this URI from meaningful attributes instead of technical randomly generated ids makes it recognizable and easier to use. However, selecting the right attributes and context information to assure uniqueness is challenging.

The URI scheme to use is [tag](https://tools.ietf.org/html/rfc4151). Tag URIs are quite human readable, but, unlike http URIs, not resolvable. This makes them suitable for identifying real-life things (entities) that have a representation on the ODH. A URI can be defined from the hierarchy of the organisation, forming a path to the resource. For example, if mycompany has a catalog with articles and one of the articles has article# 313, an article URI could be defined as `tag:vwt.digital,2020:mycompany/catalog/articles/313`

## Decision

We define a URI according to the [tag scheme](https://tools.ietf.org/html/rfc4151) for each entity that has a representation on the ODH platform.

## Consequences

### Advantages

* Entity representations can be linked to the entity in a clear and specific way.

### Disadvantages

* It can be challenging to find a truely unique identification, changes in context or semantics sometimes result in unanticipated changes to the uniqueness of an identifier.
* Multiple URIs can exist for an entity, e.g. a representation of an employee could exist in multiple, unlinked domains. Maintenance and procedures are required to manage this.

## References

* https://en.wikipedia.org/wiki/Uniform_Resource_Identifier, retrieved 24 September 2020
* https://tools.ietf.org/html/rfc4151, retrieved 30 September 2020
