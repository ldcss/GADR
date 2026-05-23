---
id: use-iso-8601-format-for-dates
title: 2. Use ISO 8601 format for dates
---

# 2. Use ISO 8601 format for dates

Date: 2021-03-25

## Status

Accepted

## Context

The system is composed of a number of API and related datastores. There are currently a number of differing date formats in use.

## Decision

We will use the ISO 8601 format for dates: yyyy-mm-dd and times.

## Consequences

Dates and times are displayed in a standard, culture-neutral format.

Standardisation will simplify development effort, permitting focus on business value.
