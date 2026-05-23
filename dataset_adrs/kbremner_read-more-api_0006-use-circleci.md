# 4. Use CircleCI

Date: 2017-09-24

## Status

Accepted

## Context

We want a mechanism that allows for the tests to be run whenever changes are made to the project.

We also want the project to be deployed whenever these tests pass.

CircleCI allows for builds to run in a Docker container based on a specified "root" image, with support for specifying additonal images for dependencies, i.e. database required for integration tests.

CircleCI provides open source projects with four free linux containers for running builds.

All of the configuration for a project built with CircleCI is stored in the project, except for environment variables.

Microsoft provides the "aspnetcore-build" Docker image, which contains all the dependencies required to build an ASP.NET Core application.

## Decision

We will use CircleCI to handle continuous integration builds and deployments.

## Consequences

There will be no cost associated with running CI builds and depoloyments.

Someone who is new to the project will be able to find the build, test and deployment steps in the configuration stored in the project. 

Pull requests will be built by CircleCI, allowing for verification that the tests pass before merging.