---
layout: default
title: ADR-0010
nav_order: 13
permalink: records/0010/
---
# Use message broker for asynchronous messaging

* Status: drafted
* Decider(s): <!-- required -->
  * [list everyone involved in the decision]
  * ...
* Date(s):
  * drafted: 2020-02-05

## Context and Problem Statement

SDR is evolving into an (increasing) set of (largely) single-purpose services, with communication between these services occurring via synchronous HTTP. This architecture is fragile as it scales under load and as the number of services increases because:

* Each service must have knowledge about many other services.
* Each service depends on many other services to perform its job; any of these services being unavailable can bring down the service or hamper performance.
* Synchronous HTTP can have a performance penalty for operations in which a response is not required (e.g., reporting events).
* The Stanford network is notoriously unreliable (especially at night); significant coding effort is required to account for this.

In addition, there are already places within SDR were we have re-invented a message broker and/or jerry-rigged around not having a message broker (e.g., polling via HTTP to determine if a long-running job has completed).

Introducing a message broker to support asynchronous communication where appropriate will allow decoupling of services, making SDR more resilient and scalable.

## Examples

Here are some specific examples of where a message broker could be introduced into the existing infrastructure.

### Event logging

Currently, various services log to the Event Service using HTTP calls. This makes each of these services dependent on the Event Service and requires that the service unnecessarily wait for the Event Service when logging an event.

Alternatively, each service could submit an event message (i.e., a message that describes the event to be logged) to the Message Broker. The Message Broker would add the message to an event queue. The Event Service could then subscribe to the event queue, logging an event for each event message.

With this approach, if the Event Service is offline or running slowly, other services are not affected.

### Workflow step processing

Currently, any service that want to process workflow steps has to have knowledge of the Workflow Service so that the workflow steps recorded by the Workflow Service can be updated as the step is started and completed. The Robots and DOR Services App interact with the Workflow Service in this way. (The situation is even worse with certain workflow steps, where the step is initiated in a robot, but completed in DOR Services App, with the robot making a call to DOR Services App to invoke the step.)

Alternatively, the Workflow Step could submit a job request message (i.e., a message that describes the job to be performed) to the Message Broker. The Message Broker would add the message to a job request topic queue, where the topic identifies the type of job (for example, "technical_metadata").

Multiple services can then subscribe to the queue, each filtering the topics that it can handle. For example, DOR Services App may select SDR ingest transfer messages. Upon receiving a message, the service would emit a job started message, perform the work, and then emit a job completed message. The Message Broker would add these message to a job status queue.

The Workflow Service could subscribe to the job status queue, updating the workflow steps for each job started or job completed message.

Imagine in the future, that a Technical Metadata Service is added. It could start handling messages with the technical metadata topic. This service would not need to have any knowledge of the Workflow Service.

Though there is not an immediate use, this also allows for the possibility of some other service requesting jobs, without it having to know what services will perform the jobs or the services that perform the jobs knowing about the new service.

With this approach, the binding between services is reduced.

## Considered Options

* Add a message broker (e.g., RabbitMQ).
* Leave as is.

Note: Some version of ActiveMQ is currently deployed in DLSS. This is not considered a viable option because ActiveMQ is legacy technology and tightly bound to Java.

## Decision Outcome

TBD.

### Positive Consequences

* Increased ability to scale number of services.
* Increased ability to scale under load.
* Increased resilience to service failures.
* Provide mechanism for notification of the completion of long-running jobs.

### Negative Consequences

* Message broker must be supported by Ops.
* Services become dependent on the Message Broker. (However, Message Brokers are typically designed to be depended on.)
* The evolution work to begin using the Message Broker.

## Technology selection

[RabbitMQ](https://www.rabbitmq.com/) is the recommended message broker implementation. RabbitMQ satisfies the following requirements:

* Support for multiple messaging patterns, in particular, direct, fanout, and topic.
* Support for message acknowledgments.
* Support for persistable message queues.
* Support for JSON messages.
* Ruby client available.
* Puppet deployment available.
* Docker image available.
* High availabability / clustering configuration available.
* Management UI provided.
* Excellent community / documentation.
* Widely deployed.
* And, of course: open source.
