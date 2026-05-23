# 3. Single source of truth

Date: 2020-05-09

## Status

Accepted

## Context

We want the data to be in one place, be it internal (in the static assets) or external (served by an API or an S3 bucket...)
We want the project to be data-driven, so that the document is re-rendered if any data changes.
We want the data being spread across the Components using the latest technologies.

## Decision

The source of data is kept internally. It will stay in the webapge, as a static asset from now on.
But the project must be kept easily switchable to an external data source.
We spread the data across Components using React Context API.

## Consequences

All the data will be stored in the context folder and will be consumed using useContext hooks.