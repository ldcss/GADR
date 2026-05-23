# 7. use-coveralls-for-monitoring-test-coverage

Date: 2020-09-11

## Status

Accepted

## Context

We want to keep our test coverage as high as possible without having to run manual checks as these take time.

## Decision

Use the free tier of Coveralls to give us statistics and to give our pull requests feedback.

## Consequences

- The free tier only works on public repositories.
- Pull request feedback should help us spot patches in coverage and continuously improve it
- The later we add this gem the harder it will be to achieve a high coverage
