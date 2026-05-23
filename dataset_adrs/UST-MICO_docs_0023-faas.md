# FaaS

## Context and Problem Statement

To execute a variety of different functions that are based on different messaging patterns we want to use the Function as a Service (FaaS) approach.

## Decision Drivers

* MUST support Kubernetes
* MUST support Kafka to trigger events
* SHOULD be a well known and proven solution
* SHOULD support the most common programming languages (at least Java, Python, JavaScript)
* SHOULD support the Serverless framework

## Considered Options

* [OpenFaaS](https://www.openfaas.com/)
* [OpenWhisk](https://openwhisk.apache.org/)
* [Kubeless](https://kubeless.io/)
* [Knative Serving](https://github.com/knative/serving)

## Decision Outcome

We want to use OpenFaaS.

## Pros and Cons of the Options

### OpenFaaS

* Good, because it supports Kubernetes
  * via [faas-netes](https://github.com/openfaas/faas-netes) (installation via Helm or `kubectl`)
  * via [OpenFaaS Operator](https://github.com/openfaas-incubator/openfaas-operator)
* Good, because it supports the Serverless framework
* Good, because it is an easy to use Serverless framework
* Good, because it has a simple architecture and can be well understood
* Good, because it supports Kafka via the [Kafka-connector](https://github.com/openfaas-incubator/kafka-connector)

### OpenWhisk

* Good, because it supports Kubernetes (installation via Helm)
* Good, because it supports the Serverless framework
* Good, because it is a mature Serverless framework supported by the Apache foundation and backed by IBM
* Bad, because it is more complex than OpenFaaS and it leverages many components (CouchDB, Kafka, Nginx, Redis and Zookeeper)

### Kubeless

* Good, because it integrates natively into Kubernetes as a CRD
* Good, because it supports the Serverless framework
* Good, because it doesn't require extra tooling (`kubectl` is enough)
* Good, because it uses Kafka messaging system as event triggers
* Bad, because it isn't as mature as OpenFaaS or OpenWhisk, documentation isn't as good as the others

### Knative Serving

* Good, because it is baked by Google
* Good, because it supports Kubernetes
* Good, because Knative Eventing supports Kafka events
* Bad, because it requires Istio
* Bad, because it is more complex than e.g. OpenFaaS
