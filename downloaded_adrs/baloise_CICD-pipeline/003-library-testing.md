# 3. Library testing

Date: 2020-11-02

## Status

Recommended

## Context

What is our testing strategy in terms of tooling, coverage and test types.

how to test
- unit tests
- testing libs / frameworks
- testing approaches
- what to test
- how to e2e test before merging / releasing
- architecture check

## Decision

- For every public groovy Class method there is at least one unit test
- We aim for 100% branch coverage
- we use JUnit 4 
- we use AssertJ
- we use ArchUnit

## Consequences

Every PR needs to be checked by reviewers carefully, not only production but also testing code.