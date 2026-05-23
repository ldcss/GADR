# 3. Use EKS Cluster as Default Container Platform

Date: 2021-06-07
Scope: Web SRE Team

## Status

Accepted

## Context

There are quite a few options when choosing a platform and infrastructure patterns for managing applications. Across Mozilla teams, services & applications are already overwhelmingly containerized using Docker. We can deploy these containerized applications onto a number of options, including but not limited to multiple Kubernetes services or self-hosted routes.

## Decision

* We will support Dockerized applications primarily, with some flexibility given to application components that greatly benefit from serverless architectures.
* Dockerized applications are deployed to Kubernetes, defaulting to a Web SRE shared applications clusters if not requiring their own Kubernetes cluster.
* We will use AWS' Elastic Kubernetes Service to manage our Kubernetes clusters, unless there is a documented reason for a particular project not to.
* We will deploy our EKS clusters using Terraform & our internal Terraform module, unless there is a documented reason for a particular project not to.
* Any divergences from the above decisions must be clearly documented in the project's or application's service documentation.

## Consequences

* Reduces complexity of setting up our own infrastructure, or context switching between multiple container platform infrastructures.
* Incurs EKS costs.
* Will require migrations from old setups (Kops, External-terraform EKS module).
* EKS access model should improve our security posture and ease of access.
    * Users must have SSO access to get to a cluster, so employees exitng limits access more reliably than previous k8s models.
    * Having the correct AWS permissions allows you to create the k8s credentials needed to interact with the cluster, so we no longer have to pass a secret file around between people.

## Resources

* Web SRE EKS Cluster Terraform module: https://github.com/mozilla-it/terraform-modules/tree/master/aws/eks
