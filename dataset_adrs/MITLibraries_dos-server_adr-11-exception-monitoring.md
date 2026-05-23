# Sentry for Application Exception Monitoring

## Context

An application is needed for real time production error discovery and reporting. Sentry is currently being
used by DLS for various applications.

## Decision

We will use Sentry for application exception monitoring.

## Status

Accepted

## Consequences

Logging related configuration should be checked to ensure that Sentry is not bombarded with
irrelevant stack traces for ingests, etc. 