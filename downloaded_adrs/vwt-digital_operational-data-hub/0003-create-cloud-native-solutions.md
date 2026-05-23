# 3. Create cloud native solutions

Date: 2020-09-21

## Status

Accepted

Implemented by [56. Deploy on Google Cloud Platform](0056-deploy-on-google-cloud-platform.md)

## Context

Cloud-native architecture fully takes advantage of the [serverless computing](0002-use-serverless-infra-components.md) to maximise your focus on writing code, creating business value and keeping customers happy.

All the developer has to worry about is orchestrating all the infrastructure they need ([sofware defined](0004-create-software-defined-everything.md)) and the application code itself.

## Decision

We will build cloud-native solutions.

## Consequences

### Advantages

A modern cloud-native application supports DevOps processes, further enabling this automation and collaboration which was not possible in the era of local development and limited server-based software delivery processes.

Because of this design, even when failures happen you can easily isolate the impact of the incident so it doesn’t take down the entire application. Instead of servers and monolithic applications, a cloud-native architecture helps you achieve higher uptime and thus further improve the user experience.

### Disadvantages

Potential vendor lock-in due to cloud provider specific functionality that is not easily portable to other cloud providers.

A cloud-native solution often involves many cloud components interacting together. To maximise the benefits of the cloud-native architecture, these components should be loosely coupled resulting in a maintainable solution. A poor design will lead to low reliability and bad maintainability.

