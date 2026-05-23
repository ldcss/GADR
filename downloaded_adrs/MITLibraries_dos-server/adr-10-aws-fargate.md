# AWS Fargate for Docker Container Deployment

## Context

Infrastructure is needed to run Docker containers (the current choice of deployment packaging). As we are apparently using Amazon Fargate for running containers of other applications, the Dockerized application 
can be deployed to Amazon Fargate (until a replacement choice for running Docker containers is made by 
the infrastructure team.

## Decision

Fargate platform will be used.

## Status

Accepted

## Consequences

If there are any unanticipated and unresolvable problems with the deployment mechanism, 
the deployment can be done to an alternative Docker environment, as 
determined by the infrastructure team.