# ADR 5: Lerna

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)
  * [Updates](#updates)

## Context

Since we're developing a monorepo with multiple packages, we need to find a way to improve our build experience and how to deploy our packages.

## Decision

We've decided to use [Lerna](https://lerna.js.org/) as the tool for our deployment. It has incredible features (such as automatic versioning), and it helped us a lot.

Our team has already used it in previous projects, so it will easy to set up and keep that tool.

## Status

**DEPRECATED** _check [update 1](#update-1)_

## Consequences

There are no hard consequences for it. We've used Lerna before, and no problems until now.

---

## More reading

* [Lerna's docs](https://lerna.js.org/)

## Updates

### Update 1

After [business/ADR#001](https://github.com/budproj/architecture-decision-log/blob/main/records/business/001-reducing-initial-technical-complexity.md), we've decided to stop the development of a decoupled design system.
