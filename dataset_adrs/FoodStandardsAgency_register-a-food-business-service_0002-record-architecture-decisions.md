# 1. Store Notify template IDs in Config DB

Date: 2018-11-05

## Status

Accepted

## Context

Notify Template IDs were stored in Environment variables, and this would have to be updated for every template change. The fields required by the Notify templates were also hardcoded. This meant that any change to the data fields required a new version of the app to be deployed.

## Decision

We will store Notify template IDs in the Config DB, associated with a specific data schema version number. Requests to the back end must include a data schema version number. Required template fields are fetched via the Notify API and optional fields are created as empty strings if required.

## Consequences

Changes to data required by Notify don't require a new version of the service to be deployed. To add a new data field, a new version of each of the Notify templates must be available in Notify, and the template IDs for these must be available alongside a data schema version in the Config DB. Finally, any client (e.g. the front end) sending requests to the service must include a `registration-data-version` field in the request headers in the semver format.
