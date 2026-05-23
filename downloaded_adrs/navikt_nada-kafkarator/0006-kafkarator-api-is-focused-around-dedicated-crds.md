# 6. Kafkarator API is focused around dedicated CRDs

Date: 2020-05-05

## Status

Accepted

See also [4. Combine topic creation and credentials management in same app](0004-combine-topic-creation-and-credentials-management-in-same-app.md)

Updated by [8. User experience](0008-user-experience.md)

## Context

When application developers wants to interact with Kafkarator, they need an API. We have previously been vague about how that API should look, should it be one CRD, multiple CRDs, piggyback on existing NAIS CRDs etc.

We need to make a decicion, so that we can proceed with detailing how the API looks, and what can be expected from it. It is also needed so that we can actually start implementing Kafkarator in earnest.

From various discussions, we have a few findings that guide our decision:

- Piggybacking on the existing NAIS CRDs are not encouraged and should be avoided
- When doing NAIS deploy, it is possible for developers to supply multiple resources to be applied to the cluster
- We have two separate concerns that needs two separate configurations

## Decision

- We will define two new CRD objects (see github issues #3 and #12)
- App developers will create these in the cluster when deploying their application
- Kafkarator will watch these two CRDs and take needed actions

## Consequences

### Risks and difficulties

Due to the way this will work, creation of topics and injection of credentials will become an async operation from deployment. This will probably mean that unless the application retries reading its secrets, it will fail the first time it is deployed.

### Benefits

- Kafkarator does not need to intercept deployment or try and interact with the application or Application resource directly.
- Kafkarator only needs to work with Kubernetes and Aiven APIs
