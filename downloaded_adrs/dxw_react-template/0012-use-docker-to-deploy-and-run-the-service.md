# 12. Use Docker to deploy and run the service

Date: 2019-10-18

## Status

Accepted

## Context

We want to be able to easily deploy to a known, stable environment when
deploying the service. Docker allows us to package our environment up and make
it reproducible and require changes to be intentional. It is well supported by
all major cloud platforms.

There are benefits to also using Docker for local development, such as ensuring
we build the service in the same environment as we run it. However, running
Docker creates overheads and complexity that slow down development.

## Decision

We will use Docker to build and run the service. At this stage, we won't use it
for local development.

## Consequences

With Docker, we can be confident about what environment we're deploying, and
manage it as code.
