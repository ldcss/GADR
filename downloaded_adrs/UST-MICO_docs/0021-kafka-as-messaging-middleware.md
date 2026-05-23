# Kafka as Messaging Middleware


## Context and Problem Statement

To compose service with the mico application we need a messaging middleware that is highly scalable and supports the [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com).


## Decision Drivers

* Should be a well known and proven solution
* Support a pipes and filters style architecture


## Considered Options

### [Apache Kafka](http://kafka.apache.org)

Pro: Proven system with high scalability. Well suited for pipes and filters architectures.

Contra: Topics have different semantics than traditional message queues. Some patterns don't work well/at all with the topic semantic.

### Some other messaging middleware

This option was not explored further.


## Decision Outcome

We want to use Kafka as our messaging middleware.

### Important things to know about Kafka

Kafka topics have a different semantic than traditional message queues. Kafka also does NOT log wether a message was consumed. It only stores the last comitted offset for a consumer. Because of that and the different topic semantic some patterns need to be adapted to work with Kafka.

For more detailed information about the inner workings of Kafka consult the following links:

 *  [Client subscriptions](https://kafka.apache.org/intro#intro_consumers)
 *  [Client positions](https://kafka.apache.org/documentation/#design_consumerposition)
 *  [Guarantees for message delivery](https://kafka.apache.org/intro#intro_guarantees)
 *  [Message delivery modes (how to achive exactly once)](https://kafka.apache.org/documentation/#semantics)
 *  [Use topics storage for key based data](https://kafka.apache.org/documentation/#compaction)
