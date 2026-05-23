# Use OpenShift as cloud Provider

## Context and Problem Statement

We want to deploy our application in docker containers that can be easily updated 

## Considered Options

* [Docker Swarm](https://docs.docker.com/engine/swarm/) Orchestration tools provided by docker
* [Kubernetes](https://kubernetes.io/) – Orchestration tools provided by ex google teams
* [OpenShift](https://www.openshift.com/) – RedHats Orchestration tools that is build on Kubernetes that provides extra tools on CI/CD 

## Decision Outcome

Chosen option: "OpenShift", because

* Built on Kubernetes.
  The bank has experience on it. 
  Provides a lot of added value tools for CI/CD, automated builds.
  Is supported by RedHat and we have a great support contract for it.
  