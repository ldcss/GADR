# Use RabbitMQ with MQTT plugin as message broker for devices so they can communicate with each other

* Status: Accepted
- Date: 2019-03-11
- Deciders:
    - achotard
    - blacroix
    - jmartinsanchez

## Context and Problem Statement

We want a message broker so the devices and other applications can communicate with the backend.

What broker and protocol should we use?

## Decision Drivers <!-- optional -->

- Applicability regarding IoT projects : low-resources clients, etc
- Possibility to use it to stream frames/images coming from cars cameras
- Ease of deployment on Kubernetes
- Existing knowledge of the team

## Considered Options

- [RabbitMQ](https://www.rabbitmq.com/), optionally with [MQTT plugin](https://www.rabbitmq.com/mqtt.html)
- [VerneMQ](https://vernemq.com/)
- Non-MQTT brokers
    - [Kafka](https://kafka.apache.org/)
    - [NATS](https://nats.io/)
    - [AWS Kinesis](https://aws.amazon.com/kinesis/)
    - [Google Cloud Pub/Sub](https://cloud.google.com/pubsub/)

## Decision Outcome

Chosen option: **[RabbitMQ](TODO) with [MQTT plugin](https://www.rabbitmq.com/mqtt.html)**, because:

- It is already well-known among the team
- It has some [existing "official" Helm chart](https://github.com/helm/charts/tree/master/stable/rabbitmq)
- It seems like a good fit to iterate fast

We **do not exclude switching to another MQTT broker such as VerneMQ in the future**, depending on our ability to dsitribute it cleanly on Kubernetes.

We also **do not exclude using another broker such as Kafka or NATS for appropriate use cases**.

## Pros and Cons of the Options <!-- optional -->

### RabbitMQ

Pros:

- Existing ["official" Helm chart](https://github.com/helm/charts/tree/master/stable/rabbitmq) ready to be deployed on Kubernetes
- Another ["official" Helm chart supporting High
  Availability](https://github.com/helm/charts/tree/master/stable/rabbitmq-ha/)
  RabbitMQ clusters on Kubernetes
- Official [MQTT plugin](https://www.rabbitmq.com/mqtt.html) supported in core distribution

Cons:

- Too obvious :D
- Doesn't scale as well as alternatives

### VerneMQ

Pros:

- Is the most performant MQTT broker out there
- Is known to be scalable
- Is pretty cool

Cons:

- No "official" Helm chart ready to be deployed on Kubernetes
- Not existing knowledge about it

### Non-MQTT brokers

Non-MQTT message brokers such as NATS, Kafka, AWS Kinesis and Google Cloud Pub/Sub were quickly put aside due to their lack of support for the MQTT protocol.

**Managed services** such as Kinesis or Pub/Sub are also eliminated because they would lock us with a given provider and we want to be able to host the entire XebiKart infrastructure anywhere (envisionning going multi-cloud). This is also the reason behind the lack of consideration for things such as **AWS IoT** or equivalent MQTT managed solutions.

**Kafka** didn't look like a good candidate for our use-case (also not supporting MQTT), as well as native NATS even if this one is the most ready to be distributed on Kubernetes. **We are still considering both for a later stage** when we will be deeper in the project and when we will be able to split brokers according to their usage.
