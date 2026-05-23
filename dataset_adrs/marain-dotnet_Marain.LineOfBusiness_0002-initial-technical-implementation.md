# API Design and Background

## Status

Proposed

## Context

As described in ADR0001, we are intending to build a new Marain API providing a standardized schema for common entities used in line-of-business applications.

This API is logically separated into three, as described by [the service definition files here.](https://github.com/marain-dotnet/Marain.LineOfBusiness/tree/master/Solutions/ServiceDefinitions/Prototyping):
- Organizational units and their data and relationships
- People and their data and relationships
- The relationships between organizational units and people

For the initial implementation we have a number of decisions to make:

### Level of separation of APIs

Here we have three choices.
1. Implement the three APIs as completely separated services, each with their own underlying storage. This would give the most flexibility in implementation, but would also be the most complex. It would likely require an element of data synchronization between the services, as some level of denormalization would be necessary to make the APIs useful in their own right.
2. Implement the three APIs as a single service, sharing a common store. This would be the simplest solution, but would be a difficult decision to reverse at a later date should it become necessary.
3. Implement the three APIs as separate services but use common storage. This is a balance between the first two options, providing a simple initial implementation but making it relatively straightforward to separate out the three services at a later date if required.

### Underlying storage selection

As always, we need to determine the most appropriate storage mechanism for the APIs. To some degree, this will depend on the level of separation decided upon.

However, since a large part of these APIs is about describing relationships between entities, a graph model is the obvious choice. If we do completely separate the three APIs, then it will make sense to use a graph database for the organizational unit and person APIs; the API that holds the relationship between organizational units and people could be either a standard document database or a graph database.

## Decision

### We will implement separate services over a single data store

This option gives us a simple path to v1 of the service but leaves us the option of further separating the APIs in the future.

### We will use a Graph database to implement storage

As described above, this is the obvious choice for an API of this nature.

## Consequences

### Care must be taken when extending the APIs to ensure we don't make it harder to separate them out in the future

With the three APIs sharing a common data store, it will be tempting when extending the APIs to allow data to "bleed" between them, which will increase their coupling. This problem applies particularly to the API which links people and organizations. The data returned by this API should be kept to a minimum.
