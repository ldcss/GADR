# 16. live-vs-static-site

Date: 2020-09-26

## Status

2020-09-26 proposed

## Context

By live application I mean that the APIs are required for the lifetime of the application and by static, the APIs are only required once - at build time or for storage.

Building a data-driven application for a portfolio has the risk that the data will become stale or inaccessible - for example if the API keys expire, the API changes or the service is no longer available. This can break the consuming application. In maintaining the Korin app, I have experienced Last.fm and IBM Watson APIs breaking due to API changes or expired API keys.

## Decision

Facing the concern that data-driven applications will break due to maintenance issues, I have decided to build them as static apps i.e. process or store the data once and present the results.

## Consequences

- These apps will by nature become dated by the time they were deployed. This creates the need for additional data maintenance tasks to refresh them. The benefit of a discrete data maintenance task is that I will be aware of any breaking changes and can take appropriate actions.
- This creates an opportunity to experiment with JAM-stack applications.
- The reduced complexity will hopefully make building apps simpler. It may also make it difficult to experiment with more advanced architectures like event-driven architectures.
