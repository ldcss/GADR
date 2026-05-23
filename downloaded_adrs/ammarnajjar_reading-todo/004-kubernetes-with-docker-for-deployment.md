# Kubernetes with Docker for Deployment

Date: Thu Sep 19 22:08:13 CEST 2019

## Milestone

0.1.0

## Context

For the project a deployment and development mechanism is need to be chosen and adopted.

## Decision

- [Kubernetes](https://kubernetes.io/) will be the deployment technology of choice.

The project will be deployed into a kubernetes cluster using [helm](https://helm.sh/).

- [Docker](https://www.docker.com/) will be the container building technology of choice.

Every thing will be directed through docker containers, from development to deployment. CI Pipeline will run inside a docker container as well.

## Consequences

### Kubernetes

Why:

- Open source
- Free
- Service discovery and load balancing
- Storage orchestration
- Automated rollouts and rollbacks
- Automatic bin packing
- Self-healing
- Secret and configuration management
- Available for many operating systems.
- Widely used and well documented, so finding help is no issue.
- Docker support.

Why not:

- A bit complicated to setup.
- Resources hungry.
- Not as good as [docker-swarm](https://docs.docker.com/engine/swarm/) when it comes to performance.

### Docker

Why:

- Available for many operating systems.
- Supported by Kubernetes

Why not:

- Resources hungry.
- A daemon must be running at all times in the background.

## References (optional)

- [Kubernetes](https://kubernetes.io/)
- [Docker](https://www.docker.com/)
- [helm](https://helm.sh/)
- [docker-swarm](https://docs.docker.com/engine/swarm/)
