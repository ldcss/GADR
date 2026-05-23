# 12. Use the 'Hobby Basic' Postgres plan in production

Date: 2019-07-23

## Status

Accepted

## Context

As the application goes live, we need to ensure that it is using a database with
sufficient capacity.

The production app is currently using the Heroku 'Hobby Basic' Postgres add-on,
which has a row limit of 10 million records, and costs $9/month. The staging
version is using the 'Hobby Dev' add-on, which has a row limit of 10 thousand,
and is free.

The fastest-growing table in this application is most likely `activities`, which
records every CRUD operation made to the `defects` table. `defects` is expected
to grow at a rate of a few thousand records per year.

As the application has just gone into production, we do not have data on which
to project the expected growth rate for the `activities` table, but the current
Postgres plan would allow for 1,000 `activities` records per defect over a year
before we hit the row limit.

The next level up in Heroku's Postgres plan is 'Standard 0', which has no row
limit but a storage limit of 64 GB, and costs $50/month.

## Decision

We will keep the production app on the Hobby Basic plan.

## Consequences

The size of the production data set should be proactively monitored, and in the
event that it nears the row limit of 10 milion, the app should be migrated to a
bigger plan.
