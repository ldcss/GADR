# 13. Use Normalize.css to normalize styles across browsers

Date: 2019-10-20

## Status

Accepted

## Context

Browsers often have subtle differences or bugs in their default styles.
Traditional CSS resets attempt to clear all styling, creating a baseline style
from which to build us custom styles. However, this approach often results in
reapplying styles that were already implemented by the browser.
[Normalize.css](http://necolas.github.io/normalize.css/), instead, normalizes
styles to a common theme across browsers. It precisely targets only the styles
that need normalizing.

## Decision

We will use Normalize.css to normalize browser default styles.

## Consequences

With style normalization, we can be confident that our styles will be consistent
across browsers. This does not replace the need to test in all target browsers.
