# Use ExternalDNS to manage DNS records

- Status: Accepted
- Date: 2019-04-10
- Deciders:
    - achotard
    - ADD YOURSELF HERE. This line will be removed before merging the PR.

## Context and Problem Statement

We are deploying **Kubernetes Services** of type `LoadBalancer` in order to
expose services such as RabbitMQ. This creates a Google Cloud Network Load
Balancer on GCP, with the associated public IP address.

In order to **connect to services using a name** and not a raw IP address, we
need to be able to **create DNS records** automatically and in a clean way,
pointing on these GCLB.

## Decision Drivers <!-- optional -->

- Ease of use for developers writing their Kubernetes manifests to expose
  Services
- Ability to plug on Google CloudDNS and potentially other providers
- Must be dynamic

## Considered Options

- [Terraform](#terraform)
- [ExternalDNS](#externaldns)
- [Mate](#mate)

## Decision Outcome

Chosen option: **"ExternalDNS"**, because:

- Is directly uses **annotations** on Kubernetes Services and Ingress to know
  what records to add and to which IP they should point. Therefore, it enable
  people to define their own records in their K8s manifests **without having to
  define anything in another repo**.
- It is maintained, wealthy and keeps growing
- It is clean and answer our need perfectly

However, we still didn't test it for Ingresses.

## Pros and Cons of the Options

### Terraform

Since [Terraform](https://www.terraform.io/) has a [Google CloudDNS record set
module](https://www.terraform.io/docs/providers/google/r/dns_record_set.html),
we are able to create these records using Terraform.

Pros:

- No new tool in the stack

Cons:

- The configuration would not be dynamic. We would have to track Services GCLB
  IPs manually and create corresponding records in Terraform. **This is a huge
  deal breaker**.

### ExternalDNS

[ExternalDNS](https://github.com/xebia-france/xebikart-infra/pull/13) allows
configuring external DNS servers (AWS Route53, Google CloudDNS and others) for
Kubernetes Ingresses and Services.

Pros:

- The _Google CloudDNS_ provider of ExternalDMS is considered _Stable_ (it's
  actually the only one beside AWS Route53)
- ExternalDNS is wealthy among the community: lots of updates, was part of
  Kubernetes Incubator before it (the Kubernetes Incubator) was stopped.

Cons:

- None?

### Mate


[Mate](https://github.com/linki/mate) is also made to manage AWS Route53 and
Google CloudDNS records for Kubernetes services and ingresses. It was part of
[the Zalando incubator](https://github.com/zalando-incubator/)

Pros:

- Mate was the premice of dynamic Cloud providers DNS configuration from
  Kubernetes objects

Cons:

- mate is now deprecated...
