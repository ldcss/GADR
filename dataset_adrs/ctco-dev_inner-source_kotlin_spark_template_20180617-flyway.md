# Flyway dockerized util and db migration scripts 

## Status

Accepted

## Context 

Developers need some tool for DB versioning and safe migrations.

## Decision 

We will introduce dockerized flyway setup for local development.
Migration scripts will also be provided.

## Consequences  

Developers will be able to use specific version of the DB schema in local setup.
CI server will be able to run DB migrations.