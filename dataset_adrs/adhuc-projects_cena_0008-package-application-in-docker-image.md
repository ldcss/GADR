# 8. Run application with Docker

Date: 2018-12-29

## Status

Accepted

## Context

`menu-generation` application is packaged as a [Spring Boot](0005-use-spring-framework.md) executable JAR file.

Running acceptance tests on development machine or during Continuous Integration must be quick, easy and the least
dependent of the underlying system.

[Docker](https://www.docker.com/) is a widespread container based solution that can be used during development lifecycle
on most operating systems as well as in well established Cloud solutions such as [Kubernetes](https://kubernetes.io/).

## Decision

`menu-generation` application will be packaged as a docker image. A `docker-compose` definition will also be provided
to help running the application and its dependencies in a consistent and isolated environment.

## Consequences

Running the application won't depend on the underlying system. It will only require a `docker` install and a `Make`
target to run it. Those prerequisites must be documented in the application's repository.

Acceptance tests execution will be based on a dedicated `docker-compose` environment to enforce execution isolation.

Upgrading the required components to run the application, such as Java version, will consist on adapting the base image
used to build the application image.

The application will be able to run in a Cloud environment.
