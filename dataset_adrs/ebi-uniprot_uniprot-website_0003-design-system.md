# 3. Design System

Date: 2019-03-06

## Status

Accepted

## Context

In order to provide a consistent UI, we need to use a design system. This design system also helps reduce the amount of code required, and ensures designers and developers speak the "same language".

## Decision

We have created our own design system/pattern librarly, [Franklin](https://ebi-uniprot.github.io/franklin-sites). It is built on top [Foundation](https://foundation.zurb.com/) (Atomic level components) and uses React.js. The library is published to `npm` as [`franklin-sites`](https://www.npmjs.com/package/franklin-sites) and can be used by any React.js website.

## Consequences

- The design system makes it easy to create a consitent UI.
- The design sytem can be used by any React.js website.
- Patterns are defined at a high level then re-used throughout the website.

Things to lookout for:

- Bundle size should be optimised.
- It would be good to eventually remove the dependency on Foundation, which is seldom used.
