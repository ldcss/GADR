# 9. Use Cloud Init to build Prometheus Server

Date: 2018-08-15

## Status

Accepted

## Context

The Prometheus Server needs to be built in a reproducible way within AWS.
Reproducible in this context means that the server can be built, destroyed and rebuilt.
The rebuilt server will be identical to the original server and the is no external intervention required (i.e. logging into the server to make changes to configuration)

## Decision

Cloud init will be used to build a reproducible server.

## Consequences

The cloud init was chosen over other strategies such as creating a machine image because there is prior art for building a Prometheus server with cloud init and building machine images requires additional tools.
It was felt that cloud init will be the fastest way to achieve the short term goals.
The use of cloud init should be reviewed at the earliest opportunity.
