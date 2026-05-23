# 13. feat-implement-helm

Date: 2020-03-12

## Status

Accepted

## Context

Now we have applications that get deployed into our microservices platform, we
 need to manage the configuration in an easy way.  YAML files are nice, but are
 difficult to reuse or to publish in order to manage vast amounts of
 deployments.  We need more tools.
 
 
Helm is a solution that eases distribution of kubernetes applications by using
 the concepts of Charts and Releases.
 
As the manual states, a Chart is a Helm package. It defines the resources to
 run an application or tool inside a Kubernetes cluster.  A Release is an
 instance of a Chart running in a cluster.  Each time a Chart is installed, a
 new release is created.  So it's reusable code.

To reuse this code and make it more accesible to others, there are repositories
 like in other package managers.  A Helm Chart can be published in a Repository
 to use it widely.

This provides huge advantages to the manageability of the applications deployed
 in Kubernetes clusters.
 
 
## Decision

I'm going to implement helm packages to replace the templates in the kube
 subfolder of each application.
 
By now, I'm not going to use a remote repository, just the local definition of
 the Helm Chart.  

## Consequences

Right now, the way to deploy the code to the Kubernetes cluster needs to modify
 a handmade template using envsubst.  This will be superseeded by Helm, as
 instead of creating temp files, we can pass the new values (like the version
 of the docker image) by command line.
 
As a disadvantage, Helm adds complexity to the system, and needs to be managed
 the same way as the code.

