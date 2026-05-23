# 13. Adopt Contract-first with OpenAPI

Date: 2019-10-27

## Status

Accepted

## Context

Contract-first approach enforces a definition of the API contract before implementation. This ensures that the API is
well designed for specific use-cases, based on consumers point of view.

Adopting a contract-first approach forces to ensure that contract is not broken during implementation and evolution of
the application.

We need to ensure that the contract is well defined through a specification and implementation respects this specification.

## Decision

[OpenAPI Specification](https://swagger.io/specification/) will be used to enforce contract-first approach.

## Consequences

The API contract definition must respect the OpenAPI specification.

Incoming requests and outgoing responses will be validated against the contract.

The OpenAPI contract will be exposed through a dedicated endpoint to let consumers retrieve it.
