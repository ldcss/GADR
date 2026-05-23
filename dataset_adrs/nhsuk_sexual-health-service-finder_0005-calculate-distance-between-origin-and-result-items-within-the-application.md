# 5. Calculate distance between origin and result items within the application

Date: 2018-12-05

## Status

Accepted

## Context

The move to Azure search has introduced the need to calculate the distance
between the search point and each result item. Previously, when using
Elasticsearch, the distance was returned within the query response. Azure
search does not have this capability, it is currently a
[feature request](https://feedback.azure.com/forums/263029-azure-search/suggestions/17760211-support-geo-distance-in-select-result).

## Decision

The decision is to calculate the distance between the search point and each
result item within the consuming application i.e. the web app. The calculation
for
[great-circle distance](https://en.wikipedia.org/wiki/Great-circle_distance)
is well known and available in numerous languages.

## Consequences

One of the consequences is the web app will contain additional code to perform
the calculation. It is unlikely the code will need to be changed therefore the
additional overhead will be minimal.
Another consequence is that the web app will take some additional time in order
to calculate the distance and serve requests. No specific timings have been
recorded to compare the duration of the web app performing the calculation
rather than the search API. The timing is small regardless of where it occurs
and no appreciable difference to the overall request/response duration is
expected.
