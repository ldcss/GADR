# Use kubectl and Helm for Kubernetes deployment

- Status: Accepted
- Date: 2019-03-17
- Deciders:
    - achotard
    - jmartinsanchez
    - ocloirec

## Context and Problem Statement

We want to **deploy** pods, services, and other resources on **Kubernetes**,
which is a GKE cluster for now.

What tool should we use to do this?

## Decision Drivers

- Ease of use
- How "far" is the tool from the Kubernetes lifecycle? - _"Is it trailing
  after upstream and if so, how far away from it"_
- Ability to express deployments in a descriptive "as-code" way
- Ease of use in a CI/CD pipeline - _Does it require a local state? Weird
  requirements? Auth to other systems?_
- Reliability - _"Will the tool usage often lead to messed up
  services/cluster?"_

## Considered Options

- [Terraform](#terraform)
- [Ansible](#ansible)
- [Kubectl](#kubectl)
- [Helm](#helm)

## Decision Outcome

Chosen option: "A mix of **kubectl** and **Helm**", because:

- `kubectl` is the native way of deploying to Kubernetes and it thus the most
  documented, widely-used, appropriate and up-to-date.
- Helm fits best for complex stacks deployment and we're eager to try things
  such as Helm charts repositories!

Helm will be used as an alternative to `kubectl` in a second part, when we'll
ramp up things and when we will need to deploy more complex stacks. The
beginning will be `kubectl` for our own services, and Helm for
components/middleware/databases with existing charts such as RabbitMQ!

This imply that the provided Kubernetes cluster(s) for this project will need
to be **provisionned with Helm requirements such as Tiller**.

## Pros and Cons of the Options

### Terraform

[Terraform](https://www.terraform.io/) is an infrastructure-as-code tool
developed by [Hashicorp](https://www.hashicorp.com/) that has support for a
[Kubernetes
provider](https://www.terraform.io/docs/providers/kubernetes/index.html).

Pros:

- Already used to spawn the underlying infrastructure on GCP (Projects, GKE
  cluster, etc)

Cons:

- Is yet another format overlay to describe Kubernetes resources
- Requires useless state synchronization

### Ansible

[Ansible](https://www.ansible.com/) and its [Kubernetes
modules](https://docs.ansible.com/ansible/latest/modules/kubernetes_module.html)
were a **No-GO** from the beginning since we're trying to avoid using Ansible
for unappropriate use cases such as this one.  Talking to APIs such as the
Kubernetes one is definitely not the job for which Ansible was made for.

### Kubectl

[`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/) is the
official command line tool to talk to the Kubernetes API.

Pros:

- Official tooling
- The GCP `gcloud` CLI allow easy authentication of `kubectl` to the Kubernetes
  API thanks to the `gcloud container clusters get-credentials  <cluster_name>
  --region <cluster_region>` command.

Cons:

- May be a bit harsh to deploy more complex stacks, and thus lead to CD
  pipelines with many many steps

### Helm

[Helm](https://helm.sh/) is _"the package manager for Kubernetes"_. It can be
seen as a way to package Kubernetes manifests and template them in order to
"bundle" complete descriptions. It uses what are called [_**Helm
charts**_](https://helm.sh/docs/glossary/#chart) to describe these bundles, and
these Helm charts can then be deployed on Kubernetes with `helm install`. Helm
requires a component called [`Tiller`](https://helm.sh/docs/glossary/#tiller)
to be installed on the Kubernetes cluster.

Pros:

- Community-agreed tooling with a widespread use
- Existing Helm charts for many open source software such as RabbitMQ which we
  are planning to use (see
  [`rabbitmq`](https://github.com/helm/charts/tree/master/stable/rabbitmq) and
  [`rabbitmq-ha`](https://github.com/helm/charts/tree/master/stable/rabbitmq-ha)
  **stable** Helm charts)
- Better revision & lifecycle handling than raw `kubectl`

Cons:

- Has some painful limitation according to some feedback we got
- Need to setup Tiller on the K8s clusters
- Existing charts often lack documentation which make it a bit painful to tune

The main challenge with Helm will be to pre-provision the GKE clusters with
Helm in a clean way, ideally not running by `helm init` but in a more "as-code"
approach.

## Links

- <https://dzone.com/articles/terraform-vs-helm-for-kubernetes> has been useful
  to transmit a more concrete insight on Terraform vs Helm.
- [Official Helm charts](https://github.com/helm/charts)
