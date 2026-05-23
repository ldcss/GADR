# 4. Build an abstracted resident store

Date: 2020-12-10

## Status

Accepted

## Context

A critical part of building these services is being able to track who evidence belongs to, and therefore we must be able to identify residents in a platform-wide manner.

At the time of this decision, the HackIT team is in the process of building the Platform APIs necessary to provide access to this sort of core data, but they are not available yet.

## Decision

To build a resident data source in this application, but make the extra effort to abstract it appropriately so that when an external resident data source and accompanying API is available.

## Consequences

This decision means we will require two Gateways for the same data source (the PostgreSQL database), which means our ORM cannot build relationships between Residents and other models automatically but instead this will have to be done in code.

This means our codebase will be slightly more verbose and it will be slightly harder to build domain models which relate to residents, but it means that we have a single point of change (the gateway) when a new data source is available.
