# 5. Use docker for applications

Date: 2018-06-07

## Status

Accepted

## Context

During the build of the Data Submission Service, we need to build and deploy
the applications and their dependencies in a repeatable manner. We also need
the ability to develop and run the applications locally.

There are a number of approaches to managing this including configuring a
combination of configuration management and virtualisation tools (like puppet
and chef combined with vagrant).

Ideally, we'd like to separate running the application from the server operating
system, so we can make use of Platform as a Service type hosting options. This
suggests that containerisation using a tool like Docker would be useful.

Containerisation is a well understood approach for doing this, and is well
supported in all the major cloud providers - with many providing dedicated
container services.

## Decision

We will use Docker to package applications so that they can be deployed.

We will look to use a Platform as a Service offering for deploying the Docker
containers.

## Consequences

We will use a build process that will output docker images.

We will use a deploy process that deploys docker to a Platform as a Service
hosting offering.
