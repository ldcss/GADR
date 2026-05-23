# ADR-002. Rebuild Nomis in Azure

Date: 12/09/2019

## Status

Accepted

## Context

The modernisation of the Fix & Go infrastructure requires an initial decision on what system to start with and what overall approach to take.

There is a large amount of prior experience and assets that might be used form the Delius AWS migration. 
This may or may not be a way of saving time on delivery, and/or increasing consistency within MoJ.

There is a discussion document (with comments from team members) here https://docs.google.com/document/d/12p3nUA4NnJplcQyj8p3QOx2je4gTjO_z3ADvH1k5tk0/edit

## Decision

We will start by modernising Nomis, as it is the largest and most critical system under our management

We will aim to deliver a working DR environment, with ability to bring it online, as this removes a large piece of operational risk

We will build this and other environments and tooling in Azure, as this reduces the impact of migration on external clients and dependencies of Nomis

We will create a new architecture for Nomis rather than refactoring the existing environments, as we consider the system simple enough that this will be more efficient

We will reuse patterns, practices and any platform-agnostic code from Delius/AWS wherever possible, as this will save development time

## Consequences

We have prioritised the business goal of delivering a Disaster Recovery capability to Nomis, 
with the constraint that we use good engineering practice rather than quick and dirty. 
This is because we know we will need to replicate and maintain this work for many environents.
