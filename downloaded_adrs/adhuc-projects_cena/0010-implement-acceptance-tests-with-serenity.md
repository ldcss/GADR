# 10. Implement acceptance tests with Serenity

Date: 2019-02-06

## Status

Accepted

## Context

[Defining acceptance tests with Cucumber](0009-test-features-with-cucumber.md) will help writing user-oriented acceptance
scenarii. However, to help maintaining an acceptance tests client library, we need to organize this library to be
extensible, without mixing concerns between Gherkin interpreter and API unitary client steps.

The acceptance tests results report must be readable and help investigating in case of error, providing hints about
what wrong happened during API calls.

## Decision

The [Serenity](http://www.thucydides.info/#/) framework will be used to define the acceptance tests library.

## Consequences

Acceptance tests library classes will be separated between Gherkin interpreter, acting as an orchestrator for unitary
client steps and those client steps.

Each API resource will have its dedicated package for each layer.
