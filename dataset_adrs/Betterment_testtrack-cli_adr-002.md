# ADR 002: Destroying splits not present in schema is not allowed

## Status

Accepted

## Context

We are transitioning from Rails migrations and a legacy TestTrack schema
format to testtrack CLI. In order to have confidence that migrations
will apply cleanly in production, we need to validate as much as we can,
and we have a path to full information on extant splits.

## Decision

We will not allow retirements of splits missing from the schema. We will
instead import all legacy splits and validate against the schema.

## Consequences

If we import the legacy schema, we can have complete information about
splits in the field, even for splits defined before the TestTrack CLI
was created, allowing us to fully deprecate the legacy migrations
immediately.

Duplicative split destructions merged from different branches will fail
to apply and force us to delete the offending duplicate migration to
unjam the migration runner. If this becomes an issue we can revisit.
