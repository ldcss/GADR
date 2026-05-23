## Title

ADR 1: Backend implementation using REST API principles

## Context

Since both developers will be working in paralel, and time is very limited,
an architecture that allows paralel work is highly beneficial.

## Decision

We will implement the backend using REST API principles, allowing both modules to work independently.

## Status

Accepted

## Consequences

- Two server services will need to be implemented indepently
- All communication between modules will happen through HTTP requests
