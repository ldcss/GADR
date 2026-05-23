# 6. Full nightly scrape

Date: 2018-04-26

## Status

Accepted

## Context
A list of IDs retrieved from Azure Storage is used to seed the ETL scrape.
The `modifiedsince` end point in syndication is used to detect when records have changed, or new records
have been added, enabling an incremental scrape of data.

The `modifiedsince` endpoint does not currently include records that have been removed, hidden, or unhidden.
Records may also be added much later than the modification date, i.e. a record modified in January may not
be published to Syndication until March. In these cases the record changes will not be reflected in the ETL.

## Decision

The `modifiedsince` end point will only be used to detect newly added pharmacies, which will be added to the
seed ID list.
All entries in the seed ID list will be refreshed overnight. If an ID has been deleted, the details will be recorded
in the summary file as reporting a 404 error, and the record will not be present in the output JSON.

## Consequences

All 11,000 records will be refreshed every night, whether they have changed or not.
