# 3. Kafkarator API is focused around dedicated CRDs

Date: 2020-09-14

## Status

Accepted

See also [2. Combine topic creation and credentials management in same app](0002-combine-topic-creation-and-credentials-management-in-same-app.md)

## Context

When application developers wants to interact with Kafkarator, they need an API. We have previously been vague about how that API should look, should it be one CRD, multiple CRDs, piggyback on existing NAIS CRDs etc.

We need to make a decision, so that we can proceed with detailing how the API looks, and what can be expected from it. It is also needed so that we can actually start implementing Kafkarator in earnest.

From various discussions, we have a few findings that guide our decision:

- When doing NAIS deploy, it is possible for developers to supply multiple resources to be applied to the cluster
- We have two separate concerns that needs two separate configurations

## Decision

- We will define one new CRD object to configure topics and access to this
- App developers will create this in the cluster when deploying their application
- Kafkarator will watch this CRD and take needed actions
- App developers will add configuration to their Application resource listing kafka pools they need access to

## Consequences

### Risks and difficulties

Due to the way this will work, creation of topics and injection of credentials will become an async operation from deployment. This will probably mean that Kubernetes will spend a little more time before the deployment is up and running the first time a new set of credentials are needed.

### Benefits

- Kafkarator does not need to intercept deployment or try and interact with the application or Application resource directly.
- Kafkarator only needs to work with Kubernetes and Aiven APIs
