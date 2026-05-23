# 4. replace file hosting with cloud storage

Date: 2017-07-06

## Status

Accepted

## Context

The container currently runs an nginx web server to host the output file for consuming applications.
If the container is not running, the file is not available.

## Decision

The nginx service will be removed and the `gp-data.json` file will be written to the team's preferred cloud hosting platform.

## Consequences

A `gp-data.json` file will be available in cloud storage for use by consuming applications.

Deployment simplified to a container running a single service.
