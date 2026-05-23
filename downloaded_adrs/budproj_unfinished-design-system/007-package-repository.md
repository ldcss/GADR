# ADR 7: Package Repository

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)
  * [Updates](#updates)

## Context

To use our packages, we need to deploy in a given repository. There are a bunch of options, from on-premise servers to private registries. We must evaluate all of those and choose the most suitable for us.

## Decision

We've decided to use [Github Packages](https://github.com/features/packages). It is straightforward to set up and use, and we're already using other Github tools.

Also, our team has a good experience with it, and that can boost our development speed.

## Status

**DEPRECATED** _check [update 1](#update-1)_

## Consequences

Since we're not self-hosting this server, if we need to integrate with our cluster in a more complex way, we can have some issues or pay high amounts of networking per deployment.

In the future, we should consider changing this and moving to an on-premise solution.

---

## More reading

* [Github packages' docs](https://github.com/features/packages)

## Updates

### Update 1

After [business/ADR#001](https://github.com/budproj/architecture-decision-log/blob/main/records/business/001-reducing-initial-technical-complexity.md), we've decided to stop the development of a decoupled design system.
