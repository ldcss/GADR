# 8. Store search query in URL

Date: 2022-01-23 (Backfilled 2022-02-06)

## Status

Accepted

## Context

This gallery has a search bar where users can filter entries by a search term. This search term is currently stored as a value in a component's React state.

It may be useful to provide a link to a particular search filter to make it easier to share a collection of entries.

## Decision

Search query will be stored in URL.

## Consequences

- Search query will be appended to links for pixel art entries to ensure that the query is persisted as the user navigates between entries.
- Special characters in query string will need to be encoded and decoded accordingly to ensure that they are displayed correctly.
