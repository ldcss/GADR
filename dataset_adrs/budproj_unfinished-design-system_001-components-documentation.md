# ADR 1: Components Documentation

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)
  * [Updates](#updates)

## Context

In mature design systems, one of the most common misconceptions is not documenting your components. We need good documentation to understand when and how to use each one of those. Our documentation doesn't need to be overly detailed, but a simple list of components, with their props,  would be enough.

## Decision

We've decided to use [Storybook](https://storybook.js.org/). This tool helps us document our components and develop them since we can make a simple canvas to interact with it.

Some major companies with mature design systems use this tool, which could be a precious asset.

## Status

**DEPRECATED** _check [update 1](#update-1)_

## Consequences

Since this is a new tool, it can be challenging for some developers to start using it. Also, there is a period where our team is going to deploy and optimize it.

---

## More reading

* [Storybook's docs](https://storybook.js.org/docs/react/get-started/introduction)

## Updates

### Update 1

After [business/ADR#001](https://github.com/budproj/architecture-decision-log/blob/main/records/business/001-reducing-initial-technical-complexity.md), we've decided to stop the development of a decoupled design system.
