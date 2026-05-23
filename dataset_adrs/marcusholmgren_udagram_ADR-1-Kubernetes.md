# ADR1: Use Kubernetes
Date: 2021-02-13

## Status
Accepted

## Context
The API endpoints needs to be managed as a unit.
To allow for operational scaling the containerised application will be built to be able to run in Kubernetes.

## Decision
To help package the individual AWS resource into a serverless application we will use [Kubernetes](https://kubernetes.io) framework.

We also considered the following alternative solutions:
* Manual creation of resource from multiple terminal sessions
* Docker Compose

## Consequences
* We need to learn Kubernetes patterns and usage style