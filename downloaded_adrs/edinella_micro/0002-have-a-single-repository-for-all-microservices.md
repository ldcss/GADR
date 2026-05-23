# Have a single repository for all microservices

## Context and Problem Statement

A repository for each microservice or only one for all of them?

## Decision Drivers

* Development agility
* Microservices decoupling
* Big-picture scenario visibility

## Considered Options

* A repository for each microservice, and another for service definitions
* A single repository with decoupled microservices including service definitions

## Decision Outcome

Chosen option: A single repository for all microservices and service definitions this time, because this way its easy to get a big picture of the approach, for the purposes of this example.

In production, I'll consider separating microservices and service definitions on repos, in order to have separate triggers on CI for them.

I think [this approach](https://medium.com/namely-labs/how-we-build-grpc-services-at-namely-52a3ae9e7c35) will be a good fit for address this concern in production.
