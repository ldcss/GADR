# 4. Compute Provisioning through Ansible

## Status

Accepted, 2019-07-01

## Context

While PCMT's basic unit of deployment is Docker and Docker-Compose 
([ADR #2](adr-002.md)), and Terraform is able to provision a cloud environment 
([ADR #3](adr-003.md)), we still need to address a gap where the computing 
environment needs to be provisioned and client configuration needs to be loaded.

## Decision

We will use ready-made Ansible roles to install the latest versions of
Docker and Docker-Compose, utilized through Terraform.

We will build PCMT Ansible role's that will serve as a template and are 
available in the Ansible Galaxy repository.

Configuration of a PCMT instance will be managed as part of an Ansible Playbook.

## Consequences

Deploying, upgrading and destroying PCMT instances will be managed through
instance specific Ansible playbooks.

The target environment will need to be addressed and accessible from the
controlling environment over SSH.

---
Copyright (c) 2019, VillageReach.  Licensed CC BY-SA 4.0:  https://creativecommons.org/licenses/by-sa/4.0/
