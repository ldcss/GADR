# 1. APP_BACKEND - Modules architecture

Date: 2020-04-04

## Status

Proposed

## Context

We need to keep extendable architecture in order to prepare for future changes, 
because we work in very flexible manner and requirements changes and evolve a lot.

## Decision

In backend directory:
- *libs* - technical parts of software - implementations of database connections etc. In the future will be moved to npm packages, 
but we leave it now for easier and faster development to avoid unnecessary complexity.

Folders in backend **src** directory are splitted by names of bounded contexts.
 
Each BC, which follow CQRS manner, has following subdirectories:
- *write-side* - keeps logical separated parts, which keep ubiquitous language + one domain inside each boundary
Each bounded-context will follow directories in manner of Domain-Driven Design Layered Architecture proposed by Eric Evans.

- *read-side* - projections from domain events of write-side
