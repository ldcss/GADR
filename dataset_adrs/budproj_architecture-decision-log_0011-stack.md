# ADR 0011: Stack

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [Updates](#updates)

## Context

Since we're a new company, being consistent with our tech stack can help us training our engineering team and boosting our contributions to the community. Many companies are too flexible in their tech stack, which creates a complexity hell, with no standards, low quality, and many strange decisions.

Our stack should not be inflexible. We should decide a **primary** stack that a developer should use if there is no good reason to avoid them. For example, a developer from the economic context could choose Clojure instead of our primary stack, but the developer should have a good reason for it.

## Decision

Below, I've listed the current stack of our company. We've grouped those into layers, each one being responsible for a different part of our company:

### Presentation Layer

This layer is responsible for presenting interfaces for our customers' interaction. We currently don't have any machine interface, since most of our applications are web or mobile apps.

Based on that, here is the stack definition for our presentation layer:

* **Programming language:** Javascript
* **Runtime:** NodeJS
* **Superset:** Typescript
* **Framework:** NextJS
* **Interface Library:** React
* **State management:** Recoil
* **Design System:** Custom, based in Material-UI

### Business Layer (Application + Domain)

This layer merges our Application and Domain layers. It is responsible for our API and domain execution. It controls and orchestrates our presentation layer and external services. It must be a easy to use, scalable, lightweight structure since our presentation layer would rely on it for processing.

Based on that, here is what we've chosen as our stack:

* **Language:** Javascript
* **Runtime:** NodeJS
* **Superset:** Typescript
* **Framework:** Koa

### Infrastructure Layer

Although most definitions for this layer resides inside the platform's repositories, some are meaningful enough to mention in this ADR:

* **Relational Database:** PostegreSQL

As I've said before, this stack is flexible, but you should have a good reason to avoid it.

## Status

Accepted.

## Consequences

Defining a solid stack will make hiring and training investments higher. But, with a well-defined stack, the quality of our architecture and code tends to improve, since we can share more knowledge between contexts.

Also, none of the defined patterns are permanent. Anyone can submit a proposal in this ADR and suggest changes to it.

## Updates

### Update 1

After [ADR#0014](0014-reducing-initial-complexity.md), we've decided to change our stack to a more MVP-like structure.
