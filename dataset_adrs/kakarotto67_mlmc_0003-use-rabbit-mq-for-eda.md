# Use RabbitMQ for messaging & publish-subsribe pattern

* Status: [accepted]
* Deciders: [[@kakarotto67](https://github.com/kakarotto67)]
* Date: [2019-09-13]

Technical Story: [Setup Message Bus for MLMC](https://github.com/kakarotto67/mlmc/issues/7)

## Context and Problem Statement

Different services are going to push different kind of messages so there is a need in EDA architecture and some messaging server.

## Decision Drivers

* Easy to use
* Easy to learn
* Possibility to run from Docker

## Considered Options

* [RabbitMQ](https://www.rabbitmq.com/)
* [NServiceBus](https://particular.net/nservicebus)

## Decision Outcome

Decided to use RabbitMQ since

* It provides exact functionality that is neded for the product (publish-subscribe event messaging)
* It is easy to learn and use and I already had some knowledge of how to use it
* It has official container on Docker Hub
* It seems to be popular and trending these days

### Positive Consequences

* I will be able to setup EDA messaging in the product.

### Negative Consequences

* n/a

## Links

* n/a
