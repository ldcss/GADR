# 2. Reports Unique Reference

Date: 2020-01-21

## Status

Accepted

## Context

In this integration, Digideps requires Sirius Public API to expose a unique identifier for a successfully created report.

This ID is saved by Digideps and used when creating supporting documents against a report

Reports are generally one-per-year-per-donor, but in certain circumstances multiple reports may be generated which cove rthe same reporting year. Both versions are saved in Sirius and need to be uniquely referencable.

## Decision

Sirius Public API will expose a UUID for each report that is created via the Deputy Reporting Integration

## Consequences

* The Deputy Reporting Integration will have the unique ID it requires.
* UUID's also allow us to decouple reports services from Sirius if needed at a future date.
