# Building OCI Images

Part of the Technical Story: [Evaluate Knative build](https://github.com/UST-MICO/mico/issues/49)</br>
Related to the [ADR-0013 Source-to-Image Workflow](./0013-source-to-image-workflow.md).

## Context and Problem Statement

We want to build OCI images based on Dockerfiles inside our Kubernetes cluster.

## Decision Drivers

* MUST run completely in userspace (no privileged rights required)
* MUST be runable on Kubernetes
* MUST be controlled in an automatic manner (CI/CD)
* SHOULD be compatible with Knative Build

## Considered Options

* Docker out of Docker
* Docker in Docker
* BuildKit
* img
* Jib
* Buildah
* Kaniko

## Decision Outcome

Chosen option: Kaniko, because it is designed for the use case we need. It works on Kubernetes and build OCI images without any daemon and without privileged rights.

## Pros and Cons of the Options

### Docker out of Docker

* Good, because Docker daemon is already running in the Kubernetes cluster
* Bad, because it would interfere the Kuberentes scheduling
* Bad, because it requires privileged mode in order to function, which is a significant security concern
* Bad, because it is not compatible with *Knative Build*

### Docker in Docker

* Good, because it is a well known approach
* Bad, because it requires privileged mode in order to function, which is a significant security concern (still better than [Docker out of Docker](#docker-out-of-docker))
* Bad, because it generally incurs a performance penalty and can be quite slow
* Bad, because it is not compatible with *Knative Build*

### BuildKit

[GitHub: BuildKit](https://github.com/moby/buildkit)

* Good, because it is created by Docker (Moby) as a "next generation `docker build`"
* Good, because it is already successfully used by the OpenFaaS Cloud
* Good, because it can run on Kubernetes without privileged rights
* Good, because an official *Knative Build Template* exists
* Bad, because it needs a deamon

### img

[GitHub: img](https://github.com/genuinetools/img)

* Good, same as *BuildKit* but daemonless
* Bad, because it needs a special Linux Capability ["RawProc](https://github.com/kubernetes/community/pull/1934/files) to create nested containers
* Bad, because currently no official *Knative Build Template* exists (nevertheless it could be created ourself)

### Jib

[GitHub: Jib](https://github.com/GoogleContainerTools/jib)

* Good, because it is fast and daemonless
* Good, because an official *Knative Build Template* exists
* Bad, because it is designed for Java applications only

### Buildah

[GitHub: Buildah](https://github.com/containers/buildah)

* Good, because it is a popular tool for creating OCI container images and maintained by Red Hat (also included by default in RHEL)
* Good, because it is daemonless
* Good, because an official *Knative Build Template* exists
* Bad, because it requires privileged rights (same as Docker daemon), rootless mode is planned

### Kaniko

[GitHub: kaniko](https://github.com/GoogleContainerTools/kaniko)

* Good, because it is a popular open source project created by Google
* Good, because it is well documented and easy to use (readymade executor image `gcr.io/kaniko-project/executor` exists)
* Good, because it is designed to work on Kubernetes
* Good, because it is daemonless
* Good, because it does not need privileged rights (however it requires to run as root inside the build container)
* Good, because an official *Knative Build Template* exists
* Bad, because there are security concerns about malicious Dockerfiles due to the lack of isolation [Issue #106](https://github.com/GoogleContainerTools/kaniko/issues/106)
