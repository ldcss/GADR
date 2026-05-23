# ADR 2: Unit Testing Tools

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)
  * [Updates](#updates)

## Context

Our company [is using TDD](https://github.com/budproj/architecture-decision-log/blob/main/records/patterns/006-test-driven-development.md) as a pattern for development. To achieve this, we must decide which unit testing tool fits the most with our design system environment.

## Decision

We've decided to use Jest with Enzyme.

Jest is an incredible unit testing tool for Javascript. It is easy to use, has a great syntax, and our team is familiar with it.

Enzyme, on the other hand, is a unit testing tool for React components. It has some libraries that help us debugging and testing those resources.

We've decided on this stack because our team has already used it in the past, and it can improve our development speed.

## Status

**DEPRECATED** _check [update 1](#update-1)_

## Consequences

We've searched about it, and it seems that this is still the optimal TDD stack in Javascript. We may not handle any consequences with it.

---

## More reading

* [Jest's docs](https://jestjs.io/docs/en/getting-started)
* [Enzyme's docs](https://enzymejs.github.io/enzyme/docs/api/)

## Updates

### Update 1

After [business/ADR#001](https://github.com/budproj/architecture-decision-log/blob/main/records/business/001-reducing-initial-technical-complexity.md), we've decided to stop the development of a decoupled design system.
