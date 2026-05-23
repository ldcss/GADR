# 2. Store OAuth2 clients in JSON

Date: 2017-09-13

## Status

Accepted

## Context

Profiles acts as a proxy for ORCID's OAuth2 service, and has its own list of (eLife) clients, eg Journal. This list is small and reasonably static.

## Decision

The list of clients will be maintained in a JSON file.

## Consequences

This data file will need to be provisioned, alongside normal application configuration.
