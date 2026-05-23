# 2. Common Go Linter

Date: 2019-03-25

## Status

Accepted

## Context

The `mysql-monitoring-release` comprises several self-contained `src` modules.
The expectation is that each contains a `bin` directory, with a `test` bash
script representing the set of unit tests for a given module.

This approach makes sense, but is leading to some copied linting code.

## Decision

We considered:
1. Making a separate module that each of the other modules' tests would source 
1. Pulling the linting code out of the modules entirely, and putting it in CI

Both options eliminate the redundant, difficult-to-maintain copypasta.

We opted for option 1, as we felt that it enabled the quickest feedback loop on
code formatting, because it still existed inside of the `bin/test` scripts.

## Consequences

We believe we've maintained the ease-of-use of the original approach, while
reducing code duplication.
