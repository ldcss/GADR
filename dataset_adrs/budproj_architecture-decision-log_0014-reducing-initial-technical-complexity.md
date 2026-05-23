# ADR 0014: Reducing Initil Technical Complexity

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)

## Context

While coding our design-system, our team understood that our technical complexity was too high. Right now, we still don't know precisely what our product is, and we need to receive inputs from our customers as fast as possible. Still, the decisions made until today (2020-10-26 - latest PR [#18](https://github.com/budproj/architecture-decision-log/pull/18)) created a massive technical complexity that is slowing down our development pace.

We need to reconsider some decisions and reduce our technical complexity, to allow a full delivery until the ender of 2020 Q4.

## Decision

Taking a look at our decisions and considering what we've developed so far (mainly our design system), the major offenders are:

* **Decoupled design system:** Since we have a single presentation application, there is no reason to code a stable and robust design system.
* **Using ThemeUI:** A more opinionated framework would provide more tools to reduce our time coding simple components.
* **Decoupled Application and Domain layers:** Since we don't have any users, scalability and reliability are not our primary concerns.
* **CQRS+ES:** Although relevant, this structure adds enormous complexity to our back-end, increasing the required time to develop our systems.
* **Test and behavior-driven development:** Unit and acceptance tests are essential tools to reduce side-effects while refactoring or coding new features. But, they increase the development time and can slow our pace.
* **Stack:** Some tools that we've decided to use are new for our team. We must reduce our learning curve by using familiar and straightforward languages and frameworks.

Based on those offenders, here is a list of actions that we're going to take to reduce our technical complexity:

1. We're going to reject [ADR#0005](005-cqrs+es.md). Our first version will **not** be event-sourced, but we can add it in future releases.
2. We're going to submit an update in [ADR#0013](/0013-microservices-overview.md) to merge our application and domain applications layers into a **business** application that crosses both layers. That is not optimal and will create legacy code in the future, but will increase our development speed considerably.
3. We're going to remove our design-system application in [ADR#0013](0013-microservices-overview.md) and archive the [design-system repository](https://github.com/budproj/design-system) until further notice. Our first release will have only a single presentation application, so there is no sense in having a robust and complex design-system.
4. We're going to deprecate [the entire design-system ADL](https://github.com/delucca/design-system/tree/feature/design-system-structure/docs/adl). Since we're not using a design-system anymore, there is no sense in maintaining them.
5. We're going to move from ThemeUI to MaterialUI since our team already has good knowledge of it, which can boost our development speed.
6. We're going to reject both [ADR#0006](006-test-driven-development.md) and [ADR#0007](007-behavior-driven-development.md). TDD and BDD are great, and we're going to use them shortly, but they would add little benefit to our first version.
7. We're going to submit a change request to [ADR#0011](011-stack.md), moving from an optimal stack to a more MVP-like stack.

## Status

Accepted.

## Consequences

Plenty of problems can occur based on this ADR. But, the most relevant one is that we're now creating legacy code for future developers. That is not-optimal, but we must first understand our audience and optimize our code based on our customer needs.

Remembering the engineering complexity formula:

```txt
Engineering Complexity = Domain Complexity + Technical Complexity + Legacy Complexity
```

Our first release must focus on our `Domain Complexity`, and not the `Technical Complexity`. So, we're coding modern applications with a good (but not optimal) framework and tools.

As soon as we reach a product-market fit, we suggest refactoring the entire code and architecture. By doing so, we can divide bounded contexts and improve our developer experience.
