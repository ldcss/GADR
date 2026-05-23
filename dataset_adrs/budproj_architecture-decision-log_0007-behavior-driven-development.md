# ADR 0007: Behavior-Driven Development

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)
  * [Updates](#updates)

## Context

Developing new features are, in general, a way of achieving business requirements. Business people express those requirements at scrum meetings in stories. It is common for developers not to understand the needs properly, creating a massive gap between business expectations and developed software.

## Decision

We are going to use Behavior-Driven Development to help us reduce that gap. BDD is a technique where we use User Stories to create acceptance tests based on user behaviors.

Instead of writing complex test statements, we use a BDD tool to create a readable phrase, like the following:

```txt
Given a new created user
When that user places a new order
Then a notification must be sent
```

Each line of that phrase relates to a given function that will execute steps and persist the state machine's context. We can use assertions to return errors along the way.

BDD is a powerful tool that enhances our TDD cycle.

## Status

**REJECTED** _check [update 1](#update-1)_

## Consequences

This technique increases the complexity of small services. Since we will divide our microservices by in our bounded contexts, we should not suffer from these consequences.

Yet, we must train our developers to use BDD, and also, the product team must keep their interest in contributing to the software development process.

---

## More reading

* [Behavior-Driven Development @Cucumber](https://cucumber.io/docs/bdd/)

## Updates

### Update 1

After [ADR#0014](0014-reducing-initial-complexity.md), we've decided that TDD is way too complicated for our initial release. We plan to add it shortly, but not in our MVP.
