# ADR 0006: Test-Driven Development

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)
  * [Updates](#updates)

## Context

Our product changes a lot. We deploy new features every day. This scenario increases the complexity of quality assurance and makes it overwhelming to ensure that all components are working correctly. We can't afford to reduce our development speed, so we must create a different way to ensure quality.

## Decision

We've decided to start using the Test-Driven Development technique. This process creates a simple way to ensure quality while it improves the reliability of our applications.

Instead of coding your feature immediately, you must follow this Test-Driven Development cycle:
1. You code a test that fails (testing the non-existent feature).
2. You develop that feature.
3. You make the test pass.
4. You refactor that feature to improve it without breaking the test.

It is a simple, yet powerful cycle.

We can develop multiple types of test, but below we've listed the most useful for us:

* **End-to-end tests:** Tests the entire system, integrating every required dependency to make a trial close to the production environment.
* **Acceptance tests:** Tests a feature of a system, mocking every external application dependency.
* **Contrac tests:** Tests the contract between two (or more) integrated microservices.
* **Unit tests:** Tests the behavior of a given function, mocking all file dependencies.

In this decision, we've decided to use at least some form of testing in all applications.

## Status

**REJECTED** _check [update 1](#update-1)_

## Consequences

Test-Driven Development decreases the development speed when a developer is learning a new context, but it increases the pace after that developer understands how that context works. We should not change our developers from context too much, since this could reduce their development speed.

---

## More reading

* [Simple TDD cycle](https://www.devmedia.com.br/test-driven-development-tdd-simples-e-pratico/18533)

## Updates

### Update 1

After [ADR#0014](0014-reducing-initial-complexity.md), we've decided that TDD is way too complicated for our initial release. We plan to add it shortly, but not in our MVP.
