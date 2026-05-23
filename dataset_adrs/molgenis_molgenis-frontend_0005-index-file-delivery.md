# 5. Index file delivery

Date: 2020-11-09

## Status

Proposal

## Context

*See [frontend architecture sessions](https://docs.google.com/document/d/1VW3ah5VAvAz2KnqNZlNmVqCzFhBMlIcjPPUlsHMFRIY/)
for background information on micro-frontend/SPA architecture.*

We need a consistent method to serve the index file for our frontend application.

## Decision

We are going to use a clientside index file for the *@molgenis-ui/core* app.

## Consequences

All info that we need in the client must be accessible via API. E.g. logged in, theme, roles.
Everytime we create new app, or existing apps that we refactor, we will change to this design.
Everytime we find we need something extra client side it must be available via API.
