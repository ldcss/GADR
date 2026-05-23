# 3. doc-about-platform

Date: 2020-02-17

## Status

Accepted

## Context

Goal: I need to select a platform for the infrastructure.

A platform?

Ok, at first, it came to my mind the idea of Platform as a Service.  I have
 three options here:

- Heroku and Cloud Foundry 
- Kubernetes
- Openshift

Also I think it could be possible to consider other solutions, like:

- AWS ECS
- AWS EKS 
- Google GKS
- Azure AKS


All of them are good options for managing microservices architectures,
 but it depends on the perspective.  As SRE, I want to keep things under
 control, so I'm going to use something I can create from scratch.  So
 I will discard Heroku now and all the managed solutions (*KS and AWS ECS).

Cloud Foundry is really a good idea from the developer point of view, as
 the only thing she has to do is just focus on development.  Cloud Foundry
 uses the concept of code deployment (it takes a directory or repository and
 builds the code and deploy it to the cells.)

Pros: it's very easy from a end user point of view, and fully compatible with
 other Cloud Foundry providers (think of IBM Cloud, Pivotal, Anynines...).
Cons: it requires license to use it and it requires lots of resources (it's for
 very large deployments).

Kubernetes: it's a standard de-facto of the container world.  Google uses it,
 Amazon uses it, Azure uses it.  And the open source community is pushing it
 a lot.  It has lots of documents, addons, blogs, meetups...

Pros: best documented solution, and more affordable (it's free).  Lots of tools
 to help with the deployment and administration of the platform.

Cons: complex. Very complex.

Openshift: I know it's more a platform as a service solution than a container
 orchestrator or platform.  Internally it uses kubernetes, but with more layers.

Pros: It must be very complete
Cons: I don't have any experience at all with openshift.


### Let's talk about costs

I would like to add here an interesting topic: Costs.

To design a System Architecture, you must cover the following set of features:

- Availability
- Economy

Availability

Availability for me includes these topics:

- Maintenability
- Testability
- Usability
- Scalability
- Performance
- Security

Economy

Because at the end, a business must earn money with the value added to the market.

So there is a complex formula to balance Availability and Economy.

Public cloud is cheaper at the beginning, but it becomes expensive quickly.

Private cloud is expensive at the short and middle scope, but it can be cheaper when the business is mature.

## Decision

Here is a good branch point.

I have experience managing apps in Cloud Foundry and Kubernetes, and I like how
 easy is for a developer or a non SRE to deploy an app in CloudFoundry.

But Kubernetes is more appropiate to answer this test, as it will allows me to
 describe all the internals and the steps to make solve the test.

Openshift... It would be nice to try it.

And about economy, it's not so easy to decide between public or private.  I'm 
 going to use my own servers, and my AWS account.

So, I will create a main branch for a solution based on Kubernetes, and I will try
 to keep an eye on Openshift if I have enough time.

## Consequences

Kubernetes is going to be the platform for managing the microservices architecture.

I will create my own cluster of kubernetes on three VM using proxmox, kubeadm and
 kubectl.

I will use my AWS account to test the scalability of the system.