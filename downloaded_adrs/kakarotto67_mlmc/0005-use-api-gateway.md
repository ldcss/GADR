# Use API Gateway for MLMC app

* Status: [proposed]
* Deciders: [[@kakarotto67](https://github.com/kakarotto67)]
* Date: [2019-09-14]

Technical Story: [Move all interservices communication into API Gateway](https://github.com/kakarotto67/mlmc/issues/11)

## Context and Problem Statement

For Microservices architecture it is a good idea to have API Gateway service to manage interservices communication and handle cross-cutting concerns (logging, security, caching, etc.).

## Decision Drivers

* Easy to use
* Easy to learn
* Can be hosted on Azure
* Can be hosted in Docker container

## Considered Options

* [Ocelot](https://threemammals.com/ocelot/)
* [Azure API Management](https://azure.microsoft.com/en-us/services/api-management/)

## Decision Outcome

No outcome yet. Have to investigate both a bit and then will decide.

### Positive Consequences

* I will be able to manage communication between services more effectively and securely with API Gateway.

### Negative Consequences

* n/a

## Links

* n/a
