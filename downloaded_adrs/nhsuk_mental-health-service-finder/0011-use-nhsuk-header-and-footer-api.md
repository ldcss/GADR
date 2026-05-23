# 11. Use NHSUK header and footer API

Date: 2020-07-21

## Status

Accepted

## Context

A API has been created which can be used to build header and footer links for NHS.UK.
We want to use this across all NHS.UK applications.

## Decision

Build a middleware function which can get the header and footer links from the API and
make them available within the Nunjucks templates. We will also cache these to prevent
a massive amount of calls to the API 

## Consequences

The header and footer will be more consistent with nhs.uk and require less maintenance.
