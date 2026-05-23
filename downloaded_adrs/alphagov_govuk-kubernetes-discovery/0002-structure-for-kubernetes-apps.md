# 1. Structure for Kubernetes apps

Date: 2017-05-24

## Status

Accepted

## Context

We wanted to agree a structure for Kubernetes applications so that we could create
consistent layouts when creating new applications.

This structure should be iterated upon when we start to work more heavily with
migrating apps over to Kubernetes.

We need to also be aware that developers may want to create their own applications
and so must be easily understood.

We want to split open and private repositories easily when we come to start publishing
our work.

## Decision

We have agreed on the following tree:

```
├── data
│   └── my-awesome-app
│   |   ├── development_secrets.yaml
|   |   └── development_configmaps.yaml
|   └── global
|       └── development_configmaps.yaml
└── manifests
    └── my-awesome-app
        ├── deployment.yaml
        └── service.yaml
```

This allows us to split the manifests section of Kubernetes configuration from the
data values that get created and mounted into any deployments.

## Consequences

This structure may not be appropriate to work with, but we can re-evaluate if we find
this problematic.
