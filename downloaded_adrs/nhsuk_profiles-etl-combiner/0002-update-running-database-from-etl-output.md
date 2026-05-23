# 2. Update Running Database from ETL Output

Date: 2017-06-19

## Status

Accepted

## Context

GP Data changes on a daily basis.

Nightly ETLs are run to obtain Syndication and POMI data.

Currently [profiles-db](https://github.com/nhsuk/profiles-db) requires manually updating from the ETL outputs, and re-deploying to refresh the data.
No automated validation of data is performed during the update.

## Decision

To avoid a new release of [profiles-db](https://github.com/nhsuk/profiles-db) each time data changes, data will be inserted into a running mongodb instance on a daily schedule.

The output from the nightly [gp-data-etl](https://github.com/nhsuk/gp-data-etl) and [pomi-data-etl](https://github.com/nhsuk/pomi-data-etl) will be validated and combined.

The contents of the existing database will only be replaced if the new data is of a comparable size.

## Consequences

The profiles database will contain a snapshot of Syndication and POMI data from the previous day.

[profiles-db](https://github.com/nhsuk/profiles-db) will be obsolete as a mongodb containing initial data is no longer required.
