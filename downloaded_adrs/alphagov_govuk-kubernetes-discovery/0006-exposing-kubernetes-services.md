# 6. Exposing Kubernetes Services

Date: 2017-06-16

## Status

Accepted

## Context

Kubernetes services can be exposed to the public using Kubernetes managed resources
that can integrate with Cloud environments, such as the Loadbalancer service resource,
or with Cloud native services, such as AWS ELBs.

Which solution to use will affect how we manage associated resources and processes, for
instance EIPs and DNSs, HTTPS certificates, green-blue deployments, etc.

Initially we want to find a solution that meets some basic requirements:
- HTTP and HTTPS support
- Internal-only and Internet facing services
- Probably we want to route traffic to services based on request URI

## Decision

Initially we tested a Loadbalancer Kubernetes service on AWS. This service configures a
classic ELB that connects with the pod service port. It requires uses Kubernetes secrets
to read the HTTPS certificate but doesn't support request URI routing. It also needs a
fixed public IP to start the ELB and a DNS entry managed externally.

Kubernetes Ingress resources allow us to define rules to route traffic to Kubernetes
services. Google Cloud has native support for Ingress resources, but on AWS we need to deploy
a controller service. On non-cloud environments (for instance, a local Minikube VM),
it is also possible to deploy a Ingress controller that can replicate the behaviour
expected in the cloud. The catalogue of Ingress controllers can be found here:

https://github.com/kubernetes/ingress/blob/master/docs/catalog.md

We tested Traefik and CoreOS ALB Ingress controller and finally decided to use the CoreOS
solution:
- Traefik feedback?
- CoreOS ALB ingress controller https://github.com/coreos/alb-ingress-controller
  - AWS managed certificates, with AWS Certificate Manager
  - Uses AWS ALB loadbalancers
  - Adds Route53 entries
  - Can optionally access services only on specific namespaces

We decided to use the CoreOS ALB controller because it uses AWS native solutions that meet our requirements.
Also, it's supported by CoreOS.

Other links and discussions about loadbalancer support for Kubernetes on cloud platforms:
- http://www.sandtable.com/a-single-aws-elastic-load-balancer-for-several-kubernetes-services-using-kubernetes-ingress/
- Kubernetes discussion around Ingress/AWS LBs support: https://github.com/kubernetes/kubernetes/issues/30518
- Internal ELB, useful for services that don't need to be open to the Internet: https://github.com/kubernetes/kops/issues/2011
- ELB and HTTPS: https://github.com/kubernetes/kubernetes/issues/22854
- Traefik working branch: https://github.com/alphagov/govuk-hosting-discovery/compare/traefik-ingress

## Consequences

AWS Certificate Manager is not supported by Terraform yet :( , so we'll have to add some tooling
or documentation to manage certificates. Because this is a solution integrated only with AWS,
we'll need to investigate other solution if we want to use ingress resources on a local environment.

