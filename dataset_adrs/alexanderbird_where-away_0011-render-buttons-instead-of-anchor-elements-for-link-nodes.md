# 11. render buttons instead of anchor elements for link nodes

Date: 2020-11-15

## Status

Accepted

## Context

- semantically, an html element that takes you to a new web page when you click
  it is an anchor -- `<a>`.
- I'd like tab navigation and the Enter key to work for navigating between
  bookmarks.
  - buttons can be accessed via Tab and activated via Enter
  - not so with an anchor tag. See
    https://stackoverflow.com/questions/41476292/how-to-give-focus-to-anchor-tag-without-href,
    etc.

## Decision

Model the links as `<button>` elements to make the interaction more normal.

## Consequences

Maybe this is the wrong decision. Down the road, if there's a good reason to go
back to anchor elements for the links, then we can add the extra bits and bobs
to make Tab and Enter work as expected for them.

It's a two-way door.
