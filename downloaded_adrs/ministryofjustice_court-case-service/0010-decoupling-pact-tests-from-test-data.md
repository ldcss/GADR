# 10. Decoupling Pact tests from test data

Date: 2022-01-13

## Status

Accepted

## Context

The data backing some of our Pact states is created in the `before-test.sql`. This SQL was originally intended for application local integration tests. Unfortunately by using this same data for Pact testing we've coupled this data with the prepare-a-case Pact tests which means any changes to our integration test data can potentially break the prepare-a-case contract; and by extension both the court-case-service and prepare-a-case builds. This makes changes to `before-test.sql` incredibly risky as changes may need to be made not only to our integration tests, but also our Pact tests and those of prepare-a-case. The prepare-a-case codebase itself has similar coupling issues between its integration/pact data and so an inconsequential change to `before-test.sql` can create huge amounts of otherwise unnecessary work.

To a lesser extent, data defined in `before-test.sql` which is used in multiple integration tests can lead to more localised problems with unrelated integration tests within court-case-service breaking.

# Decision

1. Pact tests should use mocks at the service level to avoid coupling with integration test data. 
2. (Under review) To avoid similar situations arising in local integration tests we should be open to creating new test data per test rather than re-using `before-test.sql`.

## Consequences

- Introduces some overhead and repetition when writing new Pact tests
- Isolates any changes required as a result of our internal test data or client contracts changing after the fact
- For data only used locally developers will need to use their discretion regarding the trade-off between repetition and isolation
