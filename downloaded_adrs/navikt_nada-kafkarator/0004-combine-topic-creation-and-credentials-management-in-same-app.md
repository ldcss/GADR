# 4. Combine topic creation and credentials management in same app

Date: 2020-02-27

## Status

Accepted

Followup [6. Kafkarator API is focused around dedicated CRDs](0006-kafkarator-api-is-focused-around-dedicated-crds.md)

## Context

The project requires dealing with two relatively separate concerns:

1. Create topics when needed
2. Supply credentials for working with topics.

If we were to strictly follow the Single Responsibility Principle, these should be in separate apps.
However, the two concerns are conceptually quite connected, even if they are separate in implementation,
so it makes sense to keep them in the same application.

## Decision

We will ignore the SRP in this instance, and keep the two concerns in the same application.

## Consequences

We will only have to create and deploy one application to manage kafka topics. On the other hand,
our application could become more complicated as it needs to deal with two separate concerns.
We need to keep an eye on this complexity and make sure to split the application if needed.

