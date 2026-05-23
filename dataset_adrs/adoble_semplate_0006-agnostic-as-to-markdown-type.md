# Agnostic as to markdown type

* Status: Accepted
* Date: 2021-02-18

## Context and Problem Statement

More then one type of markdown exists. Which one should be supported?

## Considered Options

* Support [GitHub Flavored Markdown - GFM](https://guides.github.com/features/mastering-markdown/)
* Support [CommonMark](https://commonmark.org/)
* Support [AsciiDoc](https://asciidoc.org/)

## Decision Outcome

The library can handle all forms of markdown.

### Positive Consequences <!-- optional -->

* The form of markdown used is determined by the user supplied template.


### Negative Consequences <!-- optional -->

* The library can only use a subset of the features that are common to all markdown languages (e.g. single new lines are ignored).
