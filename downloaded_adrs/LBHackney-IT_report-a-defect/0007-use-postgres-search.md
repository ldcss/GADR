# 7. Use Postgres Search

Date: 2019-05-29

## Status

Accepted

## Context

The New Build Team need to be able to perform basic search over properties for finding properties to either report defects against or to manage existing defects.

## Decision

To implement search we will use the built in Postgres Search rather than adding a new dependency on another service like ElasticSearch.

## Consequences

In the short term we will be able to get this working very quickly and it will not require any changes to the infrastructure, nor additional costs for Heroku addons.

As this tool is not as feature rich as external services like ElasticSearch this option may reduce flexibility in the future if search becomes more complex.
