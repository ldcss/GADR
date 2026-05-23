# ADR 6: Yarn Workspaces

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [Experience Report](#experience-report)
  * [More reading](#more-reading)
  * [Updates](#updates)

## Context

In a monorepo, it is common to miss dependencies and use `yarn link` to create links between packages. We need to find a tool to improve our development experience.

## Decision

We've decided to use [Yarn Workspaces](https://classic.yarnpkg.com/en/docs/workspaces/) integrated with Lerna to solve those problems. It has some promising features that can improve our experience and create more sustainable development environments.

## Status

**DEPRECATED** _check [update 1](#update-1)_

## Consequences

There are some complaints from the community about this tool. We've already used it, but we should watch us not to fall into those issues.

---

## Experience Report

We've started using it, and some problems appeared, especially while importing linked packages and peer dependencies.

## More reading

* [Yarn Workspaces' docs](https://classic.yarnpkg.com/en/docs/workspaces/)

## Updates

### Update 1

After [business/ADR#001](https://github.com/budproj/architecture-decision-log/blob/main/records/business/001-reducing-initial-technical-complexity.md), we've decided to stop the development of a decoupled design system.
