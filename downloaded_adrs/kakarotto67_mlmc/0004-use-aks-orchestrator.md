# Use AKS orchestrator for the MLMC app

* Status: [accepted]
* Deciders: [[@kakarotto67](https://github.com/kakarotto67)]
* Date: [2019-09-14]

Technical Story: [Configure Kubernetes orchestrator for whole app and deploy it to AKS](https://github.com/kakarotto67/mlmc/issues/12)

## Context and Problem Statement

Since the product is going to be based on Microservices architecture there is a need for good orchestrator to host its different parts.

## Decision Drivers

* Easy to use
* Easy to learn
* Possibility to host modules as Docker containers
* Well integrated with Azure
* Well integrated with Azure DevOps

## Considered Options

* [Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/)
* [Azure Service Fabric](https://azure.microsoft.com/en-us/services/service-fabric/)

## Decision Outcome

Decided to use AKS since

* It is more powerfull than ASF
* It is more suitable for Docker containers hosting
* ASF have to be used when you plan to use its programming model (stateless services, stateful services, actors), but I didn't need that
* Kubernetes seems more popular and evolved
* Kubernetes has managed implementation for Azure - AKS

### Positive Consequences

* I will be able to use orchestrator to host app's modules.

### Negative Consequences

* n/a

## Links

* n/a
