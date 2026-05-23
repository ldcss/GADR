# 009 - Proxy Limiting

* Date: [2021/06/23 when the decision was last updated]
* Status: Proposed
* Deciders: Daniel Stefaniuk

## Context

In order to protect DoS services from being overloaded by too many capacity service api requests the proxy will throttle the numbers of requests per second that can be sent

## Decision

The proxy will throttle the api requests to 3 requests/sec with an allowed burst of 8 requests in a 10 minute period

## Consequences

Any requests that are throttled by the proxy will receive a 503 service unavailable error.
The DoS service will be protected from being overload due to unusually high numbers of capacity service api requests being sent.
