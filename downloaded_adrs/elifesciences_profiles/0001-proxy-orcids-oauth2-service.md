# 1. Proxy ORCID's OAuth2 service

Date: 2017-09-05

## Status

Accepted

## Context

We need to allow applications (eg Journal) to use ORCID's OAuth2 service. We will need to combine data provided by ORCID with other sources in the future.

## Decision

We will proxy the ORCID OAuth2 service, which allows Profiles to see the access token and use ORCID's API.

## Consequences

Applications will need to be configured for eLife's OAuth2 service, rather than ORCID's directly.

Users will have two extra redirects as they pass through Profiles when authorising:

    Journal -> Profiles -> ORCID -> Profiles -> Journal
