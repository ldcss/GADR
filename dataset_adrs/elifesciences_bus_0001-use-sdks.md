# 1. Use internal SDKs to access the bus

Date: 2018-02-22

## Status

Proposed

## Context

Multiple projects need to publish or subscribe to messages from the `bus`.

Projects are written in a fixed set of supported programming languages.

There is a set of non-functional requirements to cater for in integrations, especially when listening to queues (retries, graceful shutdown, timeouts, etc).

## Decision

Access the bus exclusively through the eLife SDKs, either for publishing or subscribing to messages:

- [bus-sdk-php](https://github.com/elifesciences/bus-sdk-php)
- [bus-sdk-python](https://github.com/elifesciences/bus-sdk-python)

## Consequences

The AWS PHP SDK or Boto's SQS and SNS support should not be used directly for the purpose of accessing the `bus`.

SDKs and other generic tooling can be used by infrastructure automation tools to setup the `bus` topics and queues.
