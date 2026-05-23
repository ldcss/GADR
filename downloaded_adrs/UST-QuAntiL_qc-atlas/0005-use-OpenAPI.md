# Use OpenAPI specification

* Status: accepted
* Deciders: [Q-tal Enpro Team]

## Context and Problem Statement

The API has to be documented in human and machine readable form. If the API is documented in machine readable form, the automatic generation of client services is possible.

## Decision Drivers

* readable API documentation
* effort of manually creating client services

## Considered Options

* Use OpenAPI
* Use Spring Restdocs

## Decision Outcome

Chosen option: Use OpenAPI, because the API is described in a standardized format which is human and machine readable.

### Positive Consequences

* Standardized documentation of the API
* Automatic service generation for clients is possible

### Negative Consequences <!-- optional -->

* OpenAPI annotations have to be maintained

## Pros and Cons of the Options <!-- optional -->

### Use OpenAPI

The OpenAPI specification is a standardized API description format, [see](https://swagger.io/docs/specification/about/). 

* `+` The API is described in a standardized format
* `+` Clients may automatically generate services
* `-` Annoations have to be maintained

### Spring Restdocs

Combines hand written and automatically generated documentatio, [see](https://spring.io/projects/spring-restdocs).

* `+` some documentation is generated automatically
* `-` it's not machine readable
