---
id: prefer-open-source-software
title: 3. Prefer open source software
---

# 3. Prefer open source software

Date: 2021-04-09

## Status

Accepted

## Context

A question was raised where a system was being developed with Microsoft SQLServer. The solution does not require SQLServer and it would be straightforward to port to [PostgreSQL](https://www.postgresql.org/).

Further investigation, in slack, gave answers of:
> _"Hi, PostgreSQL always unless there's a very good reason you specifically need SQL Server"_

> _"Hi, as we follow open standard, we always recommend free open source as a first choice unless there is a good reason not to use open source."_


## Decision

Free and open source software will be selected as a first choice, unless there is a good reason not to use open source.

Example: PostgreSQL instead of Microsoft SQLServer.

## Consequences

Software systems will promote the use of open source while being lower cost to run and maintain.
