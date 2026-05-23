# Specify API Version For Every Operation

## Status

Accepted

## Context

Since the API version for a given resource is unpredictable, we need a way to specify the api version on a request by request basis. We also need to make sure this remains backwards and forward compatible in case versions are updated before the library is.

## Decision

An operation should default it's API version to the latest version, but allow it to be overridden by passing in a `api_version` argument.

## Consequences

Specifying the `api_version` argument over and over is verbose.
