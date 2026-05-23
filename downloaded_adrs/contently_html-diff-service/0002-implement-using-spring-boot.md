# 2. Implement using Spring Boot

Date: 2018-10-23

## Status

Accepted

## Context

The HTML Diff Service is born out of need to increase performance of HTML
diffing by not requiring a command line execution in Contently's web
application. Additionally, we wanted to remove the Java dependency from our
Rails application container to simplify and reduce the threat surface.

## Decision

Spring Boot is used to allow for the service to be standalone with support for
embedded servers. The decision allows portability to deploy the service without
a J2EE server.

## Consequences

Using Spring Boot allows us to "dockerize" the service and deploy it within a
Kubernetes cluster.

A serverless implementation (i.e. AWS Lambda) was considered and tested, but
ultimately abandoned given the slow startup of a Java process and low usage of
this service.
