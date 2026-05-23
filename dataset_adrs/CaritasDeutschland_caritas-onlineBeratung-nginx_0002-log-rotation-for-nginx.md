# 2. Log rotation for nginx

Date: 2020-02-10

## Status

Accepted

## Context

We need a log rotation for the nginx webserver. As the nginx does not support log rotation out of the box, we need our own solution.

## Decision

We implement the log rotation using the programm logrotate inside the docker container for the nginx webserver. We do not trigger the log rotation from outside of the docker container, because we want a solution that is independed from the host system.

## Consequences

Logrotate isn't available in the official docker image for nginx. So we need to build our own docker image with lograte. The base of our docker image is the official docker image for nginx.
