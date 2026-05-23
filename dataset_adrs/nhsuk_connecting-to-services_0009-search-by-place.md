# 10. Count the number of checks made by bots and other automated checks

Date: 2018-02-01

## Status

Accepted

## Context

There are a lot of automated checks performed against the application. These
checks are being counted as part of the normal traffic and there is no way to
currently filter them out. There is a need to remove the bot traffic so real
user behaviour can be identified.

## Decision

The decision is to count any request that includes a query string parameter `check`.

## Consequences

The number of search and result page views as a result of bot traffic will be
able to be removed from charts showing overall activity. This will allow the
real user behaviour to be identified.
