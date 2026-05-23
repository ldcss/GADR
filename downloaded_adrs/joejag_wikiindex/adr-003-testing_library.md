# Testing library

## Context

* We want to write programmer tests to support a TDD workflow.
* We want to be able to mock out functions.

## Decision

* We will use Midje to test our code.
* Despite it's heavy macro design, it allows you to write expressive code and easily makes mocks

## Alternatives Considered

* The inbuilt (deftest). We felt it was less expressive than Midje.
