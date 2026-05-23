# 6. Tags

Date: 2018-01-10

## Status

Accepted

## Context

Articles need tags to ease classification and navigation across similar topics.

Tags must have a name, slug, language, optional description and optional image.
Given this complexity, we cannot use embedded documents.

The relation between tags' translations is not useful.

We want to be able to retrieve articles for a given tag.

We want to suggest tags for a given language when an article is
created/modified.

We want to be able to modify the description/image for a given tag.

## Decision

Custom implementation of tags as a separate collection.

## Consequences

Articles will have (optionally) n tags associated.
