# 6. Future ADRs in PIG repository

Date: 2021-08-16

## Status

Accepted

Supercedes [1. Record architecture decisions](0001-record-architecture-decisions.md)

## Context

ADRs are important documents detailing how we do things in our domain.
Often an ADR will point to a new feature or even an entirely new service to create.
When an ADR initiates the creation of a new service, where does the ADR belong?
In the new repo, or in the repo where the idea originated?

Would it simply be better to collect ADRs in a central location?

## Decision

When writing new ADRs, they will be in the [PIG repo](https://github.com/navikt/pig).

## Consequences

ADRs will not be close to the code they are relevant to.
ADRs will be easy to locate, and can contain cross-service details.

