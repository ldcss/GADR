# 3. Use `RawMessageDelivery`

Date: 2018-02-22

## Status

Proposed

## Context

SNS is a service originally designed for notifications (e.g. smartphone push notifications) rather as a message queue. Its configuration needs to be tuned for our use case.

It's important to keep the channel as easy to use as possible, without additional complications.

## Decision

Use [RawMessageDelivery](https://docs.aws.amazon.com/sns/latest/dg/large-payload-raw-message.html) on all SQS-to-SNS subscriptions.

## Consequences

The content of a message published to a topic should be exactly identical to what comes out from a subscribed queue, with no wrapping, encoding or attached metadata.
