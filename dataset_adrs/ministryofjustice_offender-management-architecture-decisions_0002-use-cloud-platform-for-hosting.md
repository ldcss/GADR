# 2. Use Cloud Platform for hosting

Date: 2018-10-12

## Status

Accepted

## Context

The team are familiar with the [Template Deploy](https://github.com/ministryofjustice/template-deploy)
stack from their work on Visit someone in prison. This approach was developed
several years ago as a temporary solution, but it doesn't meet our needs for
many reasons, including:

- It defines the initial state of the stack, but does not reliably manage the
  state of resources after that, so manual changes can be made to those
  resources which are not easily visible or managed in code.
- It's expensive to run: each application has multiple dedicated EC2 instances,
  which typically run at very low load.
- Deploys for some applications take 10-15 minutes, and if they're cancelled
  the stack is left in an inconsistent state.
- The monitoring configuration isn't specific to each application, and the
  standard alert limits aren't appropriate for everything.
- Few people understand how it works.

The Cloud Platform team are working on a new
[Kubernetes-based hosting platform](https://ministryofjustice.github.io/cloud-platform-user-docs/#cloud-platform-user-guide),
to replace Template Deploy. The LAA fee calculator is already live on that
platform, and other teams are using it for development and pre-live services.
This platform is MOJ D&T's strategic hosting choice.

The Sheffield ops team also run services built in the Digital Studio on AWS and
Azure, including some in related areas to our work such as New NOMIS, Keyworker
and Licences. There is an intent to move those applications to the new Cloud
Platform. Our team aren't familiar with those stacks.

## Decision

We will use the Cloud Platform for hosting our applications.

## Consequences

We need to learn about Kubernetes.

We need to work closely with the Cloud Platform team and other users of the
platform to resolve issues and make informed choices about our approach.

The supporting services for centralised logging, monitoring and alerting which
are provided as part of the Cloud Platform are good default options to start
with, so we don't need to make separate decisions about those areas right now.

This experience of using the new platform will help the team when we come to
migrate Visit someone in prison to it as well.
