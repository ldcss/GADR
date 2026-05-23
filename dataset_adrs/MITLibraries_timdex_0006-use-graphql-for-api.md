# 6. Use GraphQL for API

Date: 2023-08-07

## Status

Accepted

Supercedes [4. Use OpenAPI Specification](0004-use-openapi-specification.md)

## Context

The initial TIMDEX implementation chose a REST API. During development of new expanded features, we revisted this decision and looked at our options and needs.

### Options Considered

#### GraphQL

**Description:** GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.

**Pros:**

- GraphiQL interactive editor allows users to explore the API without writing any code
- Users can request the exact data they want as part of the query
- Schema allows users and applications to import and understand data types

**Cons:**

- Requires developers to learn GraphQL syntax
- More difficult to scale with simple caching

#### OpenAPI spec REST API

**Description:** The OpenAPI Specification is a specification for machine-readable interface files for describing, producing, consuming, and visualizing RESTful web services.

**Pros:**

- REST APIs are comfortable for many developers as they have used them before
- uses OpenAPI spec and transitioning to V2 in OpenAPI would be familiar

**Neutral:**

- v2 requires significant changes to v1 and is essentially a rewrite so any apps using v1 will need to make changes regardless of if we keep this similar spec
- Auto generation of documentation is useful, but does not meet all of our documentation plans for v2

**Cons:**

- Requires many decisions to be made as to how to request data when designing the spec
- The only way to know how to use the API will be to rely on our spec and our documentation

#### JSON API

**Description:** JSON:API is a specification for how a client should request that resources be fetched or modified, and how a server should respond to those requests. JSON:API is designed to minimize both the number of requests and the amount of data transmitted between clients and servers. This efficiency is achieved without compromising readability, flexibility, or discoverability.

**Pros:**

- Adds standardization to REST APIs

**Cons:**

- Unclear how well adopted it is

## Decision

We will replace our REST API with a GraphQL API.

## Consequences

Users can request the specific fields they want, and we can more easily handle field deprecations.

We will also have a GraphQL playground for testing queries without having to write code.
