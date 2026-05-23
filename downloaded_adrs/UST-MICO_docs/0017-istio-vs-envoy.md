# Istio vs. Envoy

Part of the Technical Story: [Evaluate Istio vs. Envoy vs. xxx](https://github.com/UST-MICO/mico/issues/75)

## Context and Problem Statement

We want to have telemetry (performance, monitoring) and log collections for each MICO service that should be added automatically during deployment.

## Decision Drivers

* MUST be compatible with Kubernetes
* MUST at least provide all required features (telemetry, logs)
* MUST be independent of the technology used in the respective service
* SHOULD consume less resources

## Considered Options

* Istio
* Envoy

## Decision Outcome

Chosen option: Istio, because it is easier to configure than only using Envoy. By using Istio the Envoy proxies can be used as the data plane and Istio as the control plane to manage the whole service mesh.
Moreover Istio is the better choice for the future, because it has all features that could be potentially helpful for the management of a service mesh.

### Positive Consequences

* Istio enables more than just having telemetry and log collections. In addition it provides many more features that could be useful for MICO in future (follow-up decisions required).

  [Examples](https://istio.io/docs/concepts/what-is-istio/#why-use-istio):
  + Automatic Load Balancing
  + Routing rules, retries, failovers, and fault injection
  + Pluggable policy layer with access controls, rate limits and quotas
  + Secure service-to-service communication in the cluster

### Negative consequences

* Istio consumes many resources
* Istio brings more complexity into the MICO system

## Pros and Cons of the Options

### Istio

* Good, because it provides the control plane to configure the Envoy proxies (sidecars)
  + Istio Proxy (extended version of Envoy) is easier to configure than plain Envoy
  + It is integrated into Kubernetes with Custom Resource Definitions, therefore Istio is configurable with the same YAML DSL than Kubernetes
* Good, because it provides additional functionality that could be relevant in future (e.g. access control, secure communication, routing rules)
* Bad, because Istio has a steep learning curve to get familiar with all its features
* Bad, because it is still in development (though the current version is 1.0.5)

### Envoy

* Good, because it is a high-performance proxy with a lightweight footprint (developed in C++)
* Good, because it a graduated project of the Cloud Native Computing Foundation (next to Kubernetes and Prometheus)
* Bad, because the YAML DSL for configuration of Envoy differs from that of Kubernetes, which we are accustomed to use
* Bad, because in a service mesh it's complex and error prone to configure
