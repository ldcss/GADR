# 5. Testing

Date: 2019-03-06

## Status

Accepted

## Context

Testing is necessary to ensure code quality:

- Unit tests
- Integration tests
- Visual regression tests

## Decision

Use Jest+Enzyme and snapshot testing.

Jest is used as the main testing framework. Snapshot testing, which is a feature of Jest, is also used and helps prevent visual regression.

Enzyme is used as a utility of Jest to test React components.

## Consequences

- Unit tests can work as code documentation and prevent breakage.
- Jest is developped by Facebook and used by many React developers. This helps make sure they work well together.
