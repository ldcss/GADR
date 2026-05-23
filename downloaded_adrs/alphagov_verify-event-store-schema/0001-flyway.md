# 1. flyway

Date: 2018-03-07

## Status

Accepted

## Context

We need a way of running database migrations to the verify event store database.

## Decision

We have chosen to use [Flyway](https://flywaydb.org) since the team has some experince with it and it seems like a simple and lightweight option.

## Consequences

If Flyway turns out to be more difficult to use than we thought then there will be some rework to use a different tool but the contents of the migration scripts will remain the same.
