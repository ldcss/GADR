# 0002. ORID

Date: 2020-JUL-31

## Status

Accepted

## Decision

All services shall emit and consume, where applicable, a ORID. ORID shall conform to the [specification version 1](https://github.com/MadDonkeySoftware/OridNode/blob/master/docs/v1.md) where the custom fields are as follows:

| field    | mapping   | sample value |
|----------|-----------|--------------|
| custom-1 | N/A       |              |
| custom-2 | N/A       |              |
| custom-3 | accountId | 123          |

## Context

The issue motivating this decision, and any context that influences or constrains the decision.

As the mdsCloud ecosystem expands it can no longer be assumed that consumers of the service know internal APIs to issue commands. For example the current state machine implementation has a Task definition where the attribute "Resource" is a URL to invoke the function. The internal IP addresses and ports should not be known to consumers of the service as it needlessly tightly couples the system. This is compounded by operational concerns where an operator may need to "shuffle" or reconfigure systems during maintenance operations.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.

Moving to an ORID supported system will allow for many of these concerns to be mitigated.