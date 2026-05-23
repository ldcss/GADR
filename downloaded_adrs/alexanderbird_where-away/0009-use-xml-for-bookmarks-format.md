# 9. use xml for bookmarks format

Date: 2020-11-12

## Status

Accepted

Relates To [10. use a different html parser for testing](0010-use-a-different-html-parser-for-testing.md)

## Context

Options:
 - custom format, custom parser
  - that's a lot of work
 - json
  - awkward format for depicting a tree
 - yaml
  - significant whitespace makes this more error-prone, and the bookmarks file
    is likely to be edited frequently
 - xml
  - classic
  - shows trees well
  - less error prone to edit
  - not supported natively in node
    - neither parsing nor schema validation
    - schema is simple enough that I could hand-roll a validator
    - see discussion on parsing -- it needs a library: https://stackoverflow.com/questions/11398419/trying-to-use-the-domparser-with-node-js
      - top two promising libraries:
        - jsdom, 32 dependencies https://www.npmjs.com/package/jsdom
        - xmldom, 0 dependencies https://www.npmjs.com/package/xmldom

## Decision

Use XML for the bookmarks format. Use
[xmldom](https://www.npmjs.com/package/xmldom) to parse, and hand-roll the
validation.

## Consequences

This is our first dependency that needs to be shipped with the package :(

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
