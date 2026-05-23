# 2. Use SNS and SQS

Date: 2018-02-22

## Status

Proposed

## Context

eLife's internal software is deployed on AWS.

Low latency, short links between queues, publisher and consumers improve performance and security.

Consistent technologies are easier to manage at the infrastructure level.

There is a varying (sometimes small) load over the `bus`, which pushes for a service-based solution rather than running more servers.

## Decision

Use SNS topics and SQS queues subscribed to those topics for message delivery.

## Consequences

The `bus` current implementation is tied to AWS's proprietary APIs.

There are limits to what SQS can do, for example no exponential backoff in delivering messages.
