# 4. feat-about-orchestration

Date: 2020-02-17

## Status

Accepted

## Context

Goals:

1. To select an orchestration technology suitable for this type of architecture.
2. The solution must be scalable according to the load.

Here I'm going to talk about Infrastructure as Code (IaC), the way to define a system
 architecture for running applications in the cloud.

By defining resources in a text file and process them using specific API engines, a 
 cloud company can create a set of computing units, networks, users and services in a 
 repeatable and under version control way.  That allows to create new ways to manage
 infrastructure, network, storage.

To read the file we use tools that will contact the APIs and engines to control the
 order and the execution of each task performed by the engines.  These tools are called
 orchestrators.

Orchestration tools exist for creating the resources needed to deploy
 applications.  But there are two models here:

- Those that reuse resources (mutable servers)
- Those that don't reuse resources (inmutable servers)

For a microservices architecture, our main purpose is to quickly replace those
 services, with no downtime.

For this, the inmutable servers philosophy is better, as you can launch an
 instance of the new version, test it, and decide to enable it in production 
 without risking the rest of services.

Well, not so valid if we consider database migrations, but it requires to set
 some requirements about database management that are far from the scope of 
 this test.

To scale apps you can upgrade computing resources (vertical scaling), or
 adding more computing instances provisioned with the app (horizontal scaling).
   Both can be performed easily with inmutable servers.

Which orchestration tools use the inmutable servers perspective?

- [AWS CloudFormation](https://aws.amazon.com/cloudformation)
- [Terraform](https://www.terraform.io)

AWS cloud formation uses a json-like text file where resources like computing
 units, vpc, load balancers, databases, etc., are defined to create and 
 provision the declared resources.  This file can be versioned and stored in 
 a version control system.  This allows you to recreate the resources used in 
 each stage of the development of the applications.  The main issue here is 
 that is only valid for AWS.

Terraform, by hashicorp, uses a DSL (Domain Specific Language) that makes easy
 to define resources.  Also, it allows to define providers for several 
 platforms and services, so it's not limited to AWS, but it can work with 
 Google, Azure, IBM, bare metal, vmware, etc.

But for Kubernetes, there is another tool that works as orchestrator: 

* [kops](https://github.com/kubernetes/kops)

This tool, that it is used to manage and orchestrate clusters, groups and 
 secrets in AWS and other cloud platforms, uses terraform internally.  So it 
 can be used to generate a terraform set of files and store them in a version
 control system to do the same.

## Decision

I'm going to use kops for the management of the clusters, and I'm going to
 generate templates that can be used to deploy new clusters depending on the
 requirements of an environment like development, staging or production.

## Consequences

The first thing I change here is that it is not possible to keep using my own
virtual servers to create the kubernetes cluster.  Everything now will be
 running on AWS.

