# 6. Use custom JSON serialization

Date: 2020-09-25

## Status

Superceded by [12. remove custom json serialization](0012-remove-custom-json-serialization.md)

## Context

Currently, there's a little bit of pain related to serializing JS `Date` objects in NextJS. This especially comes into play on the `/blog` page (where we sort by date) and the `blog/[slug]` pages (where we display the last updated date).

Using a custom serializer allows parsing and sending of rich JS data structures, like `Date`, `Map`, and `Set` without having to do all of the parsing manually.

`superjson` is used internally by `blitzjs`—which I really like—so I'm thinking that should be a good choice to start with. In addition, it has a Babel transform that makes this seamless and noninvasive to the codebase.

## Decision

I will add `superjson` as a dependency to serialize & deserialize initial props that have rich JS data structures.

## Consequences

- This does mark a slight divergence from "vanilla NextJS". As a result it might be good to document.
- I'll need to refactor the data-fetching for a few pages.
