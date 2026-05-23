# 3. Host two mongodb-updaters in a Single Stack

Date: 2017-06-28

## Status

Accepted

## Context

Two different MongoDBs need to be updated on a daily basis.

## Decision

Given the small number of databases to be updated both services will be hosted in the same stack, rather than manually create a stack for each database updater.

## Consequences

The repository will hold a docker-compose file to define a stack containing the Pharmacy and the GP database updaters.

Both mongodb-updaters will be automatically deployed using the existing infrastructure as a single unit.
