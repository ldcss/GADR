# 6. Split nearby and open results into separate endpoints

Date: 2018-01-12

## Status

Accepted

## Context

The primary (only) consuming application for this API needs to show both open
and nearby services on separate pages (and more of them). Previously the
application had shown a mix of open and nearby services within a
single page.
Having the API so closely aligned to the needs of the consumer is not ideal.
There is scope to increase the flexibility of the API along with increasing the
ease with which it can be used both by the current and future consumers.

## Decision
The decision is to add a new endpoint i.e. `/open` alongside the current
`/nearby` endpoint. The former endpoint will return only services that are open
where the latter will be refactored to return only services that are nearby
regardless of their opening state.

## Consequences

The consequences of this change are:
- The API will be less tightly coupled to `connecting-to-services` (the primary
  consumer), increasing its utility
- The API's interface will have a breaking change and rework will be needed by
  `connecting-to-services`
- The API will be easier to use in part due to the query string parameter
  specifying the limit for the number of results returned being the same for
  both endpoints
