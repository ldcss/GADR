# 16. Pub/Sub implements Event sourcing

Date: 2020-09-21

## Status

Accepted

Implements [10. Event sourcing captures every change to business state](0010-event-sourcing-captures-every-change-to-business-state.md)

Implements [11. CQRS separates read and write responsibility](0011-cqrs-separates-read-and-write-responsibility.md)

Implemented by [18. Single writer for a topic](0018-single-writer-for-a-topic.md)

Implemented by [19. Single schema per topic](0019-single-schema-per-topic.md)

Implemented by [20. Topic messages have gobits](0020-topic-messages-have-gobits.md)

Implemented by [21. Messages are in JSON format](0021-messages-are-in-json-format.md)

Implemented by [22. Locations are specified in GeoJSON](0022-locations-are-specified-in-geojson.md)

Implemented by [23. ISO-8601 to specify date and time with timezone](0023-iso-8601-to-specify-date-and-time-with-timezone.md)

## Context

The sequence of events arising from the [event sourcing](0010-event-sourcing-captures-every-change-to-business-state.md) pattern has to be available to consumers. The pub/sub pattern seems to be a good mechanism to decouple publisher and subscriber, making them both as independant as possible from each other.

Functionality of the event handling mechanism is distribution of events and keeping a history of events that can be used for backloading and later analysis. Several implementations exist that could be applied on the platform. For example, Apache Kafka is a commonly used implementation. Google Cloud Pub/Sub is available as a managed service on the platform. Compared to other solutions, it provides less maintenance and better integration with other components on the platform. On the other hand, it does not provide message history and ordered, one-time delivery, both properties that would simplify implementation of event sourcing patterns. Acquiring a pub/sub implementation that has these properties would not be beneficial due to higher cost and implementation complexity.

Cloud Pub/Sub allows subscribers to publish their events, which makes them available to consumers. Distribution is either push, using HTTP methods, or pull, using the Pub/Sub APIs and client libraries. By offloading the messages to persistent storage (e.g. Cloud Storage or BigQuery), the history of events can be made available.

## Decision

We will use Google Cloud Pub/Sub topics to handle the events processed on the ODH.

## Consequences

### Advantages

* As a fully managed service, Pub/Sub is fitting the principles [serverless](0002-use-serverless-infra-components.md), [cloud native](0003-create-cloud-native-solutions.md), [software defined](0004-create-software-defined-everything.md).
* Other solutions are relatively costly compared to Cloud Pub/Sub.
* Pub/Sub integrates seemlessly into the platform and other services on it.

### Disadvantages

* Pub/Sub by default does not guarantee ordered delivery, and might deliver messages in a different order than received. This might require additional handling on the consumer side.
* Pub/Sub delivers a message at least once, but could in some situations redeliver a message. This might require additional handling on the consumer side.
* Pub/Sub has a limited storage period. Therefore, message history has to be managed seperately.
