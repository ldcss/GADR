# 2. Continuously deliver with Travis CI

Date: 2018-10-09

## Status

Accepted

## [Context](https://github.com/libero/community/issues/13)

Libero needs automated and human feedback over pull requests and release candidates.

## Decision

We will provide Travis CI builds for all repositories, covering both testing and deployment to a demo environment.

## Consequences

Sandboxing on someone else's hardware relieves us of the maintenance burden.

There is limited capability to customize the environment of builds, remove duplication between pipelines, or tune their performance.
