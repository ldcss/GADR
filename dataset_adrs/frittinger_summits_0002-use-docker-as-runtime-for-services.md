# 2. Use Docker as runtime for services

Date: 2019-11-01

## Status

Accepted

## Context

We want a generic runtime that let's us deploy the services a uniform way in various environments like AWS, Azure, Kubernetes or locally.
Docker is the de-facto standard today and is the system used by us for all projects.

## Decision

Use docker to deploy all services.

## Consequences

For local development docker might be an overhead but the benefits of a generic runtime outweigths that.

To overcome that problem, we can use docker-compose locally or run the docker containers individually.

As a benefit, this platform can help us to test minikube!

