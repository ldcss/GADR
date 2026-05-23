# 33. Two identity providers: development / run

Date: 2020-09-21

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

## Context

Access to the solutions (applications) as a user, referred to as the _run_ environment, is based on the company identity provider. Access to the development/operations environment, the GCP platform, is based on a separate, DevOps identity provider. This allows strict separation between Run and DevOps and makes automation of DevOps practices somewhat easier.

## Decision

We will use a separate identity provider to access the platform for DevOps practices, disconnected from access to the _run_ environment.

## Consequences

### Advantages

* Flexible and best fitting identity provider in DevOps, decoupled from the company identity provider.
* Reduced risk of DevOps privileges making it work for a developer, but not for a normal user.

### Disadvantages

* Additional overhead of user management and corresponding procedures.
