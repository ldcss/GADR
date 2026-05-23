# 3. Run a subset of all tests different for each project

Date: 2017-09-15

## Status

Accepted

## Context

A full test suite run may take > 10 minutes, so we should only run tests that are necessary. 

While testing project A, running tests that only check projects B, C, ... does not contribute to the testing of A. Especially if the code from A is not exercised.

While testing project A, tests that fail due to instability on other services B and C do not contribute to the testing of A in the same way.

## Decision

For each project, run a subset of the tests marked with `@pytest.mark.projectname`.

## Consequences

All tests should have at least an annotation with `@pytest.mark`, otherwise they don't serve any project.

Tests may have multiple annotations with `@pytest.mark`, as they test multiple projects working together.

