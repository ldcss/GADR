# 5. refresh data on major version change

Date: 2018-02-14

## Status

Accepted

## Context

Data structure may change between releases of the ETL.
The ETL uses a scrape of previous data to reduce unnecessary work.

## Decision

The major and minor version will be included in the seed data file to identify a change of data structure.

## Consequences

If the major or minor version changes a scrape of all the pharmacies will occur.
It is assumed that any data structure change will be identified as a major or minor version change.
Any version changes that does not alter the data structure will also force a scrape.
A patch release will not perform a full scan.
