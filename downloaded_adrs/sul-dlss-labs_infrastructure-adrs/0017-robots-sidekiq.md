---
layout: default
title: ADR-0017
nav_order: 20
permalink: records/0017/
---
# Consolidate robots and replace Resque with Sidekiq

* Status: accepted
* Decider(s): <!-- required -->
  * Vivian Wong
  * Andrew Berger
  * Infrastructure Team
* Date(s): <!-- required -->
  * Status (from above): 2023-02-01

## Context and Problem Statement <!-- required -->

Content processing jobs are currently performed on a bespoke robot framework based on Resque. This approach is sufficiently performant and reliable, but is difficult to maintain because:

* It is not a standard job processing framework.
* Robots are the only remaining Resque implementation in the Infra portfolio. (All others use Sidekiq.)
* Only a subset of the Infra team has detailed knowledge of and experience with Resque.

In addition, the robot framework does not support job retriability, a strategy used in our other applications that has successfully reduced the need for manual remediation of failures.

The long-term viability of Resque is also unclear. It has gone through periods of dormancy, though it is currently being sparsely maintained. (See [this issue](https://github.com/resque/resque/issues/1759)).

Robots are currently spread across multiple repositories (common accessioning, preservation robots, web archiving robots, GIS robots, and lybercore). This isolation has led to inconsistent / messy coding practices. It also makes it more difficult to understand the overall structure of the framework.

This is separate from, but related to the desire to replace the workflow logic engine (currently implemented by the Workflow Server Rails application). Simplifying the robots would make such a replacement more tractable in the future, without precluding any of the possible approaches.

## Decision Drivers <!-- optional -->

* Continued performance and scalability
* Maintability
* Implementation resources

## Additional notes

A proof-of-concept has been successfully completed that runs common accessioning and preservation robots with Sidekiq.

## Considered Options <!-- required -->

Code consolidation:

* Consolidate robots into a single repository.
* Leave code in existing repositories.

Job processing framework:

* Replace Resque with Sidekiq
* Continue using existing Resque-based framework
* Replace Resque with a message broker (e.g., RabbitMQ)

## Decision Outcome <!-- required -->

Original proposed decision: consolidate robots into a single repository and replace Resque with Sidekiq.
Consensus proposed decision: leave robots in existing repositories (either improve lybercore or inline common code) and replace Resque with Sidekiq.

## Pros and Cons of the Options <!-- optional -->

### Code consolidation: Consolidate robots into a single repository

Note that robot servers would be configured to only use a subset of robots (via queue configuration) like current architecture.

* Pro: De-spaghetti-ing of robot codebases. This would allow more consistent coding practices and overall code clarity.
* Pro: Less maintenance. There will only be a single repository to be updated instead of 5.
* Pro: Reduce duplicate code. Even though much of common functionality is encapsulated in lybercore, there is still some duplication across the codebases.
* Con: Makes Capistrano deployment more complicated, as either need to deploy all robot workers or find a mechanism for partial deployment.

### Code consolidation: Leave code in existing repositories

* Pro: Less short-term risk from changing code.
* Pro: Does not require any resources for implementation.
* Pro: Keeping the code in separate repositories make the deployment dependencies (mounts, libraries) clearer.

### Job processing framework: Replace Resque with Sidekiq

* Pro: Sidekiq is actively maintained, with commercial support options.
* Pro: Supporting only a single job processing framework across all SDR applications reduces complexity.
* Pro: Reduces dependence on small number of team members that understand the existing framework.
* Pro: Easily allows for introducing retries to reduce manual remediation.

### Job processing framework: Continue using existing Resque-based framework

* Pro: Less short-term risk from changing frameworks.
* Pro: It is known reliable for this task.
* Pro: Does not require any resources for implementation.
* Con: The long-term viability of Resque is murky.

### Job processing framework: Replace Resque with a message broker

* Pro: RabbitMQ is actively maintained, with commercial support options.
* Pro: Allows robots to be constructed in languages other than Ruby.
* Pro: If deployed correctly, highly reliable and scalable.
* Con: RabbitMQ is complex, especially when scaling. Our RabbitMQ knowledge is limited.
* Con: Lose some of the features that come with Sidekiq, e.g., retriability.

## Links <!-- optional -->

* [ADR-0010](0010-message-broker.md) - Use message broker for asynchronous messaging
