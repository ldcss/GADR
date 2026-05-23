# 2. Containerization with Docker & Docker Compose

## Status

Accepted, 2019-07-01

## Context

The need to deliver PCMT in such a way that it's possible for interested 
organizations to provide it at a reasonable cost in a SaaS model, as well
as for government organizations to have control over their tools and data by 
installing it on-prem calls for a containerization tool that has wide adoption
and which can run in the major host operating systems.

## Decision

We will provide each component of PCMT as a production ready docker image.

We will utilize docker-compose to orchestrate the docker containers that a 
single PCMT instance requires.

## Consequences

Each component of PCMT will be available as a pre-made docker container,
ready for client-configuration.

A PCMT instance will be managed through docker-compose, including configuration.

---
Copyright (c) 2019, VillageReach.  Licensed CC BY-SA 4.0:  https://creativecommons.org/licenses/by-sa/4.0/
