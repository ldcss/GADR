# 1. Use commits as tags for images

Date: 2018-02-05

## Status

Accepted

## Context

Traceability of a Docker image to a source code repository is valuable to debug any problem that comes up during testing and deployment.

Dependency pinning on project images pinning a particular version of the base image they are using is also valuable for build reproducibility.

## Decision

We will tag every new, tested version of an image using the commit SHA value that produced it.

## Consequences

Any node will be able to deploy a new image version by specifying the commit SHA.

Project images will be able to pin a version of the base image they are using with a single line.

Dependency update builds will be able to propose an upgrade by changing the SHA value in a pull request.
