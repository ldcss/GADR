# 1. Record architecture decisions

Date: 2022-03-08

## Status

Accepted

## Context

When working with our database schema which has evolved over time in response to changing needs it's become apparent that some similarly named columns are easily confused. An example is where `case_id` existed alongside `court_case_id`. The first of these is a business key used by Common Platform and ourselves, whereas the second is a foreign key referencing the `court_case` table (i.e. `court_case.id`. These are both sensible names in isolation but are confusing when they appear together.  

## Decision

We will prefix columns which reference foreign primary keys with `fk_`. For example `fk_hearing_id` would reference the `id` field of the table `hearing`.

If the foreign key in question is a business key, for example `crn`, then there is no need for this prefix as it w

## Consequences

- Will prevent confusion of columns referencing foreign primary keys and business keys
