# 1. environments

Date: 2018-04-16

## Status

Accepted

## Context

We want to have separate environments for running our software at different stages of release.
This will be used to provide a location where changes can be tested without impacting
production work and our users.

## Decision

We have decided to have N+2 separate environments: development,
staging and production. In development, we can create as many separate
stacks as we want. The staging environment will be where the tools
team will test their changes. The production environment will run all
of our users monitoring and metrics and poll each of their
environments.

Any code can be deployed to development environments.  Only code on
the `master` branch can be deployed to staging and production.

## Consequences

Keeping the environments separate reduces the chance of a core change impacting
our users and will allow us to test aspects of our system such as handling load,
fail over testing and new, possibly behaviour changing, version upgrades. Users will
test their prometheus related changes in our production environment and will not have access
to the staging environment.
