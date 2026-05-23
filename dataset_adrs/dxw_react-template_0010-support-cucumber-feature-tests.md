# 10. Support Cucumber feature tests

Date: 2019-10-13

## Status

Accepted

## Context

We want to be able to express the acceptance tests for features in a human
readable format. This would make it easier for non-technical people to
understand what tests we have and maybe even write new ones.

[Cucumber](https://cucumber.io/) is a tool for running automated tests written
in plain language.

## Decision

We will support writing feature tests in Cucumber. We will still support feature
tests not written in Cucumber.

## Consequences

Using Cucumber makes it easier to build a shared understanding of what is tested
and what isn't, to ensure we are testing features against the correct acceptance
criteria.
