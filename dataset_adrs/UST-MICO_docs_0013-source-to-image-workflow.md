# Source-to-Image Workflow

Technical Story: [Evaluate Knative build](https://github.com/UST-MICO/mico/issues/49)

## Context and Problem Statement

We want to have a Source-to-Image workflow to import services based on a GitHub repository. It should run inside our Kubernetes cluster, however currently Kubernetes doesn't have a resource build-in that is able to build container images. Therefore another technology is required.

## Decision Drivers

* MUST run on our Kubernetes cluster
* MUST run completely in userspace (no root access required)
* MUST be sufficient to provide a single URL to a GitHub repository (with included Dockerfile)
* SHOULD be independent of any cloud service provider

## Considered Options

* Gitkube
* Google Cloud Build
* Azure Container Registry Tasks (ACR Tasks)
* OpenShift Source-to-Image (S2I)
* Knative Build

## Decision Outcome

Chosen option: *Knative Build*, because it meets all of our criterion decision drivers. It allows us to implement a Source-to-Image workflow on our Kubernetes cluster independently to any cloud service provider.

### Positive Consequences

* By using *Knative Build* we have the choice to use different kinds of `Builders`, follow-up decision is required: [Building OCI images](./0015-building-oci-images.md)

### Negative consequences

* *Nothing known*

## Pros and Cons of the Options

### Gitkube

[GitHub: Gitkube](https://github.com/hasura/gitkube)

* Good, because it is easy to use (only git and kubectl are required)
* Good, because it is designed to build and deploy images to Kubernetes
* Bad, because it uses Docker-in-Docker approach (see [Building OCI Images](./0015-building-oci-images.md))
* Bad, because it is build for a different purpose: Helping developers to trigger the build and deployment of an image by using `git push`

### Google Cloud Build

[Cloud Build documentation](https://cloud.google.com/cloud-build/docs/)

* Good, because it is easy to use, nothing has to be installed (only a call to the `Cloud Build API` is required)
* Good, because it is a managed service therefore it doesn't consume our own resources
* Good, because it allows us to use different `Builder` technologies (see [Building OCI Images](./0015-building-oci-images.md))
* Bad, because we depend on the continuity of a third-party service (Google Cloud Build)
* Bad, because it runs only on Google Cloud, that forces vendor lock-in
* Bad, because it leads to additional costs (first 120 builds-minutes per day are free, see [Pricing](https://cloud.google.com/cloud-build/pricing)

### Azure Container Registry Tasks (ACR Tasks)

[Tutorial: Automate container image builds with Azure Container Registry Tasks](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-tutorial-build-task)

* Good, because it is a managed service therefore it doesn't consume our own resources
* Good, because we already run on the Azure Cloud
* Bad, because it uses the Docker daemon internally, no other `Builders` can be used (see [Building OCI Images](./0015-building-oci-images.md))
* Bad, because there is no public API available, only usable with the Azure CLI
* Bad, because we depend on the continuity of a third-party service (ACR Tasks)
* Bad, because it runs only on Azure, that forces vendor lock-in
* Bad, because it leads to additional costs (100 minutes are included for free per month, see [Pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/#)

### OpenShift Source-to-Image (S2I)

[GitHub: Source-To-Image (S2I)](https://github.com/openshift/source-to-image)

* Good, because it is the way to go for creating a Source-to-Image workflow on a OpenShift cluster
* Bad, because it is designed for the OpenShift Container Platform (additional effort is required to use it on plain Kubernetes)
* Bad, because it uses the Docker daemon internally (in future *Buildah*), no other `Builders` can be used (see [Building OCI Images](./0015-building-oci-images.md))

### Knative Build

[GitHub: Knative Build](https://github.com/knative/build)

* Good, because it has the backing of industry giants (Google, Red Hat, IBM, SAP)
* Good, because it is designed for Kubernetes
* Good, because it provides a standard, portable, reusable, and performance optimized method for defining and running on-cluster container image builds
* Good, because it allows us to use different `Builder` technologies (see [Building OCI Images](./0015-building-oci-images.md))
* Good, because *Knative Build* consumes little resources (2 pods a ~11 MB).
* Bad, because it is still work-in-progress
