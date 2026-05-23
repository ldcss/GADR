# 20. Managing versions of dependencies

Date: 2022-12-12

## Status

Accepted

## Context

UaL is looking to keep dependencies as up to date as possible whilst not merging
new dependencies straight away to avoid issues around dependency poisoning.

This is advantageous as it makes upgrades a lot easier and gives us the latest features to
use in our code.

## Decision

- Bundle minor and patch updates into a single PR which runs against a full PR environment. Created every Monday.
- Major updates to run separately against a full PR environment. Created every Monday.
- Security updates to run daily against reduced workflow that only does unit tests and builds.

## Consequences

We should be able to quickly merge security vulnerabilities whilst ensuring that major updates
and the 'minor and patch' bundled updates are fully tested against AWS infra.
