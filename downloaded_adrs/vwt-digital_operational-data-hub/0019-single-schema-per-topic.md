# 19. Single schema per topic

Date: 2020-09-21
Update: 2021-07-21

## Status

Accepted

Implements [16. Pub/Sub implements Event sourcing](0016-pub-sub-implements-event-sourcing.md)
Implements [21. Messages are in JSON format](0021-messages-are-in-json-format.md)

## Context

A schema is a vocabulary that allows you to annotate and validate documents. Every topic has a schema that can validate the messages the topic receives.

## Decision

Since every topic only receives messages in JSON format (see [21. Messages are in JSON format](0021-messages-are-in-json-format.md) ), we define a JSON Schema for every topic that can validate the messages received by said topic.
If a JSON schema contains an object with a primary key, the field `primary_key` should be added at the same depth as the `required` field. This is not an official JSON schema field.

## Consequences

Every message received by a topic can be validated against a schema. This way, if a message is not conform the schema, the developer knows something is amiss.

## References

* https://json-schema.org/, retrieved 6 October 2020
