# 1. Spring Boot as web framework

Date: 2017-06-30

## Status

Accepted 

## Context

We need to choose a web framework for the app.

## Decision

We use Spring Boot because it allows us starting fast, and concentrating on business logic of the app, rather than working on infrastructure tasks.

## Consequences

- Spring is big, slow, and contains a lot of black magic inside. We may meet issues when standard components are not easily configurable as we need.
- Debugging is complicated.
- Produced binaries are big and slow.
