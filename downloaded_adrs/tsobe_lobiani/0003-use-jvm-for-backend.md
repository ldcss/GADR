# 3. Use JVM for backend

Date: 2021-01-09

## Status

Accepted

## Context

Since the backend is monolithic, we need to choose a language or at least a platform

## Decision

We will develop on JVM platform, specifically we will use Kotlin for production code and Groovy for tests

## Consequences

- Initial development pace might be slower, since we are not as fluent in Kotlin and Groovy as we are in Java for example
- These languages are fully interoperable with Java, which means that tons of community-driven Java projects can be 
reused if needed without compatibility issues
