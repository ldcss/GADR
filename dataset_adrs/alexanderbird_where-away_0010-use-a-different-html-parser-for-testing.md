# 10. use a different html parser for testing

Date: 2020-11-14

## Status

Accepted

Relates To [9. use xml for bookmarks format](0009-use-xml-for-bookmarks-format.md)

## Context

It's useful to parse snippets of the rendered html to assert on them easier
(e.g. in transform.js unit tests). 

The xml parser we bundle with the app can technically parse html, but it doesn't
seem to support basic operations like `innerHTML`. That's a major nuisance.

JSDom is a mature and popular html parsing library.

## Decision

Add [JSDom](https://www.npmjs.com/package/jsdom) as a dev dependency to parse html in test.

## Consequences

Two similar libraries, one for prod and one for test. Both are similar, but one
is optimized for lightweight xml parsing while the other is optimized for full
html parsing. One is well suited for bundling with the app (minimal
dependencies) while the other is suited for testing (who cares about the deps;
more complete / easy to use interface). 

It could be confusing to a newcomer -- which do I use? That's the cost of
optimization.
