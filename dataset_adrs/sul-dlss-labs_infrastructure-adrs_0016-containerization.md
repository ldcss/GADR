---
layout: default
title: ADR-0016
nav_order: 19
permalink: records/0016/
---
# Containerization of SDR applications

* Status: drafted
* Decider(s):
  * Vivian Wong
  * Julian Morley
  * Infrastructure Team
  * Operations Team
* Date(s):
  * Status (from above): 2022-08-05

## Context and Problem Statement <!-- required -->

Currently, SDR infrastructure is managed by Puppet and SDR applications are deployed using Capistrano.

This approach has a number of shortcomings, which results in SDR instability and requires significant time from the Infrastructure and Operations Teams for troubleshooting. It also hinders our agility, as provisioning new servers takes time and requires manual intervention.

These shortcomings include:

* Server inconsistency: Servers vary in a number of ways between environments (e.g., dor-services app stage and prod) and within an environment (e.g., dor-services-app-a and dor-services-app-b). While some of these variations are necessary (e.g., being connected to different storage), others are unnecessary and problematic (e.g., having different versions of Ruby installed in different ways, different versions of libraries, etc.) This problematic variation is due to manual interventions on the server and because different puppet specifications are kept for each server and must be manually kept in sync. In the past several years this has also been complicated by server OS migrations, where different environments are running different OSes.
* Development inconsistency: The local development environments differ from the deployment environments to a significant degree; this inconsistency leads to "surprises" when moving an application to a deployment environment. Of course, the environments cannot be identical, but the less differences the easier it will be to detect issues at development time.
* Puppet / Capistrano mismatch: Relying on both Puppet and Capistrano makes some activities like upgrading Ruby very difficult, as it requires coordinating changes in both locations and performing manual operations.
* Too much manual intervention: Overall, provisioning, deploying, and maintaining our applications require too much manual intervention by both the Infrastructure and Operations Teams.
* No canonical specification of application requirements: Applications requirements (e.g., libraries, ports, storage mounts) must be gleaned from multiple sources (e.g., multiple puppet configurations, DevOpsDocs, repository READMEs, shared_configs, etc.) This makes server provisioning and maintenance very error prone.

It is proposed to use containerization, in particular Docker images, as a deployment strategy for SDR applications. There are a variety of approaches for using containerization that are described under Considered Options.

## Decision Drivers

* Consistent deployment of SDR applications and provisioning of servers.
* Separation of responsibilities such that Operations handles provisioning of servers and Infrastructure handles deployment of applications (i.e., maintain the current approach).
* Realistic technical requirements given current priorities, staffing, and funding levels.

## Considered Options

* Docker images running in Kubernetes
* Docker images running on Puppet-managed servers with images built on server
* Docker images running on Puppet-managed servers with images pulled from Docker repository (e.g., Docker Hub)

Note that it is possible to take an incremental approach, viz., start with Docker images running on Puppet-managed servers with images built on server then move to images pulled from a Docker repository, and then move from Puppet-managed servers to Kubernetes.

## Decision Outcome

To be determined.

## Pros and Cons of the Options <!-- optional -->

### Docker images running in Kubernetes

* Pro: Kubernetes provides advanced provisioning features, e.g., auto-scaling.
* Pro: Kubernetes provides the ability to quickly spin-up and tear-down testing environments.
* Con: Kubernetes is extremely complicated.
* Con: While DLSS is adopting Kubernetes for some projects, it is likely to be some time before SDR would be a candidate.

### Docker images running on Puppet-managed servers with images built on server

For this approach, Puppet would be used manage servers running Docker. Puppet would no longer handle Ruby, libraries, etc., but would continue to manage storage, firewall ports, and provide secrets via environment variables.

Docker Compose would be used to run one or more containers on the server. For example, a server might run an Apache container (for Shibboleth) and a Rails container (for the web application). Or a server might run multiple instances of a Sidekiq worker container (similar to current servers running multiple Sidekiq worker processes). The minimal orchestration requires for this is a good fit for Docker Compose, while also providing some abilities for environment specific configuration. Together, Docker and Docker Compose provide a clear canonical specification of application requirements.

In general, the containers running on the server would match the server's current responsibilities. For example, argo-prod-01 would run the Argo web application and Sidekiq workers; it wouldn't also run DOR Services App.

Puppet managed storage would be shared into the Docker containers.

In addition, Capistrano would be used to deploy the application. This leverages existing tooling for deploying code and configuration, including handling testing of branches. However, instead of starting processes on the server, Capistrano will build Docker images and start/stop Docker containers running those images.

* Pro: Re-uses existing Puppet-managed infrastructure.
* Pro: Re-uses existing tooling for deploying code, configuration, and secrets management.
* Pro: Requires minimal changes to development and deployment processes.
* Con: Does not guarantee that identical containers are running on different servers.

### Docker images running on Puppet-managed servers with images pulled from Docker repository

This is similar to the above approach, except code will not be deployed to the server and the Docker image will not be built on the server. Instead, the Docker image will be built elsewhere (developer machine, CircleCI) and pulled to the server.

* Pro: Guarantees that identical containers are running on different servers.
* Pro: Most consistent with prevailing industry practices.
* Con: Requires changes to development processes to handle automation of build images.
* Con: Requires new, undetermined approach to configuration and secrets management. (It is preferable that the Infrastructure Team be able manage configuration without Operations Team involvement, similar to existing shared_configs approach.)

## Out of scope

* Continuous deployment: CD is not a goal of this ADR.
* Replace shared_configs / better secrets management: It may make sense to consider as adjacent of this work.
* Containerization of core services, e.g., databases, Redis, RabbitMQ

## Other considerations / open questions

* Can Shibboleth be run in a container?
* Are there UIT firewall, load balancer, or other that are problematic for containers?
* How would cron jobs be handled?
* What are the security best practices / processes that should be followed for containers?
