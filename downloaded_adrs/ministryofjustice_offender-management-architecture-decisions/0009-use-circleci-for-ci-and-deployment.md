# 9. Use CircleCI for CI and deployment

Date: 2018-11-16

## Status

Accepted

## Context

We need to choose tooling for various continuous integration and deployment
tasks:

- running automated tests on branches/pull requests
- running security and code quality checks on branches/pull requests
- building Docker images
- deploying applications to our environments

Jenkins and CircleCI are commonly used at MOJ for these tasks, and the team
have experience with both of them, as well as other options such as Travis.

The Cloud Platform team operate a Jenkins server but are keen to move services
away from it, especially anything which doesn't use Template Deploy.

The LAA fee calculator is built and deployed using CircleCI with the new cloud
platform, so we'd have an example to follow if we also chose CircleCI. That
team didn't evaluate a lot of options when they made that decision, but it's
working well so far for them. Our applications are a little more complex than
theirs since we have a database, but we don't expect to be doing anything
unusual in our build and deploy pipelines.

There's also some [documentation](https://ministryofjustice.github.io/cloud-platform-user-docs/02-deploying-an-app/004-use-circleci-to-upgrade-app/)
on using CircleCI with Helm for continuous deployment to the new cloud
platform - we may not want to follow it exactly, but it covers some useful
topics.

Our team haven't been practising continuous deployment (that is, deploying
every change automatically to production) on Visit someone in prison - deploys
to production for that service need to be triggered by a human. We'd like to
keep that option open for this service, though.

It's important to us that our build and deployment configuration is managed in
code. We've decided to start out with two applications (see [ADR 0004](0004-separate-api-and-user-facing-applications.md))
and want to be able to easily make and reproduce changes to builds and
deployments for both.

We're keen to get started quickly - we'd rather not spend time assessing lots
of tooling options at this stage. Our needs will evolve anyway, so it's fine
to pick something that works for us now and revisit that decision later on if
we need to.

## Decision

We will use CircleCI for continuous integration.

We will use CircleCI for deploying.

## Consequences

Our applications are in public repositories, so we can use some free containers
to build them.

That means that our builds are public too, though, so we need to be careful to
not expose any secrets in our build output.
