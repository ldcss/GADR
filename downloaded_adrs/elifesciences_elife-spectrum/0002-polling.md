# 2. Polling is the preferred approach

Date: 2017-09-07

## Status

Accepted

## Context

Most of the operations triggered on the system under test are asynchronous and we do not have a clear way of understanding when they are completed, if they are at all. [Bare sleeps lead to test instability](https://martinfowler.com/articles/nonDeterminism.html#AsynchronousBehavior).

## Decision

Polling is the preferred approach to checks: it is minimally invasive for the system under test and promotes the creation of APIs to monitor the activities inside the different services.

Polling is not necessary where we are guaranteed consistent state by design. For example, after an article has been published on the elLife 2.0 API it should be immediately available on the public-facing website. 

## Consequences

Checks should rely on polling primitives and timeouts, giving up after the timeout if the state they expect hasn't manifested itself.

Checks should have a reasonable interval between polling calls, to avoid creating unnecessary load without an noticeable decrease in latency.

