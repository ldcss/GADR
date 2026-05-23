# ADR 0009: Open Source

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)

## Context

Our product, by its nature, deals with a massive number of possible integrations. It is almost impossible for us to develop and maintain all available integrations with multiple data sources. If we want to survive and evolve in an ecosystem like this, we must solve that issue.

## Decision

Based on the stated context, we've decided to go open-source for our entire codebase. Every new application our developers think must consider it's community, collaborations, and possible improvements. By doing so, we increase our ecosystem coverage, security, and allow modifications and customizations by our customers.

## Status

Accepted.

## Consequences

Any new application should be well-designer. Also, our developers must put the community first and even think in terms of developer experience. We can never commit any secret or credential, and our software should be decoupled enough to allow improvements from external contributors.
